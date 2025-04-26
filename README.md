A Python tool to scrape JavaScript files from a given website, extract hidden endpoints, and check if they are alive.
Perfect for bug bounty hunting, penetration testing, and web security reconnaissance.

📸 Demo
bash
Copy
Edit
$ python endpoint_scraper.py
Enter the website URL: example.com

Found 5 JS files. Extracting endpoints...

Found 14 unique endpoints:

https://example.com/api/login [ALIVE]
https://example.com/admin/dashboard [ALIVE]
https://example.com/test/api [Status: 404]
...
�� Features
✅ Automatically adds https:// if missing

✅ Scrapes external JavaScript files from the page

✅ Extracts possible hidden endpoints using Regex

✅ Checks if extracted endpoints are alive

✅ Handles errors gracefully (timeouts, invalid URLs, etc.)

✅ Useful for Reconnaissance and Security Testing

📦 Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/js-endpoint-scraper.git
cd js-endpoint-scraper
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Run the script:

bash
Copy
Edit
python endpoint_scraper.py
Input the target website when prompted.

📋 Requirements
Python 3.x

requests

beautifulsoup4

You can install required modules manually:

bash
Copy
Edit
pip install requests beautifulsoup4
or use requirements.txt (recommended).

⚡ How It Works
Takes a target URL input.

Fetches the page HTML and finds all <script src=...> links.

Downloads each JavaScript file.

Extracts potential endpoints like /api/user, /admin/dashboard, etc.

Sends HTTP requests to each endpoint and checks if they are alive.

Prints the results.

🎯 Ideal For
Bug Bounty Hunting

Web App Pentesting

Reconnaissance

Finding Hidden/Deprecated APIs

✨ Future Improvements
Save results to a file.

Add multithreading for faster checking.

Colorize output (e.g., green for alive, red for dead).

Smarter endpoint extraction (handling URLs inside functions or variables).

🤝 Contributing
Pull requests are welcome!
Feel free to open issues or suggest new features.

📜 License
This project is licensed under the MIT License.

🌟 Give a Star!
If you like this project, please ⭐️ star this repo!
It helps a lot and motivates me to build more awesome tools.

🔗 Connect With Me
GitHub: yourusername

Twitter: @yourhandle

Medium: @yourmedium

🐍
Built with Python and 💙 for the Cybersecurity Community.

⚡ Tip:
You can save this as README.md inside your project folder, then push to GitHub!
Want me to also create a requirements.txt for you? 📄✨
(one line)
If yes, just say — make requirements.txt 🚀
