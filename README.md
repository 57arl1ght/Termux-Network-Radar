# 📡 Termux Network Radar (Telegram C2 Scanner)

A lightweight, Telegram-controlled network scanner designed to run on Termux (Android) or any Linux environment. This tool acts as a portable Command and Control (C2) agent, allowing you to remotely discover network devices and perform rapid port scanning via a Telegram bot interface.

## ✨ Features
* **Remote Execution:** Trigger scans from anywhere in the world using Telegram.
* **Network Discovery:** Uses Nmap under the hood to find all active hosts in the target subnet.
* **Port Scanning:** Automatically checks discovered devices for common open ports (SSH, HTTP, RDP, SMB, FTP, etc.) using Python Sockets.
* **Target Flexibility:** Scan the default local network or specify a custom CIDR range directly from the chat.
* **Portability:** Perfect for "Hardware Implant" scenarios using an old Android phone with Termux or a Raspberry Pi.

## 🛠 Prerequisites
Before running the bot, ensure you have the following installed on your system (Termux/Linux):
* Python 3
* Nmap
* `pyTelegramBotAPI` library

**Termux Installation Command:**
```bash
pkg update && pkg upgrade
pkg install python nmap
pip install pyTelegramBotAPI


git clone [https://github.com/YOUR_USERNAME/Termux-Network-Radar.git](https://github.com/YOUR_USERNAME/Termux-Network-Radar.git)
cd Termux-Network-Radar

python termux_scanner.py
Then, open your bot in Telegram and send commands:
/scan - Scans the default network (192.168.1.0/24).
/scan 10.0.0.0/24 - Scans a specific network range.

