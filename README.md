<p align="center">
  <img src="https://raw.githubusercontent.com/jowner526202-hash/Official-reporting-forms/main/security-banner.png" width="100%">
</p>

<p align="center">
<img src="https://img.shields.io/github/stars/jowner526202-hash/IP-Striker-Ahmed?style=for-the-badge&color=blue" alt="Stars">
<img src="https://img.shields.io/github/forks/jowner526202-hash/IP-Striker-Ahmed?style=for-the-badge&color=green" alt="Forks">
</p>

---


# 🛡️ AHMED-STRIKER-V2 
### Intelligence IP Tracking & OSINT System
![Version](https://img.shields.io/badge/Version-2.0.0-cyan) ![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Kali%20Linux-green)

---

## 📖 وصف الأداة (About)
أداة **AHMED-STRIKER** هي نظام استخباراتي مصغر بلغة بايثون، مخصص لفحص وتحليل عناوين الـ IP. تم تطويرها لتوفير دقة عالية في تتبع المواقع الجغرافية وكشف محاولات التخفي الرقمي، مما يسهل على المحققين الجنائيين الرقميين والمطورين جمع المعلومات اللازمة.

### 🛡️ المميزات التقنية:
* **دقة البيانات:** تجلب المدينة، الدولة، الرمز البريدي، ومزود الخدمة (ISP).
* **كشف التزييف:** ميزة احترافية لكشف ما إذا كان المستهدف يستخدم **VPN** أو **Proxy**.
* **الرصد الجغرافي:** توليد رابط مباشر لخرائط جوجل (Google Maps) مع إحداثيات دقيقة.
* **التوثيق:** حفظ كافة عمليات الفحص في ملف `ahmed_results.txt` تلقائياً.
* **الذكاء البرمجي:** الكود يقوم بتثبيت المكتبات الناقصة ذاتياً عند التشغيل.

---

## 🚀 تعليمات التثبيت والتشغيل (Installation)

### 📱 أولاً: مستخدمي Termux (Android)
انسخ الأوامر التالية والصقها في التيرمكس:
```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clon https://github.com/ahmadshh208/IP-Striker-Ahmed.git
cd IP-Striker-Ahmed
python IP-Striker-Ahmed


ثانياً: مستخدمي Kali Linux / Ubuntu
افتح الطرفية (Terminal) وقم بتنفيذ ما يلي:
sudo apt update && sudo apt install python3-pip git -y
git clone https://github.com/ahmadshh208/IP-Striker-Ahmed.git
cd IP-Striker-Ahmed
pip3 install requests
python3 IP-Striker-Ahmed
