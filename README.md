# Dashboard-TopUp-Game
# 🎮 Top Up K2

Top Up K2 adalah aplikasi web top up game berbasis Django yang dirancang untuk memudahkan pengguna dalam melakukan pembelian item game secara online. Aplikasi ini menyediakan layanan top up untuk beberapa game populer seperti Mobile Legends, Free Fire, PUBG Mobile, FC Mobile, dan Higgs Domino dengan berbagai pilihan nominal dan metode pembayaran.

## 📖 Deskripsi

Proyek ini dibuat sebagai implementasi pembelajaran Django Framework dan konsep Object-Oriented Programming (OOP). Pengguna dapat memilih game, memasukkan User ID, menentukan nominal top up, memilih metode pembayaran, dan melakukan transaksi. Data transaksi kemudian disimpan ke database dan ditampilkan pada halaman riwayat transaksi.

Selain berfungsi sebagai simulasi website top up game, proyek ini juga menunjukkan penerapan konsep OOP dalam pengembangan aplikasi web menggunakan Python dan Django.

---

## ✨ Fitur Utama

- Top up berbagai game populer
- Pilihan nominal sesuai game
- Input User ID pemain
- Metode pembayaran:
  - QRIS
  - DANA
  - OVO
  - GoPay
  - BCA
- Riwayat transaksi otomatis
- Popup notifikasi pembayaran berhasil
- Tampilan modern dan responsif
- Database SQLite untuk penyimpanan data

---

## 🎮 Daftar Game

- Mobile Legends
- Free Fire
- PUBG Mobile
- FC Mobile
- Higgs Domino

---

## 🛠️ Teknologi yang Digunakan

- Python 3
- Django
- HTML5
- CSS3
- JavaScript
- SQLite3

---

## 📂 Struktur Project

```text
TopUp/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── topup/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│       ├── ml.jpg
│       ├── ff.jpg
│       ├── pubg.jpg
│       ├── fc.jpg
│       └── higgs.jpg
│
├── manage.py
└── db.sqlite3
```

---

## 🧠 Implementasi OOP

### 1. Inheritance (Pewarisan)

Class turunan dapat mewarisi atribut dan method dari class induk.

```python
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class QRISPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"QRIS Payment Rp{amount}"
```

### 2. Encapsulation (Enkapsulasi)

Data transaksi disimpan dalam model Django dan dikelola melalui objek.

```python
class Transaction(models.Model):
    game = models.CharField(max_length=100)
    nominal = models.CharField(max_length=100)
    total = models.IntegerField()
```

### 3. Abstraction (Abstraksi)

Pengguna hanya mengetahui proses pembayaran tanpa perlu memahami detail implementasinya.

```python
@abstractmethod
def process_payment(self, amount):
    pass
```

### 4. Polymorphism (Polimorfisme)

Method yang sama dapat menghasilkan perilaku berbeda.

```python
class DanaPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"DANA Payment Rp{amount}"

class OvoPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"OVO Payment Rp{amount}"
```

---

## ⚙️ Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/username/topup-k2.git
```

### 2. Masuk ke Folder Project

```bash
cd TopUp
```

### 3. Buat Virtual Environment

```bash
python -m venv env
```

### 4. Aktifkan Virtual Environment

Windows:

```bash
env\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install django
```

### 6. Jalankan Migration

```bash
python manage.py migrate
```

### 7. Jalankan Server

```bash
python manage.py runserver
```

Buka browser:

```text
http://127.0.0.1:8000
```

---

## 📸 Fitur yang Tersedia

✅ Dashboard Top Up Game

✅ Popup Pembayaran

✅ Riwayat Transaksi

✅ Penyimpanan Database

✅ Implementasi OOP

✅ Responsive Design

---

## 🎯 Tujuan Proyek

- Mempelajari Django Framework
- Mengimplementasikan konsep OOP
- Membuat simulasi website top up game
- Mengelola data menggunakan database SQLite
- Mengembangkan antarmuka web interaktif

---

## 👨‍💻 Developer

Dibuat sebagai proyek pembelajaran dan implementasi Django Framework serta Object-Oriented Programming (OOP).

**Top Up K2 ⚡**
