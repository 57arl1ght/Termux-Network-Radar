import telebot
import subprocess
import re
import socket


BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE" 

bot = telebot.TeleBot(BOT_TOKEN)

def scan_ports(ip):
    open_ports = []
    target_ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 
        80: "HTTP", 443: "HTTPS", 445: "SMB", 
        3389: "RDP", 5555: "ADB", 8080: "Alt HTTP"
    }
    
    for port, service in target_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        if sock.connect_ex((ip, port)) == 0:
            open_ports.append(f"{port} [{service}]")
        sock.close()
    return open_ports

def scan_network(ip_range):
    result = subprocess.run(['nmap', '-sn', ip_range], capture_output=True, text=True)
    devices = {}
    for line in result.stdout.split('\n'):
        if "Nmap scan report for" in line:
            ip_match = re.search(r'([0-9]{1,3}\.){3}[0-9]{1,3}', line)
            if ip_match:
                ip = ip_match.group(0)
                devices[ip] = {'name': "Unknown device"}
    return devices

@bot.message_handler(commands=['start', 'scan'])
def handle_scan(message):
    
    args = message.text.split()
    target_network = args[1] if len(args) > 1 else "192.168.1.0/24"
    
    bot.reply_to(message, f"📡 Starting network scan on {target_network}. Please wait...")
    
    devices = scan_network(target_network)
    
    if not devices:
        bot.send_message(message.chat.id, "🤷‍♂️ No devices found.")
        return
        
    for ip, info in devices.items():
        ports = scan_ports(ip)
        if ports:
            ports_text = "\n🔓 Open ports:\n- " + "\n- ".join(ports)
        else:
            ports_text = "\n🔒 All standard ports are closed"
        
        msg = f"🖥 IP: {ip}\n🏷 Name: {info['name']}{ports_text}"
        bot.send_message(message.chat.id, msg)
        
    bot.send_message(message.chat.id, "✅ Scan completed successfully!")

if __name__ == "__main__":
    print("🤖 Bot-agent is running! Waiting for commands...")
    bot.polling(none_stop=True)