"""
Seed script — populates demo_data/ with realistic mock records.

Usage:
    cd backend
    python scripts/seed_data.py

Generates:
  demo_data/citizen_reports/   — 25 SMS-style JSON messages (Hindi/English)
  demo_data/social_posts/      — 20 tweet-like JSON messages
  demo_data/satellite/         — 5 Sentinel-2 flood GeoJSON polygons

TODO (Phase 1): implement full generators.
"""
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

BASE = Path(__file__).parent.parent.parent / "demo_data"


def _write(path: Path, data: list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ wrote {len(data)} records → {path}")


def seed_citizen_reports() -> None:
    """TODO (Phase 1): generate realistic Hindi/English SMS reports."""
    records = [
        {
            "id": f"sms_{i:03d}",
            "source": "sms",
            "text": f"[PLACEHOLDER] Citizen report {i} — implement in Phase 1",
            "lat": 28.6139 + i * 0.001,
            "lon": 77.2090 + i * 0.001,
            "timestamp": (datetime.now(UTC) - timedelta(minutes=i * 3)).isoformat(),
        }
        for i in range(1, 26)
    ]
    _write(BASE / "citizen_reports" / "mock_reports.json", records)


def seed_social_posts() -> None:
    """TODO (Phase 1): generate realistic tweet-style posts."""
    records = [
        {
            "id": f"tweet_{i:03d}",
            "source": "tweet",
            "text": f"[PLACEHOLDER] Social post {i} #Flood #Delhi — implement in Phase 1",
            "timestamp": (datetime.now(UTC) - timedelta(minutes=i * 5)).isoformat(),
        }
        for i in range(1, 21)
    ]
    _write(BASE / "social_posts" / "mock_tweets.json", records)


def seed_satellite_polygons() -> None:
    """TODO (Phase 1): generate Sentinel-2 GeoJSON flood polygons."""
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [77.20 + i * 0.02, 28.60],
                    [77.22 + i * 0.02, 28.60],
                    [77.22 + i * 0.02, 28.62],
                    [77.20 + i * 0.02, 28.62],
                    [77.20 + i * 0.02, 28.60],
                ]],
            },
            "properties": {
                "id": f"sentinel_{i:03d}",
                "flood_depth_m": round(0.5 + i * 0.3, 1),
                "timestamp": (datetime.now(UTC) - timedelta(hours=i)).isoformat(),
                "note": "PLACEHOLDER — implement in Phase 1",
            },
        }
        for i in range(1, 6)
    ]
    geojson = {"type": "FeatureCollection", "features": features}
    _write(BASE / "satellite" / "flood_polygons.geojson", [geojson])


if __name__ == "__main__":
    print("🌱 Seeding demo_data/ ...")
    seed_citizen_reports()
    seed_social_posts()
    seed_satellite_polygons()
    print("Done. Run Phase 1 to replace placeholders with realistic data.")
