import socket
import time

HOST = "46.38.138.68"
PORT = 7283

print("Starting Network & Port Diagnostics...", flush=True)

try:
    print(f"Testing raw TCP connection to {HOST}:{PORT}...", flush=True)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)  # تایم‌اوت ۵ ثانیه
    result = s.connect_ex((HOST, PORT))
    s.close()
    
    if result == 0:
        print("Port 7283 is OPEN and reachable! Connection successful.", flush=True)
    else:
        print(f"Port 7283 is CLOSED or blocked. Error code: {result}", flush=True)

except Exception as e:
    print(f"Socket test failed with error: {e}", flush=True)

# نگه داشتن کانتینر برای بررسی لاگ
while True:
    time.sleep(60)
