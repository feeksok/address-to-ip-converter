# address-to-ip-converter

This repository has been turned into a safer, privacy-conscious geolocation utility.

Purpose:
- Convert a public place, postcode area, city, or region into approximate coordinates.
- Return latitude, longitude, and altitude when available.
- Avoid exact private home locations and avoid IP assignment for residences.

Important:
- This tool is for broad public-location geocoding only.
- It does not provide a precise private residential IP or exact home address.
- It should not be used for stalking, tracking, or unlawful monitoring.

Quick start:

```bash
pip install -r requirements.txt
python safe_geolocation.py "BT47 6SQ"
```

Example output:

```json
{
  "input": "BT47 6SQ",
  "latitude": 54.344,
  "longitude": -7.629,
  "altitude_meters": 42.7,
  "place": "Strabane, County Tyrone, Northern Ireland",
  "status": "ok",
  "privacy_notice": "Area-level and public-location only. Not for exact private home locations."
}
```

This is intentionally safer than any residential-IP lookup and is suitable for public area/location lookups only.
