import json

def load_json_data(filepath):
    """Load JSON data from file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_web_data(web_data):
    """Extract province and city information from web format"""
    provinces = {}
    cities = {}
    
    for province in web_data:
        province_code = province['code']
        province_name = province['text']
        provinces[province_code] = province_name
        
        # Extract cities
        if 'children' in province and province['children']:
            for city in province['children']:
                city_code = city['code']
                city_name = city['text']
                cities[city_code] = {
                    'name': city_name,
                    'province_code': province_code,
                    'province_name': province_name
                }
    
    return provinces, cities

def extract_mos_data(mos_data):
    """Extract province and city information from mos format"""
    provinces = {}
    cities = {}
    
    for province in mos_data:
        province_code = province['code']
        province_name = province['name']
        provinces[province_code] = province_name
        
        # Extract cities
        if 'cityList' in province and province['cityList']:
            for city in province['cityList']:
                city_code = city['code']
                city_name = city['name']
                cities[city_code] = {
                    'name': city_name,
                    'province_code': province_code,
                    'province_name': province_name
                }
    
    return provinces, cities

def compare_data(web_provinces, web_cities, mos_provinces, mos_cities):
    """Compare data between web and mos formats"""
    print("=== Province Comparison ===")
    # Check for provinces in web but not in mos
    only_in_web_provinces = set(web_provinces.keys()) - set(mos_provinces.keys())
    only_in_mos_provinces = set(mos_provinces.keys()) - set(web_provinces.keys())
    
    if only_in_web_provinces:
        print(f"Provinces in Web but not in MOS: {only_in_web_provinces}")
    if only_in_mos_provinces:
        print(f"Provinces in MOS but not in Web: {only_in_mos_provinces}")
    
    # Check for matching provinces
    common_provinces = set(web_provinces.keys()) & set(mos_provinces.keys())
    print(f"Common provinces: {len(common_provinces)}")
    
    print("\n=== City Comparison ===")
    # Check for cities in web but not in mos
    only_in_web_cities = set(web_cities.keys()) - set(mos_cities.keys())
    only_in_mos_cities = set(mos_cities.keys()) - set(web_cities.keys())
    
    if only_in_web_cities:
        print(f"Cities in Web but not in MOS: {len(only_in_web_cities)}")
        for code in list(only_in_web_cities)[:10]:  # Show first 10
            city = web_cities[code]
            print(f"  {code}: {city['name']} ({city['province_name']})")
        if len(only_in_web_cities) > 10:
            print(f"  ... and {len(only_in_web_cities)-10} more")
            
    if only_in_mos_cities:
        print(f"Cities in MOS but not in Web: {len(only_in_mos_cities)}")
        for code in list(only_in_mos_cities)[:10]:  # Show first 10
            city = mos_cities[code]
            print(f"  {code}: {city['name']} ({city['province_name']})")
        if len(only_in_mos_cities) > 10:
            print(f"  ... and {len(only_in_mos_cities)-10} more")
    
    # Check for matching cities
    common_cities = set(web_cities.keys()) & set(mos_cities.keys())
    print(f"\nCommon cities: {len(common_cities)}")
    
    # Check for name differences in common cities
    name_differences = []
    for code in common_cities:
        web_city_name = web_cities[code]['name']
        mos_city_name = mos_cities[code]['name']
        if web_city_name != mos_city_name:
            name_differences.append({
                'code': code,
                'web_name': web_city_name,
                'mos_name': mos_city_name
            })
    
    if name_differences:
        print(f"\n=== Name Differences ({len(name_differences)}) ===")
        for diff in name_differences[:10]:  # Show first 10
            print(f"City {diff['code']}: Web='{diff['web_name']}' vs MOS='{diff['mos_name']}'")
        if len(name_differences) > 10:
            print(f"  ... and {len(name_differences)-10} more")

def main():
    # File paths
    web_file_path = r"C:\Users\LVLE\Desktop\dealerCompare\web_province.json"
    mos_file_path = r"C:\Users\LVLE\Desktop\dealerCompare\mos.json"
    
    try:
        # Load data from files
        web_data = load_json_data(web_file_path)
        mos_data = load_json_data(mos_file_path)
        
        # Extract information
        web_provinces, web_cities = extract_web_data(web_data)
        mos_provinces, mos_cities = extract_mos_data(mos_data)
        
        # Compare data
        compare_data(web_provinces, web_cities, mos_provinces, mos_cities)
        
        # Summary statistics
        print("\n=== Summary ===")
        print(f"Web format - Provinces: {len(web_provinces)}, Cities: {len(web_cities)}")
        print(f"MOS format - Provinces: {len(mos_provinces)}, Cities: {len(mos_cities)}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()