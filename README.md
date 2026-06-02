# DGS Akıllı Veri Analiz Botu (Playwright & Docker)

Bu proje, DGS (Dikey Geçiş Sınavı) Matematik konularını ve çıkmış soru dağılımlarını web kazıma (web scraping) yöntemiyle dinamik olarak analiz eden ve yerel bir veri arşivi oluşturan akıllı bir otomasyon botudur. Proje, modern yazılım mimarilerine uygun olarak tamamen **Docker** ve **Docker Compose** altyapısı üzerinde konteynerize edilerek geliştirilmiştir.

## 🚀 Projenin Öne Çıkan Özellikleri

* **Dinamik Yıl Analizi:** Tablo başlıklarındaki yılları statik kodlamayla değil, güncel yılları tespit eden akıllı bir algoritmayla dinamik olarak eşleştirir.
* **En Güncel 8 Yıl Verisi:** Sitedeki veriler arasından en güncel 8 yıla ait soru dağılımlarını filtreler ve analiz eder.
* **Hata Yönetimi (Robust Code):** Sayfa gecikmeleri veya zaman aşımı (Timeout) durumlarına karşı `try-except` blokları ve Playwright'ın kararlı kütüphane mekanizmalarıyla korunmaktadır.
* **Veri Çıktısı (JSON):** Toplanan tüm verileri Türkçe karakterleri koruyarak yapılandırılmış `JSON` formatında kaydeder.
* **Görsel Kanıt (Screenshot):** Botun verileri doğru analiz ettiğini kanıtlamak amacıyla, ilgili HTML tablo elementinin anlık ekran görüntüsünü kırparak arşiv klasörüne bırakır.

---

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.11+
* **Otomasyon / Web Scraping:** Playwright (Synchronous API)
* **Konteynerizasyon:** Docker & Docker Compose
* **Taban İmaj:** `mcr.microsoft.com/playwright/python:v1.60.0-jammy`

---

## 📁 Proje Yapısı

```text
├── DGS_Veri_Arsivi/         # Bot çalıştıktan sonra otomatik oluşan klasör (Gitignore'lu)
│   ├── dgs_akilli_8_yillik_veri.json
│   └── dogrulama_tablosu_akilli.png
├── dgs_bot.py               # Ana bot kaynak kodu
├── Dockerfile               # Docker imaj reçetesi
├── docker-compose.yml       # Konteyner orkestrasyon dosyası
├── requirements.txt         # Gerekli Python kütüphaneleri
├── .gitignore               # Repo bütünlüğü için gereksiz dosyaları engelleme listesi
└── README.md                # Proje dokümantasyonu
💻 Kurulum ve Çalıştırma
Projenin en büyük avantajı, çalıştırılacağı bilgisayarda Python, Playwright veya herhangi bir tarayıcı (Chromium vb.) kurulmasına ihtiyaç duymamasıdır. Tek gereksinim, sistemde Docker Desktop uygulamasının kurulu ve çalışır durumda olmasıdır.

Projeyi Ayağa Kaldırmak İçin:
Proje kök dizininde bir terminal (CMD/VS Code Terminal) açın.

Aşağıdaki komutu çalıştırın:

Bash
docker-compose up --build
Bu komut; gerekli imaj katmanlarını birleştirecek, kütüphaneleri yükleyecek ve botu izole bir konteyner içinde otomatik olarak tetikleyecektir. İşlem tamamlandığında konteyner güvenli bir şekilde kendini kapatacaktır.
