# 🌐 Web Profile Pribadi - Muhammad Jawsyan (PHP & MySQL Database)

> **Tugas Praktikum: Web Profile dengan PHP dan MySQL**  
> **Mata Kuliah:** Pemrograman Web (Kelas A)  
> **Dosen Pengajar:** Rahmad Syalevi, S. Kom., M.T.I  
> **Program Studi:** S1 Teknik Informatika (Fakultas Ilmu Rekayasa)  
> **Perguruan Tinggi:** Universitas Paramadina  
> **Repositori GitHub:** [https://github.com/j12k14a/portfolio-jawsyan-htmlcss](https://github.com/j12k14a/portfolio-jawsyan-htmlcss)  
> **Live Demo Web (Firebase Hosting):** [https://jawsyanbreachlog-3c8b3.web.app](https://jawsyanbreachlog-3c8b3.web.app)  
> **Live Demo Web (GitHub Pages):** [https://j12k14a.github.io/portfolio-jawsyan-htmlcss/](https://j12k14a.github.io/portfolio-jawsyan-htmlcss/)  
> **Live Demo Web (Local XAMPP):** `http://localhost/portfolio-jawsyan/index.php`  
> **Database:** `db_portofolio` (MySQL / MariaDB via PDO) & Firebase Cloud Firestore (Project: `jawsyanbreachlog`)

---

## 📌 Deskripsi Tugas & Pemenuhan Ketentuan

Tugas ini merupakan modifikasi dan peningkatan website profil portofolio pribadi dari antarmuka statis (*frontend: HTML5, CSS3, JS*) ke versi dinamis berbasis **PHP Server-Side Scripting** yang terkoneksi penuh dengan **Database MySQL**.

Sesuai instruksi pada modul perkuliahan dan portal Edlink:
1. **Migrasi ke PHP:** Seluruh data profil yang tampil di halaman HTML berasal langsung dari database melalui file `index.php`.
2. **Koneksi Database Terpisah:** Disediakan file `koneksi.php` menggunakan **PDO (PHP Data Objects)** yang mendukung *prepared statement* untuk proteksi terhadap celah *SQL Injection* (sesuai materi slide 21 & 30).
3. **Struktur Database Sederhana & Terstruktur:** Database bernama `db_portofolio` dengan tabel-tabel sesuai instruksi modul:
   - `tbl_data_pribadi` : Informasi identitas diri, foto, NIM, status sistem, dan tagline.
   - `tbl_pendidikan`   : Riwayat jenjang pendidikan, program studi, dan masa studi.
   - `tbl_skill`        : Daftar keahlian teknis keamanan siber, AI, dan persentase penguasaan.
   - `tbl_portofolio`   : Data katalog proyek (4 item proyek unggulan).
   - `tbl_kontak`       : Saluran komunikasi resmi, tautan WhatsApp, email kampus, blog, dan media sosial.
   - `tbl_prestasi`     : Rekapitulasi 14 dokumen sertifikasi dan piagam apresiasi resmi (termasuk kategori militer SATSIBER TNI & TNI AD, serta Juara 4 CTF Nasional).
   - `tbl_pesan`        : Penampung kiriman pesan masuk dari formulir kontak via metode `POST`.
4. **Formulir Interaktif Terkoneksi MySQL:** Formulir kontak pada bagian `#kontak` memproses data pengirim via `$_POST` dan menyimpannya secara otomatis ke tabel `tbl_pesan`.

---

## 🛠️ Arsitektur & Teknologi

| Komponen | Spesifikasi / Tools | Keterangan |
|---|---|---|
| **Server-Side Engine** | PHP (PDO Extension) | Kompatibel dengan PHP 5.3+ hingga PHP 8.3+ |
| **Database Server** | MySQL / MariaDB | Database `db_portofolio` dengan engine InnoDB & charset UTF-8 |
| **Frontend Framework** | Bootstrap 5.3.3 | Responsif pada resolusi ponsel (≈ 375px) hingga desktop |
| **Ikonografi** | Bootstrap Icons 1.11.3 | Ikon modern berbasis CDN |
| **Web Server Lokal** | Apache (XAMPP / Laragon) | Berjalan di `http://localhost/portfolio-jawsyan/` |
| **Version Control** | Git & GitHub | Disimpan di branch `main` repositori resmi |

---

## 🗄️ Skema Database (`db_portofolio`)

Database `db_portofolio` tersimpan dalam berkas `db_portofolio.sql`. Berikut adalah ringkasan struktur tabel:

### 1. `tbl_data_pribadi`
Menyimpan informasi biodata utama mahasiswa.
```sql
CREATE TABLE `tbl_data_pribadi` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama_lengkap` VARCHAR(100) NOT NULL,
    `nama_panggilan` VARCHAR(50) NOT NULL,
    `nim` VARCHAR(20) NOT NULL,
    `program_studi` VARCHAR(100) NOT NULL,
    `fakultas` VARCHAR(100) NOT NULL,
    `universitas` VARCHAR(100) NOT NULL,
    `status_sistem` VARCHAR(50) NOT NULL,
    `tagline` VARCHAR(255) NOT NULL,
    `ringkasan_bio` TEXT NOT NULL,
    `tentang_lengkap` TEXT NOT NULL,
    `foto_profil` VARCHAR(255) NOT NULL,
    `badge_kehormatan_1` VARCHAR(100) NOT NULL,
    `badge_kehormatan_2` VARCHAR(100) NOT NULL
);
```

### 2. `tbl_pendidikan`
Menyimpan riwayat pendidikan formal dan vokasi.
```sql
CREATE TABLE `tbl_pendidikan` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `jenjang` VARCHAR(50) NOT NULL,
    `nama_institusi` VARCHAR(150) NOT NULL,
    `jurusan` VARCHAR(100) NOT NULL,
    `periode` VARCHAR(50) NOT NULL,
    `status` VARCHAR(50) NOT NULL,
    `keterangan` TEXT NOT NULL,
    `urutan` INT DEFAULT 1
);
```

### 3. `tbl_skill`
Menyimpan keahlian teknis beserta persentase bar visual.
```sql
CREATE TABLE `tbl_skill` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama_skill` VARCHAR(100) NOT NULL,
    `kategori` VARCHAR(50) NOT NULL,
    `persentase` INT NOT NULL,
    `level` VARCHAR(50) NOT NULL,
    `ikon` VARCHAR(50) NOT NULL,
    `urutan` INT DEFAULT 1
);
```

### 4. `tbl_portofolio`
Menyimpan daftar proyek unggulan.
```sql
CREATE TABLE `tbl_portofolio` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `judul_proyek` VARCHAR(150) NOT NULL,
    `kategori` VARCHAR(50) NOT NULL,
    `badge_text` VARCHAR(50) NOT NULL,
    `badge_color` VARCHAR(20) NOT NULL,
    `deskripsi` TEXT NOT NULL,
    `fitur_1` VARCHAR(255) NOT NULL,
    `fitur_2` VARCHAR(255) NOT NULL,
    `fitur_3` VARCHAR(255) NOT NULL,
    `teknologi` VARCHAR(255) NOT NULL,
    `link_github` VARCHAR(255) NOT NULL,
    `ikon` VARCHAR(50) NOT NULL,
    `urutan` INT DEFAULT 1
);
```

### 5. `tbl_kontak`
Menyimpan kontak dan tautan komunikasi resmi.
```sql
CREATE TABLE `tbl_kontak` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `jenis` VARCHAR(50) NOT NULL,
    `label` VARCHAR(100) NOT NULL,
    `nilai` VARCHAR(255) NOT NULL,
    `tautan` VARCHAR(255) NOT NULL,
    `ikon` VARCHAR(50) NOT NULL,
    `keterangan` VARCHAR(100) NOT NULL,
    `urutan` INT DEFAULT 1
);
```

### 6. `tbl_prestasi`
Menyimpan rekapitulasi sertifikasi resmi dan piagam apresiasi (TNI AD, BSSA DKI Jakarta, CTF Zero Day, dll.).
```sql
CREATE TABLE `tbl_prestasi` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `tanggal` VARCHAR(50) NOT NULL,
    `tgl_urut` DATE NOT NULL,
    `judul_prestasi` VARCHAR(255) NOT NULL,
    `kategori` VARCHAR(100) NOT NULL,
    `penyelenggara` VARCHAR(150) NOT NULL,
    `no_registrasi` VARCHAR(100) NOT NULL,
    `status_verifikasi` VARCHAR(100) NOT NULL,
    `badge_class` VARCHAR(50) NOT NULL,
    `gambar_piagam` VARCHAR(255) NOT NULL,
    `is_featured` TINYINT(1) DEFAULT 0,
    `is_militer` TINYINT(1) DEFAULT 0,
    `urutan` INT DEFAULT 1
);
```

### 7. `tbl_pesan`
Menyimpan masukan dari formulir kontak.
```sql
CREATE TABLE `tbl_pesan` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `subjek` VARCHAR(150) NOT NULL,
    `pesan` TEXT NOT NULL,
    `ip_address` VARCHAR(50) DEFAULT NULL,
    `tgl_kirim` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 💻 Script Koneksi Database (`koneksi.php`)

```php
<?php
$db_host = "localhost";
$db_user = "root";
$db_pass = "";
$db_name = "db_portofolio";
$charset = "utf8mb4";

$dsn = "mysql:host=" . $db_host . ";dbname=" . $db_name . ";charset=" . $charset;

$options = array(
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
);

try {
    $pdo = new PDO($dsn, $db_user, $db_pass, $options);
} catch (PDOException $e) {
    die("Koneksi database gagal: " . htmlspecialchars($e->getMessage()));
}
?>
```

---

## 🚀 Panduan Menjalankan Proyek di Komputer Lokal

1. **Jalankan XAMPP / Laragon:**  
   Aktifkan modul **Apache** dan **MySQL**.
2. **Import Database:**  
   - Buka phpMyAdmin di browser: `http://localhost/phpmyadmin/`.
   - Buat database baru bernama `db_portofolio`.
   - Pilih tab **Import**, pilih file `db_portofolio.sql`, lalu klik **Go / Kirim**.
3. **Salin Folder Proyek ke Webroot:**  
   Letakkan folder proyek di dalam direktori `C:\xampp\htdocs\portfolio-jawsyan\`.
4. **Buka di Browser:**  
   Akses alamat URL:  
   👉 **`http://localhost/portfolio-jawsyan/index.php`**

---

## 👨‍💻 Identitas Mahasiswa

- **Nama Lengkap:** Muhammad Jawsyan  
- **NIM:** 125103034  
- **Program Studi:** S1 Teknik Informatika  
- **Mata Kuliah:** Pemrograman Web (Kelas A)  
- **Dosen Pengampu:** Rahmad Syalevi, S. Kom., M.T.I  
- **Institusi:** Universitas Paramadina
