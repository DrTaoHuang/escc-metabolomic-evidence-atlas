"""Rebuild the public atlas graph using only its public reader and relation inputs.

Python 3.10+; standard library only. No network access or source-data mutation.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import re

SCHEMA_VERSION = "1.0"
RULES = {
    "REL01": "An observation belongs to its accepted result group; membership is not proof of chemical identity or independent replication.",
    "REL02": "A performance record evaluates a registered model/marker identifier; multiple records are not additional independent tests.",
    "REL03": "An original source feature corresponds to an observation through a reviewed exact feature key within the same source.",
    "REL04": "An original source feature is a reported model input through the reviewed feature/performance key; structural identification and independent validation are not inferred.",
    "REL05": "A topic cites an explicitly registered report; report citation does not assign every result in that report to the topic.",
    "REL06": "A clinical table row describes an explicitly keyed observation, performance or model; a table row is not an additional study or patient.",
    "REL07": "An explicit reader-record link identifies its report, study or cohort/dataset context; it does not establish participant independence or synthesis eligibility.",
    "REL08": "A registered source/dataset relationship is retained from an explicit ledger row; report-level arrays are not crossed to invent pairs.",
    "REL09": "A support record preserves a reported pathway/compound mapping; it does not establish a measured molecular identity, mechanism or observation-level connection.",
    "REL10": "Reviewed theme membership identifies the exact record and its role; membership is not a new evidence grade or claim of independent replication.",
    "REL11": "A topic row belongs to its clinical-use topic; the counting unit remains a supplementary-table row.",
}
RECORD_KINDS = {
    "reports": "report", "observations": "observation", "supports": "support",
    "performances": "performance", "groups": "group", "topics": "topic",
}
EXTRA_KINDS = {"study", "cohort", "dataset", "model", "feature", "pathway", "compound"}
ENTITY_FIELDS = {"reportIds": "report", "studyIds": "study", "cohortIds": "cohort", "datasetIds": "dataset"}
BASE_TABLE = {"reports": "S3", "observations": "S17", "supports": "S18", "performances": "S9", "groups": "S16"}
ALLOWED_TYPES = {
    "observation_group", "performance_model", "feature_observation", "feature_model_input",
    "topic_cites_report", "clinical_row_observation", "clinical_row_performance", "clinical_row_model",
    "record_report", "record_study", "record_cohort_context", "record_dataset_context",
    "source_study", "dataset_source", "dataset_report", "support_pathway_mapping", "support_compound_mapping",
    "topic_row", "topic_observation", "topic_support", "topic_performance", "topic_group", "topic_priority",
}


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def canonical_digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def node_id(kind, public_id):
    return kind + ":" + str(public_id)


def ids(record, field):
    return list(record.get(field, []))


def context_for(record, section):
    result = {key: record[key] for key in ("matrix", "comparison", "timepoint", "direction", "validation") if key in record}
    if "use" in record:
        result["reportedUse" if section in ("observations", "groups", "supports") else "use"] = record["use"]
    if section in ("observations", "groups") and "identity" in record:
        result["identityQualification"] = record["identity"]
    if section == "supports" and "identity" in record:
        result["evidenceLayer"] = record["identity"]
    if section == "performances":
        result["inputFeatures"] = record.get("identity", "")
        result["validationRole"] = record.get("validationRole", "")
        result["originalRecordStatus"] = record.get("direction", "")
    if section == "groups":
        result["synthesisClass"] = record["synthesisClass"]
    if section == "topics" and "category" in record:
        result["topicCategory"] = record["category"]
    return result


def source_ref(record, section, topic=None):
    table = BASE_TABLE.get(section)
    if table is None:
        table = (record.get("tableIds") or (topic or {}).get("tableIds") or ["S11"])[0]
    locators = [detail["value"] for detail in record.get("details", []) if detail.get("label") in ("原报告定位", "原始报告定位")]
    locator = "\n".join(dict.fromkeys(locators)) if locators else f"Supplementary Table {table}, reader entry {record['id']}."
    return {"tableId": table, "recordId": record["id"], "locator": locator}


def record_node(record, section):
    node = {
        "id": node_id(RECORD_KINDS[section], record["id"]), "kind": RECORD_KINDS[section],
        "label": record.get("title", record["id"]), "labelEn": record.get("title", record["id"]),
        "labelZh": record.get("title", record["id"]), "recordKind": section, "recordId": record["id"],
        "context": context_for(record, section), "reportIds": [record["id"]] if section == "reports" else ids(record, "reportIds"),
        "studyIds": ids(record, "studyIds"), "cohortIds": ids(record, "cohortIds"), "datasetIds": ids(record, "datasetIds"),
    }
    if section == "topics":
        node["topicId"] = record["id"]
    return node


def readable_id(kind, public_id):
    en = {"study": "Study unit", "cohort": "Source cohort", "dataset": "Analytic dataset", "model": "Model/marker"}[kind]
    zh = {"study": "研究单元", "cohort": "来源队列", "dataset": "分析数据集", "model": "模型/标志物"}[kind]
    return en + " " + public_id, zh + " " + public_id


def build(reader, reviewed):
    if reviewed.get("schemaVersion") != SCHEMA_VERSION:
        raise ValueError("Unsupported public relation-input schema")
    if reviewed.get("readerCanonicalSha256") != canonical_digest(reader):
        raise ValueError("Reviewed relations are not bound to this reader dataset")
    nodes = {}
    records = {}
    for section in RECORD_KINDS:
        for record in reader[section]:
            n = record_node(record, section)
            if section == "topics":
                n["labelEn"] = reviewed.get("labels", {}).get(n["label"], n["label"])
            assert n["id"] not in nodes, n["id"]
            nodes[n["id"]] = n
            records[(section, record["id"])] = record

    for field, kind in ENTITY_FIELDS.items():
        if kind == "report":
            continue
        for public_id in sorted({value for report in reader["reports"] for value in ids(report, field)}):
            en, zh = readable_id(kind, public_id)
            nodes[node_id(kind, public_id)] = {
                "id": node_id(kind, public_id), "kind": kind, "label": en, "labelEn": en, "labelZh": zh,
                "recordKind": None, "recordId": None, "context": {},
                "reportIds": sorted(report["id"] for report in reader["reports"] if public_id in ids(report, field)),
                "studyIds": [public_id] if kind == "study" else [],
                "cohortIds": [public_id] if kind == "cohort" else [],
                "datasetIds": [public_id] if kind == "dataset" else [],
            }
            if kind in ("cohort", "dataset"):
                # Retain the already public source/dataset explanations without
                # converting their qualifications into a new eligibility grade.
                matching = [detail for report in reader["reports"] if public_id in ids(report, field)
                            for detail in report.get("details", []) if re.search(r"\b" + re.escape(public_id) + r"\b", detail["label"])]
                nodes[node_id(kind, public_id)]["details"] = list({compact(detail): detail for detail in matching}.values())

    by_model = defaultdict(list)
    for performance in reader["performances"]:
        by_model[performance["modelId"]].append(performance)
    for public_id, performances in sorted(by_model.items()):
        en, zh = readable_id("model", public_id)
        title = performances[0]["title"]
        nodes[node_id("model", public_id)] = {
            "id": node_id("model", public_id), "kind": "model", "label": title, "labelEn": title, "labelZh": title,
            "recordKind": None, "recordId": None, "modelId": public_id,
            "context": {"use": sorted({use for p in performances for use in p["use"]}), "performanceIds": sorted(p["id"] for p in performances)},
            **{field: sorted({value for p in performances for value in ids(p, field)}) for field in ENTITY_FIELDS},
        }

    for topic in reader["topics"]:
        for row in topic.get("records", []):
            n = record_node(row, "topics")
            n.update(id=node_id("topicRow", row["id"]), kind="topicRow", recordKind="topics", recordId=topic["id"],
                     topicId=topic["id"], topicRowId=row["id"], context={"use": row.get("use", []), "topicCategory": topic["category"], "rowUnit": "supplementary table row"})
            assert n["id"] not in nodes, n["id"]
            nodes[n["id"]] = n
            records[("topicRows", row["id"])] = row

    for extra in reviewed.get("additionalNodes", []):
        assert extra["kind"] in EXTRA_KINDS, extra
        assert extra["id"].startswith(extra["kind"] + ":"), extra
        if extra["id"] in nodes:
            # Explicit public entity metadata may enrich a registry node, but may
            # not change its type, neutral identifier or source-reference arrays.
            assert extra["kind"] == nodes[extra["id"]]["kind"]
            for field in ("label", "labelEn", "labelZh", "details", "sourceRefs"):
                if field in extra:
                    nodes[extra["id"]][field] = extra[field]
            nodes[extra["id"]]["context"].update(extra.get("context", {}))
        else:
            assert all(field in extra for field in ("label", "labelEn", "labelZh", "context", "reportIds", "studyIds", "cohortIds", "datasetIds")), extra
            nodes[extra["id"]] = extra

    edges = {}

    def add(source, target, edge_type, rule, source_refs, context=None):
        assert source in nodes and target in nodes, (source, target)
        assert edge_type in ALLOWED_TYPES and rule in RULES, (edge_type, rule)
        assert source_refs and all(ref.get("tableId") and ref.get("recordId") and ref.get("locator") for ref in source_refs), source_refs
        ctx = {"relationStatus": "explicit", **(context or {})}
        # IDs are stable neutral endpoint IDs, not dates, extraction IDs or file
        # hashes. A source membership occurrence deliberately retains duplicates.
        suffix = ""
        for field in ("membershipOccurrence", "role"):
            if field in ctx:
                suffix += "-" + re.sub(r"[^A-Za-z0-9_-]", "_", str(ctx[field]))
        identifier = "E-" + edge_type + "-" + source.replace(":", "_") + "-" + target.replace(":", "_") + suffix
        refs = sorted(source_refs, key=lambda value: (value["tableId"], value["recordId"], value["locator"]))
        edge = {"id": identifier, "source": source, "target": target, "type": edge_type, "context": ctx, "sourceRefs": refs, "rule": rule}
        if identifier in edges:
            prior = edges[identifier]
            assert prior["context"] == ctx and prior["rule"] == rule, identifier
            prior["sourceRefs"] = sorted({compact(ref): ref for ref in prior["sourceRefs"] + refs}.values(), key=lambda value: (value["tableId"], value["recordId"], value["locator"]))
        else:
            edges[identifier] = edge

    for section in ("reports", "observations", "supports", "performances", "groups"):
        for record in reader[section]:
            source = node_id(RECORD_KINDS[section], record["id"])
            ctx = {"recordKind": section, "recordId": record["id"]}
            if section == "supports":
                ctx["evidenceLayer"] = record.get("identity", "")
            if section == "performances":
                ctx["validationRole"] = record.get("validationRole", "")
            for field, kind in ENTITY_FIELDS.items():
                for public_id in ids(record, field):
                    if source != node_id(kind, public_id):
                        edge_type = {"report": "record_report", "study": "record_study", "cohort": "record_cohort_context", "dataset": "record_dataset_context"}[kind]
                        add(source, node_id(kind, public_id), edge_type, "REL07", [source_ref(record, section)], ctx)

    for observation in reader["observations"]:
        add(node_id("observation", observation["id"]), node_id("group", observation["groupId"]), "observation_group", "REL01", [source_ref(observation, "observations")])
    for performance in reader["performances"]:
        add(node_id("performance", performance["id"]), node_id("model", performance["modelId"]), "performance_model", "REL02", [source_ref(performance, "performances")], {"validationRole": performance["validationRole"]})
    for topic in reader["topics"]:
        for report_id in topic["reportIds"]:
            add(node_id("topic", topic["id"]), node_id("report", report_id), "topic_cites_report", "REL05", [source_ref(topic, "topics")], {"topicCategory": topic["category"]})
        for row in topic.get("records", []):
            source = node_id("topicRow", row["id"])
            ref = source_ref(row, "topicRows", topic)
            add(source, node_id("topic", topic["id"]), "topic_row", "REL11", [ref])
            for report_id in row["reportIds"]:
                add(source, node_id("report", report_id), "record_report", "REL07", [ref], {"recordKind": "topicRows", "recordId": row["id"]})

    for relation in reviewed.get("relations", []):
        add(relation["source"], relation["target"], relation["type"], relation["rule"], relation["sourceRefs"], relation.get("context"))

    node_list = sorted(nodes.values(), key=lambda node: node["id"])
    edge_list = sorted(edges.values(), key=lambda edge: edge["id"])
    node_counts = dict(sorted(Counter(node["kind"] for node in node_list).items()))
    edge_counts = dict(sorted(Counter(edge["type"] for edge in edge_list).items()))
    scientific_topic_links = sum(edge["type"] == "topic_cites_report" and edge["context"].get("topicCategory") == "science" for edge in edge_list)
    coverage = {
        "readerCounts": reader["counts"], "nodeKinds": node_counts, "edgeTypes": edge_counts,
        "scientificTopics": sum(topic["category"] == "science" for topic in reader["topics"]),
        "scientificTopicReportLinks": scientific_topic_links,
        "clinicalTopicRows": sum(len(topic["records"]) for topic in reader["topics"] if topic["category"] == "clinical"),
        "existingQualityDomainAssessments": sum(len(report.get("quality", [])) for report in reader["reports"]),
        "reviewedInputCoverage": reviewed.get("coverage", {}), "scopeNotes": reviewed.get("scopeNotes", []),
        "units": {"nodes": "typed public entities and records, not patients or unique identified molecules", "edges": "typed documented relations, not independent validations or causal effects", "feature": "original source feature within a stated source", "compound": "external compound identifier used in a reported mapping, not confirmation of a measured compound"},
    }
    assert node_counts["observation"] == reader["counts"]["observations"] == 3846
    assert node_counts["group"] == reader["counts"]["groups"] == 3704
    assert node_counts["performance"] == reader["counts"]["performances"] == 811
    assert node_counts["model"] == reader["counts"]["models"] == 692
    assert edge_counts["observation_group"] == 3846 and edge_counts["performance_model"] == 811
    assert scientific_topic_links == 37
    assert Counter(edge["source"] for edge in edge_list if edge["type"] == "observation_group") == Counter(node_id("observation", record["id"]) for record in reader["observations"])
    assert reader["counts"]["quantitativeEndpoints"] == 0
    return {"schemaVersion": SCHEMA_VERSION, "nodes": node_list, "edges": edge_list, "counts": {"nodes": len(node_list), "edges": len(edge_list)}, "coverage": coverage, "rules": RULES}


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: compact(row[field]) if isinstance(row.get(field), (dict, list)) else row.get(field, "") for field in fields})


def generate(reader_path, relation_path, output):
    reader_bytes = reader_path.read_bytes()
    relation_bytes = relation_path.read_bytes()
    reader = json.loads(reader_bytes.decode("utf-8-sig"))
    reviewed = json.loads(relation_bytes.decode("utf-8-sig"))
    graph = build(reader, reviewed)
    output.mkdir(parents=True, exist_ok=True)
    text = compact(graph)
    (output / "graph.json").write_text(text + "\n", encoding="utf-8", newline="\n")
    (output / "graph-data.js").write_text("window.ESCC_GRAPH=" + text.replace("</", "<\\/") + ";\n", encoding="utf-8", newline="\n")
    write_csv(output / "nodes.csv", graph["nodes"], ["id", "kind", "label", "labelEn", "labelZh", "recordKind", "recordId", "topicId", "topicRowId", "modelId", "context", "reportIds", "studyIds", "cohortIds", "datasetIds", "details", "sourceRefs"])
    write_csv(output / "edges.csv", graph["edges"], ["id", "source", "target", "type", "context", "sourceRefs", "rule"])
    assert reader_path.read_bytes() == reader_bytes and relation_path.read_bytes() == relation_bytes
    return graph


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reader", type=Path, default=here.parent / "evidence.json")
    parser.add_argument("--relations", type=Path, default=here / "reviewed_relations.json")
    parser.add_argument("--output", type=Path, default=here.parent / "atlas-data")
    args = parser.parse_args()
    graph = generate(args.reader, args.relations, args.output)
    print(compact({"nodes": graph["counts"]["nodes"], "edges": graph["counts"]["edges"], "nodeKinds": graph["coverage"]["nodeKinds"], "edgeTypes": graph["coverage"]["edgeTypes"]}))


if __name__ == "__main__":
    main()
