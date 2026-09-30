"""
Example usage of the Address to IP Converter
Demonstrates various ways to use the converter
"""

from converter import AddressToIPConverter

def example_single_conversion():
    """Example: Convert a single address"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Single Address Conversion")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    address = "1600 Pennsylvania Avenue NW, Washington, DC"
    print(f"Converting: {address}")
    
    result = converter.convert(address)
    
    if result['success']:
        print(f"✓ Success!")
        print(f"  Coordinates: {result['coordinates']['latitude']}, {result['coordinates']['longitude']}")
        print(f"  IP Address: {result['ip']}")
    else:
        print(f"✗ Failed: {result['message']}")


def example_postcode_conversion():
    """Example: Convert a postcode"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Postcode Conversion")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    # UK postcode
    postcode = "SW1A 1AA"
    print(f"Converting UK Postcode: {postcode}")
    result = converter.convert(postcode)
    
    if result['success']:
        print(f"✓ Success!")
        print(f"  IP Address: {result['ip']}")
    else:
        print(f"✗ Failed: {result['message']}")


def example_international_address():
    """Example: Convert international addresses"""
    print("\n" + "="*60)
    print("EXAMPLE 3: International Addresses")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    addresses = [
        "Eiffel Tower, Paris, France",
        "Brandenburg Gate, Berlin, Germany",
        "Big Ben, London, UK",
    ]
    
    for address in addresses:
        print(f"\nConverting: {address}")
        result = converter.convert(address)
        
        if result['success']:
            print(f"  ✓ IP: {result['ip']}")
            print(f"    Coords: {result['coordinates']['latitude']:.4f}, {result['coordinates']['longitude']:.4f}")
        else:
            print(f"  ✗ {result['message']}")


def example_batch_conversion():
    """Example: Batch convert multiple addresses"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Batch Conversion")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    # List of company headquarters
    company_locations = [
        "1 Infinite Loop, Cupertino, CA",  # Apple
        "1600 Amphitheatre Parkway, Mountain View, CA",  # Google
        "410 Terry Avenue North, Seattle, WA",  # Amazon
    ]
    
    print(f"Converting {len(company_locations)} addresses...\n")
    results = converter.convert_batch(company_locations)
    
    for result in results:
        status = "✓" if result['success'] else "✗"
        print(f"{status} {result['input']}")
        if result['success']:
            print(f"   IP: {result['ip']}")
        else:
            print(f"   Error: {result['message']}")


def example_error_handling():
    """Example: Handling errors and edge cases"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Error Handling")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    # Invalid/unclear addresses
    test_cases = [
        "Invalid Address XYZ123",
        "123 Main St",  # Too generic
        "North Pole",  # Remote location
    ]
    
    for address in test_cases:
        print(f"\nTesting: {address}")
        result = converter.convert(address)
        
        print(f"  Success: {result['success']}")
        print(f"  Message: {result['message']}")
        if result['coordinates']:
            print(f"  Coordinates: {result['coordinates']}")


def example_use_result_data():
    """Example: Using the result data for further processing"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Processing Results")
    print("="*60)
    
    converter = AddressToIPConverter()
    
    address = "Statue of Liberty, New York, NY"
    result = converter.convert(address)
    
    if result['success']:
        print(f"Location: {result['input']}")
        print(f"IP Address: {result['ip']}")
        print(f"Latitude: {result['coordinates']['latitude']:.6f}")
        print(f"Longitude: {result['coordinates']['longitude']:.6f}")
        
        # Example: Calculate distance or perform other geolocation tasks
        lat = result['coordinates']['latitude']
        lon = result['coordinates']['longitude']
        print(f"\nYou can now use these coordinates for:")
        print(f"  • Plotting on a map")
        print(f"  • Calculating distances to other locations")
        print(f"  • Reverse IP lookups")
        print(f"  • Geographic analysis")


if __name__ == "__main__":
    print("\n" + "█"*60)
    print("ADDRESS TO IP CONVERTER - EXAMPLES")
    print("█"*60)
    
    # Run all examples
    example_single_conversion()
    example_postcode_conversion()
    example_international_address()
    example_batch_conversion()
    example_error_handling()
    example_use_result_data()
    
    print("\n" + "█"*60)
    print("Examples completed!")
    print("█"*60 + "\n")
