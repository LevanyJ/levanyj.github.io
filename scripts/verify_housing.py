#!/usr/bin/env python3
"""Recompute the Day22 anonymised housing data aggregates from published CSV.

Usage: python scripts/verify_housing.py [data/housing_numeric_snapshot.csv]
No external packages and no network requests. Input is the anonymized numeric export
of an Excel snapshot from the Day22 classroom bundle (not live listings).
"""
import csv, statistics, pathlib, json, collections, sys, hashlib
DEFAULT = pathlib.Path(__file__).resolve().parents[1] / 'data' / 'housing_numeric_snapshot.csv'
p = pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT
with p.open(encoding='utf-8-sig', newline='') as f:
    rows=list(csv.DictReader(f))
assert rows and all(float(r['area_sqm'])>0 and float(r['price_wan'])>0 for r in rows)
nums=lambda k:[float(r[k]) for r in rows]
result={
 'count':len(rows),
 'median_price_wan':round(statistics.median(nums('price_wan')),2),
 'median_area_sqm':round(statistics.median(nums('area_sqm')),2),
 'median_unit_yuan_sqm':round(statistics.median(nums('unit_yuan_sqm')),2),
 'floor_distribution':dict(sorted(collections.Counter(r['floor'] for r in rows).items())),
 'rooms_distribution':dict(sorted(collections.Counter(int(r['rooms']) for r in rows).items())),
 'anonymous_csv_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'note':'Historical Chengdu classroom listing snapshot; not current prices or transactions.'
}
print(json.dumps(result,ensure_ascii=False,indent=2))
