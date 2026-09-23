import time
import ts3

HOST = "46.38.138.68"
PORT = 7283
USER = "jts3"
PASS = "ekBgRh5LZtmV"

print("Starting TeamSpeak 3 Bot Test...", flush=True)

try:
    print(f"Connecting to {HOST}:{PORT}...", flush=True)
    # ایجاد اتصال با در نظر گرفتن تایم‌اوت
    with ts3.query.TS3Connection(HOST, PORT, timeout=10) as ts3conn:
        print("Connected! Attempting login...", flush=True)
        ts3conn.login(client_login_name=USER, client_login_password=PASS)
        print("Login successful! Bot is authenticated.", flush=True)
        
        ts3conn.use(sid=1)
        resp = ts3conn.hostinfo()
        server_name = resp[0].get("virtualserver_name", "نامشخص")
        print(f"Successfully connected to Virtual Server: {server_name}", flush=True)

except Exception as e:
    print(f"Connection failed with error: {e}", flush=True)

# نگه داشتن کانتینر برای بررسی لاگ‌ها
while True:
    time.sleep(60)
