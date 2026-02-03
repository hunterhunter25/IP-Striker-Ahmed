#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time, json

# محاولة استيراد مكتبة requests وتثبيتها تلقائياً إذا نقصت (مهم لـ Termux)
try:
    import requests
except ImportError:
    print("\n[*] Installing dependencies...")
    os.system("pip install requests")
    import requests

# مصفوفة الألوان المتوافقة مع Termux و Kali
G = '\033[92m' # أخضر
R = '\033[91m' # أحمر
C = '\033[96m' # سماوي
Y = '\033[93m' # أصفر
B = '\033[94m' # أزرق
W = '\033[97m' # أبيض
S = '\033[1m'  # عريض
X = '\033[0m'  # إعادة ضبط

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    # تشفير اسمك داخل البانر بشكل فني
    print(f"""{C}{S}
  █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗ 
 ██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗
 ███████║███████║██╔████╔██║█████╗  ██║  ██║
 ██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║
 ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝
 {Y}       [ AHMED CYBER INTELLIGENCE V2 ]
 {W}    ---------------------------------------
 {G}    [+] Developed by: {S}Ahmed Developer{X}{G}
 {G}    [+] System: {S}Termux / Kali Linux / Pro{X}{G}
 {G}    [+] Status: {S}Encrypted & Verified{X}
 {C}    ---------------------------------------{X}
    """)

def ip_tracker():
    banner()
    try:
        target = input(f"{C}[?]{W} أدخل الـ IP المستهدف (أو Enter لجهازك): {G}").strip()
        
        print(f"\n{Y}[*] جاري اختراق قاعدة بيانات الموقع...{X}")
        time.sleep(1)
        
        # استخدام API دقيق جداً يعطي معلومات متقدمة
        api_url = f"http://ip-api.com/json/{target}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query"
        response = requests.get(api_url)
        data = response.json()

        if data['status'] == 'success':
            print(f"\n{G}{S}[✅] تم جلب البيانات بنجاح لـ: {data['query']}{X}\n")
            
            info = {
                "الدولة": f"{data['country']} ({data['countryCode']})",
                "المدينة": data['city'],
                "المنطقة": data['regionName'],
                "الرمز البريدي": data['zip'],
                "إحداثيات": f"{data['lat']} , {data['lon']}",
                "مزود الخدمة": data['isp'],
                "المنظمة": data['org'],
                "اتصال جوال": "نعم" if data['mobile'] else "لا",
                "بروكسي/VPN": "⚠️ مكتشف (Proxy/VPN)" if data['proxy'] else "اتصال مباشر (آمن)",
                "استضافة/سيرفر": "نعم (Hosting)" if data['hosting'] else "جهاز مستخدم عدي",
            }

            for key, value in info.items():
                print(f"{C} {key:.<15}: {W}{value}{X}")
            
            # رابط الخريطة
            map_link = f"https://www.google.com/maps/place/{data['lat']}+{data['lon']}"
            print(f"\n{Y}[!] رابط الموقع الجغرافي:{X}\n{B}{map_link}{X}")
            
            # حفظ في ملف تلقائياً (تشفير المخرجات)
            with open("ahmed_results.txt", "a") as f:
                f.write(f"IP: {data['query']} | Date: {time.ctime()} | Location: {data['city']}\n")
            print(f"\n{G}[+] تم حفظ النتيجة في ahmed_results.txt{X}")

        else:
            print(f"\n{R}[❌] خطأ: {data['message']}{X}")

    except KeyboardInterrupt:
        print(f"\n{R}[!] تم إيقاف النظام من قبل أحمد.{X}")
        sys.exit()
    except Exception as e:
        print(f"\n{R}[❌] فشل الاتصال بالخادم الرئيسي.{X}")

if __name__ == "__main__":
    ip_tracker()
  
