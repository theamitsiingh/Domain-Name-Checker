import requests
import itertools
import json

def generate_domain_names(keywords):
    prefixes = ["get", "best", "top", "my", "the", "pro"]
    suffixes = ["hub", "online", "site", "world", "expert"]
    extensions = [".com", ".net", ".org", ".io", ".co", ".tech", ".store", ".xyz", ".ai"]
    
    domain_names = [keyword + ext for keyword in keywords for ext in extensions]
    domain_names += [prefix + keyword + ext for prefix, keyword, ext in itertools.product(prefixes, keywords, extensions)]
    domain_names += [keyword + suffix + ext for keyword, suffix, ext in itertools.product(keywords, suffixes, extensions)]
    return domain_names

def check_domain_availability(domain, api_key, api_secret):
    url = f"https://api.godaddy.com/v1/domains/available"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json={"domain": domain}, headers=headers)
    if response.status_code == 200:
        return response.json().get("available", False)
    return False

def get_domain_price(domain, api_key, api_secret):
    url = f"https://api.godaddy.com/v1/domains/pricing/{domain}"
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("price", "Unknown")
    return "Unknown"

def whois_lookup(domain):
    url = f"https://api.whoislookupapi.com/v1/whois?domain={domain}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return "Whois lookup failed."

def main():
    keywords = input("Enter your area of interest (comma separated keywords): ").strip().lower().split(",")
    keywords = [keyword.replace(" ", "") for keyword in keywords]
    api_key = "YOUR_GODADDY_API_KEY"  # Replace with your actual API key
    api_secret = "YOUR_GODADDY_API_SECRET"  # Replace with your actual API secret
    
    domain_suggestions = generate_domain_names(keywords)
    
    print("Checking domain availability and prices...")
    available_domains = {}
    for domain in domain_suggestions:
        if check_domain_availability(domain, api_key, api_secret):
            price = get_domain_price(domain, api_key, api_secret)
            available_domains[domain] = price
    
    if available_domains:
        print("Available domains:")
        for domain, price in available_domains.items():
            print(f"{domain} - Price: {price}")
    else:
        print("No available domains found. Try a different keyword.")
    
    save_option = input("Would you like to save the available domains? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open("available_domains.json", "w") as file:
            json.dump(available_domains, file, indent=4)
        print("Available domains saved to available_domains.json")
    
    whois_option = input("Would you like to perform a Whois lookup on a taken domain? (yes/no): ").strip().lower()
    if whois_option == "yes":
        domain_to_lookup = input("Enter the domain you want to lookup: ").strip()
        print(whois_lookup(domain_to_lookup))

if __name__ == "__main__":
    main()