#!/usr/bin/env python3
"""Reproducible descriptive analysis for 2Pair / ConflictLab Human Wave 1 CSV exports.

Method boundary:
- descriptive raw-choice / UX statistics only;
- no CS/CR polarity inference;
- no Gate D mapping;
- no psychological interpretation of latency/intensity;
- no automatic KEEP/REVISE/REJECT or supported/cross-load verdict.

Blind coding helpers create study-local aliases and a separate alias key. The key is
sensitive research material and must not be committed or shown to blind coders before
coding lock.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import secrets
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

EXPECTED_PAIRS = {
    "CS-PR-01", "CS-RE-01", "CS-CA-01",
    "CR-PZ-01", "CR-FS-01", "CR-PO-01",
}
REQUIRED_COLUMNS = {
    "participant_id", "candidate_id", "protocol_version", "presentation_index",
    "top_asset", "bottom_asset", "choice_position", "chosen_asset", "free_text",
    "intensity", "hard_to_identify", "latency_ms", "excluded",
}
NO_CLEAR_VALUES = {"no clear choice", "no_clear_choice", "none", "—", "-"}
REASON_CLASSES = {"supported", "cross-load", "insufficient", "NONE"}
CONFOUNDS = {
    "aesthetics", "composition", "utility", "familiarity",
    "social_desirability", "salience_novelty", "other", "none", "",
}


def _clean(value: Optional[str]) -> str:
    return (value or "").strip()


def _num(value: Optional[str]) -> Optional[float]:
    text = _clean(value)
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _int(value: Optional[str]) -> Optional[int]:
    n = _num(value)
    return None if n is None else int(n)


def load_rows(paths: Sequence[Path]) -> List[dict]:
    rows: List[dict] = []
    for path in paths:
        with path.open("r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            columns = set(reader.fieldnames or [])
            missing = REQUIRED_COLUMNS - columns
            if missing:
                raise ValueError(f"{path}: missing required columns: {', '.join(sorted(missing))}")
            for row in reader:
                item = dict(row)
                item["_source_file"] = path.name
                rows.append(item)
    return rows


def is_excluded(row: dict, excluded_participants: set[str]) -> bool:
    if _clean(row.get("participant_id")) in excluded_participants:
        return True
    return _clean(row.get("excluded")).lower() in {"1", "true", "yes", "y"}


def choice_kind(row: dict) -> str:
    pos = _clean(row.get("choice_position")).lower()
    chosen = _clean(row.get("chosen_asset")).lower()
    if pos in NO_CLEAR_VALUES or chosen in NO_CLEAR_VALUES or not chosen:
        return "no_clear_choice"
    if pos == "top":
        return "top"
    if pos == "bottom":
        return "bottom"
    return "other"


def median(values: Iterable[Optional[float]]) -> Optional[float]:
    cleaned = [float(v) for v in values if v is not None and math.isfinite(float(v))]
    return None if not cleaned else statistics.median(cleaned)


def round_or_none(value: Optional[float], digits: int = 1):
    return None if value is None else round(value, digits)


def analyze(rows: List[dict], excluded_participants: set[str]) -> dict:
    excluded_rows = [r for r in rows if is_excluded(r, excluded_participants)]
    included = [r for r in rows if not is_excluded(r, excluded_participants)]

    participant_rows: Dict[str, List[dict]] = defaultdict(list)
    for row in included:
        participant_rows[_clean(row["participant_id"])].append(row)

    participant_summary = []
    complete_count = 0
    for participant_id, prows in participant_rows.items():
        pair_ids = {_clean(r["candidate_id"]) for r in prows}
        complete = EXPECTED_PAIRS.issubset(pair_ids)
        complete_count += int(complete)
        participant_summary.append({
            "participant_id": participant_id,
            "protocol_versions": sorted({_clean(r["protocol_version"]) for r in prows}),
            "source_files": sorted({_clean(r.get("_source_file")) or "in_memory" for r in prows}),
            "row_count": len(prows),
            "unique_pair_count": len(pair_ids),
            "complete_6_of_6": complete,
        })

    by_pair: Dict[str, List[dict]] = defaultdict(list)
    for row in included:
        by_pair[_clean(row["candidate_id"])].append(row)

    pair_summaries = []
    for candidate_id in sorted(by_pair):
        prows = by_pair[candidate_id]
        kinds = Counter(choice_kind(r) for r in prows)
        assets = Counter(
            _clean(r["chosen_asset"])
            for r in prows
            if choice_kind(r) in {"top", "bottom"} and _clean(r["chosen_asset"])
        )
        hard = sum(_int(r.get("hard_to_identify")) == 1 for r in prows)
        pair_summaries.append({
            "candidate_id": candidate_id,
            "n_rows": len(prows),
            "n_participants": len({_clean(r["participant_id"]) for r in prows}),
            "top_choices": kinds["top"],
            "bottom_choices": kinds["bottom"],
            "no_clear_choice": kinds["no_clear_choice"],
            "other_choice_state": kinds["other"],
            "hard_to_identify_n": hard,
            "hard_to_identify_rate": round(hard / len(prows), 4) if prows else None,
            "free_text_n": sum(bool(_clean(r.get("free_text"))) for r in prows),
            "median_latency_ms": round_or_none(median(_num(r.get("latency_ms")) for r in prows), 1),
            "median_intensity": round_or_none(median(_num(r.get("intensity")) for r in prows), 2),
            "chosen_asset_counts": dict(sorted(assets.items())),
        })

    return {
        "analysis_contract": "wave1-descriptive-v0.1",
        "method_boundary": {
            "signal_mapping_status": "NONE",
            "automatic_family_verdict": False,
            "notes": [
                "Descriptive only: selected assets have no inferred CS/CR polarity.",
                "Latency and intensity are described but never interpreted psychologically.",
                "KEEP/REVISE/REJECT and supported/cross-load/insufficient/NONE require locked human coding / validation rules.",
                "Participant IDs across protocol versions are not assumed to represent different or identical humans.",
            ],
        },
        "counts": {
            "raw_rows": len(rows),
            "excluded_rows": len(excluded_rows),
            "included_rows": len(included),
            "participant_ids": len(participant_rows),
            "complete_6_of_6_participant_ids": complete_count,
            "incomplete_participant_ids": len(participant_rows) - complete_count,
        },
        "protocol_counts": dict(sorted(Counter(_clean(r["protocol_version"]) for r in included).items())),
        "language_counts": dict(sorted(Counter(_clean(r.get("language")) or "unknown" for r in included).items())),
        "source_file_counts": dict(sorted(Counter(_clean(r.get("_source_file")) or "in_memory" for r in included).items())),
        "pair_summary": pair_summaries,
        "participant_summary": sorted(participant_summary, key=lambda x: x["participant_id"]),
    }


def write_pair_csv(report: dict, path: Path) -> None:
    fields = [
        "candidate_id", "n_rows", "n_participants", "top_choices", "bottom_choices",
        "no_clear_choice", "other_choice_state", "hard_to_identify_n",
        "hard_to_identify_rate", "free_text_n", "median_latency_ms", "median_intensity",
        "chosen_asset_counts",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in report["pair_summary"]:
            out = dict(row)
            out["chosen_asset_counts"] = json.dumps(out["chosen_asset_counts"], ensure_ascii=False, sort_keys=True)
            writer.writerow(out)


def make_alias_map(candidate_ids: Sequence[str]) -> dict:
    aliases = [f"PAIR-{i:02d}" for i in range(1, len(candidate_ids) + 1)]
    shuffled = list(candidate_ids)
    secrets.SystemRandom().shuffle(shuffled)
    return {alias: candidate for alias, candidate in zip(aliases, shuffled)}


def write_blind_coding_package(rows: List[dict], excluded_participants: set[str], coding_path: Path, alias_key_path: Path) -> None:
    included = [r for r in rows if not is_excluded(r, excluded_participants) and _clean(r.get("free_text"))]
    candidate_ids = sorted({_clean(r["candidate_id"]) for r in included})
    alias_map = make_alias_map(candidate_ids)
    reverse = {candidate: alias for alias, candidate in alias_map.items()}

    alias_key_path.write_text(json.dumps({
        "alias_scheme": "wave1-neutral-alias-v0.1",
        "warning": "Do not show this file to blind coders before coding lock. Do not commit participant-study alias keys to the public repository.",
        "aliases": alias_map,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    fields = [
        "blind_row_id", "blind_pair_alias", "free_text", "reason_class",
        "confound_primary", "confound_secondary", "coder_id", "coder_notes",
    ]
    with coding_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for i, row in enumerate(included, 1):
            writer.writerow({
                "blind_row_id": f"R{i:04d}",
                "blind_pair_alias": reverse[_clean(row["candidate_id"])],
                "free_text": _clean(row["free_text"]),
                "reason_class": "", "confound_primary": "", "confound_secondary": "",
                "coder_id": "", "coder_notes": "",
            })


def summarize_coding(coding_path: Path, alias_key_path: Path) -> dict:
    key = json.loads(alias_key_path.read_text(encoding="utf-8"))
    aliases = key.get("aliases", {})
    per_pair = defaultdict(lambda: {"reason_class": Counter(), "confound_primary": Counter(), "coded_rows": 0})
    invalid = []

    with coding_path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            alias = _clean(row.get("blind_pair_alias"))
            candidate = aliases.get(alias)
            if not candidate:
                invalid.append({"blind_row_id": _clean(row.get("blind_row_id")), "problem": f"unknown alias {alias}"})
                continue
            reason = _clean(row.get("reason_class"))
            confound = _clean(row.get("confound_primary"))
            if reason and reason not in REASON_CLASSES:
                invalid.append({"blind_row_id": _clean(row.get("blind_row_id")), "problem": f"invalid reason_class {reason}"})
                continue
            if confound and confound not in CONFOUNDS:
                invalid.append({"blind_row_id": _clean(row.get("blind_row_id")), "problem": f"invalid confound_primary {confound}"})
                continue
            if reason:
                per_pair[candidate]["reason_class"][reason] += 1
                per_pair[candidate]["coded_rows"] += 1
            if confound:
                per_pair[candidate]["confound_primary"][confound] += 1

    return {
        "coding_contract": "wave1-blind-coding-summary-v0.1",
        "automatic_family_verdict": False,
        "pair_coding_summary": {
            candidate: {
                "coded_rows": data["coded_rows"],
                "reason_class_counts": dict(sorted(data["reason_class"].items())),
                "confound_primary_counts": dict(sorted(data["confound_primary"].items())),
            }
            for candidate, data in sorted(per_pair.items())
        },
        "invalid_rows": invalid,
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Descriptive Human Wave 1 CSV analysis; no psychological inference.")
    p.add_argument("csv", nargs="*", type=Path, help="Wave 1 CSV export(s), v0.3/v0.4 compatible")
    p.add_argument("--exclude-participant", action="append", default=[], help="Participant UUID to exclude; repeatable")
    p.add_argument("--json-out", type=Path)
    p.add_argument("--pair-csv-out", type=Path)
    p.add_argument("--blind-coding-template-out", type=Path)
    p.add_argument("--alias-key-out", type=Path)
    p.add_argument("--coding-results", type=Path, help="Completed blind coding CSV to summarize")
    p.add_argument("--alias-key", type=Path, help="Alias key matching --coding-results")
    p.add_argument("--coding-summary-out", type=Path)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if args.coding_results:
        if not args.alias_key:
            raise SystemExit("--coding-results requires --alias-key")
        summary = summarize_coding(args.coding_results, args.alias_key)
        if args.coding_summary_out:
            args.coding_summary_out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    if not args.csv:
        raise SystemExit("Provide at least one Wave 1 CSV export")
    if bool(args.blind_coding_template_out) != bool(args.alias_key_out):
        raise SystemExit("--blind-coding-template-out and --alias-key-out must be used together")

    rows = load_rows(args.csv)
    excluded = set(args.exclude_participant)
    report = analyze(rows, excluded)
    if args.json_out:
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.pair_csv_out:
        write_pair_csv(report, args.pair_csv_out)
    if args.blind_coding_template_out:
        write_blind_coding_package(rows, excluded, args.blind_coding_template_out, args.alias_key_out)

    print(json.dumps({
        "analysis_contract": report["analysis_contract"],
        "counts": report["counts"],
        "protocol_counts": report["protocol_counts"],
        "pair_summary": report["pair_summary"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
