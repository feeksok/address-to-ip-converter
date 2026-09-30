"""
Direct test of postcode: BT47 6EW
"""

from converter import AddressToIPConverter
import json

converter = AddressToIPConverter()

postcode = "BT47 6EW"
print(f"Converting postcode: {postcode}\n")

result = converter.convert(postcode)

print("="*70)
print("RESULT:")
print("="*70)
print(json.dumps(result, indent=2))
