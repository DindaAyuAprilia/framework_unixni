# UnixNi Company Profile

UnixNi Company Profile adalah website company profile dinamis berbasis **Django** yang dikembangkan sebagai proyek akademik.

Project ini menerapkan konsep pengelolaan konten berbasis database, sehingga berbagai informasi pada website seperti teks, gambar, profil perusahaan, tim, galeri, FAQ, dan artikel dapat diperbarui melalui **Django Admin** tanpa harus mengubah source code halaman secara langsung.

## Tujuan Project

Project ini dibuat untuk mempelajari bagaimana konten website dapat dipisahkan dari tampilan dan dikelola sebagai data.

Dengan pendekatan ini, administrator dapat memperbarui informasi website melalui panel admin, sementara halaman frontend secara otomatis menampilkan data terbaru dari database.

## Fitur Utama

### Pengelolaan Konten Dinamis

Konten website dapat dikelola melalui Django Admin, meliputi:

- Hero / welcome section
- Profil perusahaan
- Nilai perusahaan
- Logo brand atau partner
- Testimoni
- FAQ
- Informasi tentang perusahaan
- Misi dan struktur organisasi
- Informasi tim
- Pencapaian dan target
- Galeri dan dokumentasi
- Informasi kontak
- Jam operasional
- Alamat
- Blog dan artikel

### Homepage

Homepage mengambil data secara dinamis dari database untuk menampilkan:

- Welcome content
- Nilai perusahaan
- Brand/partner
- Testimoni
- FAQ

Administrator dapat memperbarui informasi tersebut melalui Django Admin tanpa mengubah template HTML.

### Tentang Kami

Halaman About menampilkan data seperti:

- Profil perusahaan
- Deskripsi perusahaan
- Misi
- Struktur organisasi
- Logo dan diagram pendukung

### Tim

Halaman tim menyediakan informasi mengenai:

- Profil tim
- Nilai
- Pencapaian
- Target

### Galeri

Fitur galeri mencakup:

- Pengelolaan kategori galeri
- Upload gambar
- Pengelolaan item galeri
- Pengelompokan dokumentasi

### Blog

Fitur blog meliputi:

- Pembuatan dan pengelolaan artikel
- Upload gambar artikel
- Tanggal publikasi
- Tag artikel
- Pencarian artikel berdasarkan judul
- Related post
- Like artikel
- Komentar pengguna

### Kontak

Halaman kontak menampilkan:

- Informasi kontak
- Jam operasional
- Alamat
- Form pengiriman email

### Authentication

Project menggunakan sistem autentikasi Django untuk mendukung fitur yang membutuhkan akun pengguna, seperti interaksi pada artikel.

## Teknologi yang Digunakan

| Teknologi | Kegunaan |
| --- | --- |
| Python | Bahasa pemrograman backend |
| Django | Framework pengembangan web |
| Django ORM | Pengelolaan dan pemodelan data |
| Django Admin | Administrasi dan pengelolaan konten |
| SQLite | Database pengembangan |
| HTML | Struktur halaman |
| CSS | Styling |
| JavaScript | Interaksi frontend |
| Bootstrap | Komponen antarmuka |
| Git & GitHub | Version control |

## Konsep Pengelolaan Konten

```text
Administrator
      |
      v
 Django Admin
      |
      v
Django Models / ORM
      |
      v
   Database
      |
      v
 Django Views
      |
      v
   Templates
      |
      v
Company Profile Website
```

Konten website disimpan pada database melalui Django Models.

Administrator dapat melakukan penambahan, perubahan, atau penghapusan konten melalui Django Admin. Data kemudian dipanggil oleh Django Views dan ditampilkan secara dinamis pada halaman website.

Dengan konsep ini, pembaruan informasi website tidak selalu membutuhkan perubahan pada source code.

## Model Data

Beberapa data yang dikelola dalam aplikasi meliputi:

- Welcome Card
- Company Value
- Company Profile
- Trusted Brand
- Testimonial
- FAQ
- About
- Mission
- Structure
- Team
- Achievement
- Target
- Gallery
- Contact
- Working Hours
- Address
- Blog Post
- Tag
- Related Post
- Comment

## Menjalankan Project

### 1. Buat Virtual Environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 2. Install Dependency

```bash
pip install django pillow
```

### 3. Jalankan Migration

Masuk ke direktori yang berisi `manage.py`, kemudian:

```bash
python manage.py migrate
```

### 4. Buat Akun Administrator

```bash
python manage.py createsuperuser
```

### 5. Jalankan Development Server

```bash
python manage.py runserver
```

Buka:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Pembelajaran dari Project

Melalui project ini saya mempelajari bahwa informasi pada website tidak harus ditulis secara statis di dalam HTML.

Konten seperti teks, gambar, profil, galeri, FAQ, dan artikel dapat disimpan sebagai data pada database dan dikelola melalui Django Admin. Pendekatan ini membuat website lebih mudah diperbarui dan dikelola tanpa harus mengubah source code setiap kali informasi berubah.

Project ini memberikan pengalaman dalam:

- Pengembangan website dengan Django
- Front-end dan back-end development
- Pemodelan database
- Django ORM
- Django Admin
- Dynamic content management
- Pengelolaan gambar dan media
- Authentication
- Blog dan interaksi pengguna
- Pengelolaan form
- Git dan GitHub

## Developer

**Dinda Ayu Aprilia**  
S1 Informatika — Universitas Mulawarman

GitHub: [DindaAyuAprilia](https://github.com/DindaAyuAprilia)
