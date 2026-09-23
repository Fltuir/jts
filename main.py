import ts3

# اطلاعات اتصال به سرور تیم‌اسپیک شما
HOST = "46.38.138.68"
PORT = 7283  # پورت کوئری شما
USER = "jts3"
PASS = "ekBgRh5LZtmV"

print(f"در حال تلاش برای اتصال به {HOST}:{PORT} با نام کاربری {USER}...")

try:
    # ایجاد اتصال به سرورکوئری
    with ts3.query.TS3Connection(HOST, PORT) as ts3conn:
        # لاگین با اطلاعات کوئری
        ts3conn.login(client_login_name=USER, client_login_password=PASS)
        print("اتصال موفقیت‌آمیز بود! ربات به راحتی توانست به سرور لاگین کند.")
        
        # انتخاب مجازی سرور (آیدی 1 یا پیش‌فرض)
        ts3conn.use(sid=1)
        
        # دریافت اطلاعات پایه سرور برای تست
        resp = ts3conn.hostinfo()
        server_name = resp[0].get("virtualserver_name", "نامشخص")
        print(f"نام سرور تیم‌اسپیک شما: {server_name}")

except Exception as e:
    print(f"خطا در اتصال به سرورکوئری: {e}")
