import requests
import json

# 🔑 Your API Key
API_KEY = "FNjhvByIdP9MMhckAUbPo7Ocl1UUcYX5aDTmc8hn"

# 🔹 Function to lookup phone details
def lookup_number(phone_number, country_hint="IN"):
    url = "https://api.trestleiq.com/3.1/caller_id"
    
    params = {
        "phone": phone_number,
        "phone.country_hint": country_hint
    }
    
    headers = {
        "x-api-key": API_KEY,
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        # Agar response sahi nahi mila toh error dikhaye
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code} - {response.text}")
            return None
        
        data = response.json()
        
        # 🟢 Format & Print Response
        print("\n📞 Phone Lookup Result")
        print("="*50)
        print(f"Phone Number     : {data.get('phone_number')}")
        print(f"Valid            : {data.get('is_valid')}")
        print(f"Line Type        : {data.get('line_type')}")
        print(f"Carrier          : {data.get('carrier')}")
        print(f"Prepaid?         : {data.get('is_prepaid')}")
        print(f"Business Number? : {data.get('is_commercial')}")
        
        belongs_to = data.get("belongs_to")
        if belongs_to:
            print("\n👤 Owner Info")
            print(f"Name             : {belongs_to.get('name')}")
            print(f"Age Range        : {belongs_to.get('age_range')}")
            print(f"Type             : {belongs_to.get('type')}")
        
        addresses = data.get("current_addresses", [])
        if addresses:
            print("\n🏠 Address Info")
            for addr in addresses:
                city = addr.get("city", "")
                postal = addr.get("postal_code", "")
                country = addr.get("country", "")
                print(f"City: {city}, Postal: {postal}, Country: {country}")
        
        emails = data.get("emails", [])
        if emails:
            print("\n📧 Emails")
            for e in emails:
                print(f"- {e}")
        
        print("="*50)
    
    except Exception as e:
        print(f"⚠ Exception occurred: {str(e)}")

# 🔹 Example usage:
if __name__ == "__main__":
    number = input("Enter phone number (with country code, e.g. +919876543210): ")
    lookup_number(number, country_hint="IN")
