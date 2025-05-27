
# 🇻🇳 ProxyCheckerVN — Proxy Checker by Luckystop

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6%2B-yellow.svg)
![Made-in-Vietnam](https://img.shields.io/badge/Made%20in-Vietnam-red.svg)

> Công cụ kiểm tra proxy nhanh, hỗ trợ phân loại HTTP, SOCKS4, SOCKS5 và lọc IP Việt Nam 🇻🇳  
> By: @Luckystopdz | Telegram: [@Humanpv](https://t.me/Humanpv)

---

## ✨ Tính năng nổi bật

- ✅ Kiểm tra proxy hoạt động (LIVE/DIE)
- 🔍 Phân loại tự động: HTTP, SOCKS4, SOCKS5
- 🇻🇳 Lọc proxy có IP từ Việt Nam
- 🚀 Chạy đa luồng cực nhanh (multi-threaded)
- 🎨 Màu sắc hiển thị đẹp, dễ theo dõi
- 💾 Lưu kết quả ra file theo từng loại

---

## 📦 Cài đặt

```bash
pip install requests colorama
````

---

## ⚙️ Cách sử dụng

```bash
python proxycheckervn.py --file proxies.txt --t 50
```

* `--file`: Tên file chứa danh sách proxy (mỗi dòng 1 proxy dạng `ip:port`)
* `--t`: Số luồng (thread) kiểm tra song song (mặc định 50)

---

## 📁 Kết quả xuất ra

* `good_proxy_http.txt` — Các proxy HTTP hoạt động
* `good_proxy_socks4.txt` — Các proxy SOCKS4 hoạt động
* `good_proxy_socks5.txt` — Các proxy SOCKS5 hoạt động
* `VietNam_Proxies.txt` — Proxy có IP tại Việt Nam

---

## 📸 Giao diện CLI

```text
[15:30:12] [LIVE] - 45.77.123.12:8080 | United States | 145ms
[15:30:13] [DIE]  - 123.45.67.89:1080
[15:30:14] [LIVE] - 113.22.11.88:8080 | Vietnam | 122ms
```

---

## 📜 Giấy phép

Phát hành dưới giấy phép **Apache License 2.0**
Xem thêm tại: [LICENSE](https://www.apache.org/licenses/LICENSE-2.0)

---

## 💬 Liên hệ

* Telegram: [@Humanpv](https://t.me/Humanpv)
* Developer: [Luckystopdz](https://t.me/Luckystopdz)

---

```

---

📌 Gợi ý: bạn có thể đổi tên file script thành `proxycheckervn.py` để đồng nhất repo và file.

Bạn muốn mình xuất luôn file `README.md` để bạn tải không?
```
