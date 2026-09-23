import time
import ts3

HOST = "46.38.138.68"
PORT = 7283
USER = "jts3"
PASS = "ekBgRh5LZtmV"

print("Starting TeamSpeak 3 Bot Test...", flush=True)

try:
    print(f"Connecting to {HOST}:{PORT}...", flush=True)
    
    # ایجاد اتصال استاندارد به سرورکوئری
    ts3conn = ts3.query.TS3Connection(HOST, PORT)
    
    print("Connected! Attempting login...", flush=True)
    ts3conn.login(client_login_name=USER, client_login_password=PASS)
    print("Login successful! Bot is authenticated.", flush=True)
    
    ts3conn.use(sid=1)
    resp = ts3conn.hostinfo()
    server_name = resp[0].get("virtualserver_name", "نامشخص")
    print(f"Successfully connected to Virtual Server: {server_name}", flush=True)
    
    # بستن امن اتصال در پایان تست
    ts3conn.close()

except Exception as e:
    print(f"Connection failed with error: {e}", flush=True)

# نگه داشتن کانتینر برای بررسی لاگ‌ها
while True:
    time.sleep(60)
