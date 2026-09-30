"""
Quick Test Script - Try the converter on your own address
Simply run this script and follow the prompts
"""

from converter import AddressToIPConverter
import json

def main():
    print("\n" + "="*70)
    print("🏠 ADDRESS TO IP CONVERTER - PERSONAL TEST")
    print("="*70)
    print("\nEnter your home address or postcode to convert it to an IP address.")
    print("Examples of valid inputs:")
    print("  • Full address: '123 Main Street, New York, NY 10001'")
    print("  • Postcode: '10001' or 'SW1A 1AA'")
    print("  • Mix: 'Brooklyn, NY 10001'")
    print("\n" + "-"*70)
    
    # Get user input
    user_input = input("\n📍 Enter your address or postcode: ").strip()
    
    if not user_input:
        print("❌ No input provided. Exiting.")
        return
    
    print(f"\n⏳ Processing: {user_input}")
    print("   (Finding coordinates and IP address...)\n")
    
    # Initialize converter
    converter = AddressToIPConverter()
    
    # Convert
    result = converter.convert(user_input)
    
    # Display results
    print("="*70)
    print("📊 RESULTS:")
    print("="*70)
    
    if result['success']:
        print(f"\n✅ SUCCESS!\n")
        print(f"📍 Location: {result['input']}")
        print(f"📡 IP Address: {result['ip']}")
        print(f"🗺️  Latitude: {result['coordinates']['latitude']:.6f}")
        print(f"🗺️  Longitude: {result['coordinates']['longitude']:.6f}")
        print(f"\n💡 You can use this IP for:")
        print(f"   • Geolocation verification")
        print(f"   • Mapping applications")
        print(f"   • Geographic analysis")
        print(f"   • Distance calculations")
    else:
        print(f"\n❌ CONVERSION FAILED\n")
        print(f"❗ Message: {result['message']}")
        print(f"\n💡 Tips to fix this:")
        print(f"   • Try a more complete address with city/country")
        print(f"   • Use a valid postcode for your country")
        print(f"   • Include country name for international addresses")
    
    print("\n" + "="*70)
    
    # Option to try again
    retry = input("\n🔄 Try another address? (yes/no): ").strip().lower()
    if retry in ['yes', 'y']:
        main()
    else:
        print("\n👋 Thanks for testing! Check your repository for more features.\n")


if __name__ == "__main__":
    main()
