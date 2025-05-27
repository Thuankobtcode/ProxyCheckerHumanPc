# 🇻🇳 ProxyCheckerVN — Fast Proxy Checker by Luckystop

![Python](https://img.shields.io/badge/Python-3.6%2B-yellow.svg)
![Multi-Threaded](https://img.shields.io/badge/Threads-Up%20to%2050-green.svg)
![Made-in-Vietnam](https://img.shields.io/badge/Made%20in-Vietnam-red.svg)

> A fast and smart proxy checker that supports HTTP, SOCKS4, SOCKS5, and filters proxies by country (Vietnam by default 🇻🇳).  
> Developed by: **@Luckystopdz** | Telegram: [@Humanpv](https://t.me/Humanpv)

---

## ✨ Features

- ✅ Check if proxies are alive (LIVE/DIE)
- 🔍 Auto detect and classify: HTTP, SOCKS4, SOCKS5
- 🌍 Country-based filter (e.g., Vietnam 🇻🇳)
- ⚡ Multi-threaded for maximum performance
- 🎨 Colored console output
- 💾 Saves results to categorized output files

---

## 📦 Installation

```bash
pip install requests colorama
⚙️ Usage
bash
Copy
Edit
python proxycheckervn.py --file proxies.txt --t 50
--file: Input file containing proxy list (ip:port format, one per line)

--t: Number of threads (default: 50)

📁 Output Files
good_proxy_http.txt — Working HTTP proxies

good_proxy_socks4.txt — Working SOCKS4 proxies

good_proxy_socks5.txt — Working SOCKS5 proxies

VietNam_Proxies.txt — Proxies from Vietnam

💡 Tip: You can modify the country filter to collect proxies from other countries by changing the country code in the script (e.g., "VN" → "US", "DE", "FR", etc.)

📸 Example Output
text
Copy
Edit
[15:30:12] [LIVE] - 45.77.123.12:8080 | United States | 145ms
[15:30:13] [DIE]  - 123.45.67.89:1080
[15:30:14] [LIVE] - 113.22.11.88:8080 | Vietnam | 122ms
💬 Contact
Telegram Channel: @Humanpv

Developer: @Luckystopdz

yaml
Copy
Edit
