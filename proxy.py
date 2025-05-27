import argparse
import requests
import threading
import time
from queue import Queue
import os
from colorama import init, Fore, Style

init(autoreset=True)

CHECK_URL = "http://ip-api.com/json"
TIMEOUT = 5
print_lock = threading.Lock()
q = Queue()

good_http = []
good_socks4 = []
good_socks5 = []
vietnam_proxies = []


def check_proxy(proxy, thread_id):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        start_time = time.time()
        response = requests.get(CHECK_URL, proxies=proxies, timeout=TIMEOUT)
        delay = round((time.time() - start_time) * 1000)

        if response.status_code == 200:
            data = response.json()
            country = data.get("country", "Unknown")
            if "VN" in data.get("countryCode", ""):
                vietnam_proxies.append(proxy)

            with print_lock:
                print(Fore.GREEN + f"[{time.strftime('%H:%M:%S')}] [LIVE] - {proxy} | {country} | {delay}ms")

            # Xác định loại proxy theo cổng
            if proxy.endswith(":1080") or proxy.endswith(":1081"):
                good_socks5.append(proxy)
            elif proxy.endswith(":1082") or proxy.endswith(":1083"):
                good_socks4.append(proxy)
            else:
                good_http.append(proxy)
        else:
            with print_lock:
                print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] [DIE] - {proxy}")
    except Exception:
        with print_lock:
            print(Fore.RED + f"[{time.strftime('%H:%M:%S')}] [DIE] - {proxy}")


def worker(thread_id):
    while not q.empty():
        proxy = q.get()
        check_proxy(proxy, thread_id)
        q.task_done()


def load_proxies(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def save_proxies(filename, proxies):
    with open(filename, "w") as f:
        for p in proxies:
            f.write(p + "\n")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print (r"""
 _   _ _   _ __  __    _    _   _   ____   ____  
| | | | | | |  \/  |  / \  | \ | | |  _ \ / ___| 
| |_| | | | | |\/| | / _ \ |  \| | | |_) | |     
|  _  | |_| | |  | |/ ___ \| |\  | |  __/| |___  
|_| |_|\___/|_|  |_/_/   \_\_| \_| |_|    \____| 
           
   Channels : https://t.me/humanpcc
    devloper : @thuannodejs       
           """)
    parser = argparse.ArgumentParser(description="HTTP/HTTPS Proxy Checker")
    parser.add_argument("--file", "-f", required=True, help="Input proxy file")
    parser.add_argument("--t", type=int, default=50, help="Number of threads (default: 50)")

    args = parser.parse_args()

    proxy_list = load_proxies(args.file)
    for proxy in proxy_list:
        q.put(proxy)

    threads = []
    for i in range(args.t):
        t = threading.Thread(target=worker, args=(i,))
        t.daemon = True
        threads.append(t)
        t.start()

    q.join()

    # Thống kê và lưu
    print(f"\n{Fore.GREEN}✅ Total Good HTTP: {len(good_http)}")
    print(f"{Fore.GREEN}✅ Total Good SOCKS4: {len(good_socks4)}")
    print(f"{Fore.GREEN}✅ Total Good SOCKS5: {len(good_socks5)}")
    print(f"{Fore.GREEN}🇻🇳 Total Vietnam Proxies: {len(vietnam_proxies)}")

    save_proxies("good_proxy_http.txt", good_http)
    save_proxies("good_proxy_socks4.txt", good_socks4)
    save_proxies("good_proxy_socks5.txt", good_socks5)
    save_proxies("VietNam_Proxies.txt", vietnam_proxies)

    print(f"{Fore.CYAN}📁 All results saved.")


if __name__ == "__main__":
    main()
