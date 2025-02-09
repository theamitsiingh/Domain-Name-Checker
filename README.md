# Domain Name Checker

## 🚀 Overview
The **Domain Name Checker** is a powerful Python script that helps users generate, check, and purchase domain names based on their area of interest. It suggests domain names, verifies their availability, fetches pricing details, and even provides WHOIS lookup for unavailable domains.

## 🎯 Features
- **Smart Domain Name Generation**: Generates domain name suggestions using keywords, prefixes, and suffixes.
- **Multiple Domain Extensions**: Supports `.com`, `.net`, `.org`, `.io`, `.co`, `.tech`, `.store`, `.xyz`, and `.ai`.
- **Availability Check**: Verifies domain name availability using the GoDaddy API.
- **Price Fetching**: Retrieves the price of available domains.
- **WHOIS Lookup**: Provides WHOIS information for already registered domains.
- **Save Available Domains**: Stores available domain names in a JSON file for future reference.

## 🛠️ Setup & Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/domain-name-checker.git
   cd domain-name-checker
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Obtain API keys from GoDaddy:
   - Sign up for a GoDaddy Developer account: [GoDaddy API](https://developer.godaddy.com/)
   - Get your API key and secret.
4. Update the script with your API credentials:
   ```python
   api_key = "YOUR_GODADDY_API_KEY"
   api_secret = "YOUR_GODADDY_API_SECRET"
   ```

## 🔥 How to Use
1. Run the script:
   ```bash
   python domain_name_checker.py
   ```
2. Enter your area of interest (comma-separated keywords).
3. The script will:
   - Generate domain name suggestions.
   - Check their availability.
   - Fetch domain prices.
   - Offer an option to save results.
   - Provide WHOIS lookup for unavailable domains.
4. Follow the on-screen prompts to explore and save domain options.

## 📝 Example Usage
```
Enter your area of interest (comma separated keywords): tech, innovation
Checking domain availability and prices...
Available domains:
techhub.com - Price: $12.99
bestinnovation.io - Price: $9.99
...
Would you like to save the available domains? (yes/no): yes
Available domains saved to available_domains.json
Would you like to perform a Whois lookup on a taken domain? (yes/no): no
```

## 📌 Notes
- Ensure you have a stable internet connection.
- If you encounter API rate limits, consider upgrading your GoDaddy API plan.
- Modify the script to include additional features if needed!

## 🤝 Contributions
Feel free to fork this repository and submit a pull request if you have improvements or additional features to add!

## 📜 License
This project is licensed under the MIT License.

---
✨ Happy domain hunting! 🚀

