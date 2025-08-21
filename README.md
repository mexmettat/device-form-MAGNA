# 🏭 Kurumsal Ekipman Teslim & İade Formu

Bu proje, fabrika ve ofis ortamlarında çalışanların **ekipman teslimi** ve **iadesi** süreçlerini dijitalleştirmek için geliştirilmiş bir **Flask tabanlı web uygulamasıdır**.  
Kullanıcılar, giriş ekranından form tipini seçerek (Teslim veya İade) ilgili formu doldurabilir ve **PDF çıktısı** alabilirler.

## 🚀 Özellikler
- 📌 **Form Seçimi:** Açılış ekranında Teslim veya İade seçme  
- 🖥️ **Ekipman Listesi:** Bilgisayar, telefon, sim kart, monitör vb. cihazlar  
- ✏️ **Diğer Alanı:** Uzun metinlerde satır kaydırma destekli  
- ✅ **Oryantasyon Onayı:** “Oryantasyon aldım” kutucuğu  
- 📄 **PDF Çıktısı:** Kurumsal formatta, imza alanları ve logo ile yazdırılabilir  
- 🏭 **Kurumsal Tasarım:** Logo alanı, ortalanmış giriş ekranı, fabrika kullanımı için optimize edilmiş sade arayüz  

## 🛠 Kullanılan Teknolojiler
- **Backend:** Python (Flask)  
- **Frontend:** HTML5, CSS3, Jinja2  
- **PDF:** Tarayıcı yazdırma (Print to PDF)  

## 📂 Proje Yapısı
```
EKIPMAN-FORM/
├── static/
│   ├── magna-icon.png
│   ├── magna-logo.png
│   └── style.css
├── templates/
│   ├── form.html
│   ├── home.html
│   └── pdf.html
├── app.py
├── requirements.txt
└── venv/
```

## ⚙️ Kurulum & Çalıştırma
```bash
# 1. Repo klonla
git clone https://github.com/mexmettat/ekipman-form.git
cd ekipman-form

# 2. Sanal ortam oluştur ve aktif et
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Uygulamayı başlat
python app.py
```

👉 Tarayıcıda aç: **http://127.0.0.1:5000**

## 📸 Ekran Görüntüleri
- **Ana Sayfa:** Teslim / İade seçimi  
- **Form Sayfası:** Ekipman listesi + diğer alan  
- **PDF Çıktısı:** Kurumsal tasarım, imza bölümü, logo  

## 👨‍💻 Geliştiren
**Mehmet TAT**  
- [GitHub](https://github.com/mexmettat)  
- [LinkedIn](https://www.linkedin.com/in/mehmettat/)  
