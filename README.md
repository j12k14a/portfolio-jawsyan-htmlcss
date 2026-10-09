# 🌐 Portofolio Pribadi - Muhammad Jawsyan (Bootstrap 5 Framework)

> **Tugas Praktikum: Website Portofolio Menggunakan CSS Template / Framework**  
> **Mata Kuliah:** Pemrograman Web (Kelas A)  
> **Dosen Pengajar:** Rahmad Syalevi, S. Kom., M.T.I  
> **Program Studi:** S1 Teknik Informatika  
> **Perguruan Tinggi:** Universitas Paramadina  
> **Batas Pengumpulan (Edlink):** 12 Oktober 2026, 23:59 WIB  
>  
> 🔗 **Tautan Publikasi Resmi:**  
> - **Live Deployment Vercel:** [https://portfolio-jawsyan-htmlcss.vercel.app](https://portfolio-jawsyan-htmlcss.vercel.app)  
> - **GitHub Repository:** [https://github.com/j12k14a/portfolio-jawsyan-htmlcss](https://github.com/j12k14a/portfolio-jawsyan-htmlcss)  
> - **GitHub Pages Demo:** [https://j12k14a.github.io/portfolio-jawsyan-htmlcss/](https://j12k14a.github.io/portfolio-jawsyan-htmlcss/)

---

## 📌 Ringkasan Proyek & Ketentuan Tugas

Website portofolio ini merupakan kelanjutan dari proyek mandiri sebelumnya, yang kini dimigrasikan dan dikembangkan menggunakan **Framework CSS Bootstrap 5 (v5.3.3)** dipadukan dengan desain kustom bertema *Cyber Dark Terminal*. Proyek ini memenuhi seluruh 6 kriteria utama yang diberikan oleh dosen pengampu pada platform Edlink:

1. **Framework CSS:** Menerapkan **Bootstrap 5.3.3** (CDN resmi dengan dukungan Popper JS dan Bootstrap Icons v1.11.3).
2. **Kelengkapan Bagian Wajib:** Memuat lengkap bagian **Beranda**, **Tentang Saya**, **Proyek** (4 item proyek unggulan &gt; syarat minimal 3), **Prestasi / Sertifikasi**, dan **Kontak**.
3. **Desain Responsif:** Tampilan teruji rapi dan proporsional pada layar ponsel beresolusi sempit (**≈ 375px**, e.g., iPhone SE) hingga layar monitor desktop resolusi tinggi tanpa terjadi *horizontal overflow*.
4. **HTML5 Semantik:** Struktur halaman dibangun menggunakan elemen semantik murni (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`).
5. **Penyimpanan Kode & Publikasi:** Tersimpan rapi di GitHub sesuai aturan praktikum 6.4 dan terpublikasikan di **Vercel** serta GitHub Pages.
6. **Pelaporan Edlink:** Repositori publik dan URL Vercel siap dikumpulkan sebelum tenggat waktu.

---

## 🛠️ Arsitektur & Teknologi

| Komponen | Spesifikasi / Library | Keterangan |
|---|---|---|
| **Struktur Inti** | HTML5 Semantic Elements | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` |
| **Framework CSS** | Bootstrap 5.3.3 | Grid system, Navbar collapse, Form floating labels, Responsive tables, Modals/Cards |
| **Ikonografi** | Bootstrap Icons 1.11.3 | Ikon antarmuka modern dan ringan via CDN |
| **Tipografi** | Google Fonts | `Inter` (sans-serif modern) & `Fira Code` (monospace teknikal) |
| **Custom Styling** | `assets/css/style.css` | Cyber dark palette (`#090d16`, neon cyan `#00f2fe`, gold `#f59e0b`, glassmorphism) |
| **Hosting & CI/CD** | Vercel & GitHub | Distribusi global CDN berkecepatan tinggi dengan HTTPS otomatis |

---

## 📑 Struktur Halaman & Bagian (Section Breakdown)

### 1. Header & Navigasi Semantik (`<header>`, `<nav>`)
- Navbar responsif *sticky-top* dengan efek *glassmorphism backdrop blur*.
- Tombol burger toggle otomatis untuk layar ponsel lebar ≈ 375px.
- Terintegrasi fitur Bootstrap *ScrollSpy* dengan navigasi halus (*smooth scrolling*).

### 2. Beranda / Hero Section (`#beranda`)
- Tagline status sistem: `SYSTEM_ONLINE // ETHICAL_HACKER`.
- Foto profil personal dengan border glow neon dan lencana akreditasi terapung (*floating badges*).
- Tombol Call to Action (CTA) responsif dan tautan jejaring resmi (LinkedIn, GitHub, Blog, Email).

### 3. Tentang Saya (`#tentang`)
- Ringkasan latar belakang akademik di Program Studi Teknik Informatika, Universitas Paramadina.
- Kartu sorotan apresiasi siber:
  - **PUSSIBER TNI AD (Kartika CSIRT)**: No. `SERT/36/PUSSIBERAD/KARTIKA-CSIRT/IX/2026`.
  - **BSSA Diskominfotik DKI Jakarta**: No. `113/BUG/BSSA/VIII/2026`.
- Data tabel biodata akademik dan visualisasi bilah keahlian (*technical skill progress bars*).

### 4. Proyek Unggulan (`#proyek`) — *Minimal 3 Item Terpenuhi (Tersedia 4 Item)*
Setiap proyek disajikan dalam semantic `<article class="custom-card project-card">` lengkap dengan deskripsi, fitur utama, teknologi yang digunakan, serta tautan repositori:
1. **Fufufafa AI Agent (Autonomous Bug Hunter):** Agen kecerdasan buatan otonom untuk audit reconnaissance permukaan web, identifikasi celah CWE/CVE, dan generator laporan aman (Python 3, Google Gemini API, ADK).
2. **CTF Offensive Toolkit & Exploit Solver (Juara 4 Nasional):** Kumpulan skrip eksploitasi modular dan pemecah kriptografi yang membawa tim meraih 4th Place Scholar Battle Winner di ajang ZERO DAY 2026 (Kali Linux, Burp Suite, Wireshark, Cryptool).
3. **ADK UAS (Kreativitas & Inovasi Agentic AI):** Sistem terintegrasi multi-agent communication protocols dengan asynchronous API client and tool dynamic registry (Python 3.11, RESTful API, AsyncIO, JSON-RPC).
4. **Script Kiddie of Linux (Platform Edukasi Keamanan Siber):** Portal publikasi artikel teknikal analisis kerentanan, panduan hardening Linux, serta penulisan write-up CTF (Web Platform, Markdown, Linux Tools).

### 5. Prestasi & Rekapitulasi Sertifikasi (`#prestasi`)
- **Tabel Responsif 12 Dokumen Resmi:** Rekapitulasi piagam penghargaan, nomor registrasi dokumen, dan status verifikasi sah.
- **Galeri Kartu Visual Teratas (4 Dokumen Utama):**
  1. *DISKOMINFO Kota Bandung* (06 Okt 2026) - Sertifikat Apresiasi Temuan Kerentanan.
  2. *PUSSIBER TNI AD* (03 Sep 2026) - Sertifikat Apresiasi Kerentanan Kartika CSIRT.
  3. *BSSA Pemprov DKI Jakarta* (20 Agu 2026) - Sertifikat Apresiasi Vulnerability Disclosure.
  4. *ZERO DAY CTF 2026* (28 Jun 2026) - Piagam Juara 4 Nasional Scholar Battle.

### 6. Kontak (`#kontak`)
- Saluran kontak terverifikasi: Email kampus resmi, WhatsApp langsung, Afiliasi kampus, dan Blog.
- Tabel Service Level Agreement (SLA) waktu respons komunikasi.
- Formulir pesan interaktif responsif berbasis komponen Bootstrap 5 *Floating Labels* dan validasi HTML5.

### 7. Footer Semantik (`<footer>`)
- Hak cipta kepemilikan karya, identitas kelas kuliah, dan tautan pintas kembali ke setiap bagian halaman.

---

## 📱 Uji Responsivitas (375px Ponsel & Desktop)

Website telah diverifikasi menggunakan inspeksi perangkat responsif untuk memastikan:
- **Ponsel Sempit (375px - e.g. iPhone SE):**
  - Navbar tertutup rapi dalam menu hamburger tanpa menabrak judul.
  - Gambar profil mengecil secara proporsional (`190px`) dan lencana tersusun rapi di bawah foto.
  - Tombol CTA dan grup tombol formulir berubah menjadi tumpukan vertikal *full-width* (`w-100`) sehingga nyaman ditekan dengan jempol (*touch-friendly*).
  - Tabel rekapitulasi dapat digeser horizontal secara mulus via `.table-responsive` tanpa merusak batas layar utama.
- **Desktop (1024px - 1920px):**
  - Layout grid multi-kolom memanfaatkan ruang horizontal secara optimal.
  - Efek hover kartu, transisi glow, dan fixed glassmorphism navbar bekerja presisi.

---

## 📁 Struktur Direktori Repositori

```text
portfolio-jawsyan-htmlcss/
├── index.html              # Halaman Portofolio Utama (Bootstrap 5 & Semantic HTML5)
├── vercel.json             # Konfigurasi Deployment Statis Vercel
├── README.md               # Dokumentasi Lengkap Tugas Akademik
├── assets/
│   ├── css/
│   │   └── style.css       # Custom Stylesheet Eksternal (Cyber Dark Theme & Breakpoints)
│   └── img/                # Aset Foto Personal & Piagam Sertifikasi Resmi
│       ├── profile.jpg
│       ├── cert_diskominfo_bandung.png
│       ├── cert_diskominfo_bandung.pdf
│       ├── cert_pussiber_tni_ad.png
│       ├── cert_pussiber_tni_ad.pdf
│       ├── cert_bssa_dki_jakarta.png
│       ├── cert_bssa_dki_jakarta.pdf
│       ├── cert_zeroday.png
│       ├── cert_sevima_10jp.jpg
│       ├── cert_sevima_ai.jpg
│       ├── cert_sevima_cti.jpg
│       ├── cert_cisco.png
│       ├── cert_crpo.png
│       ├── cert_microsoft_ai.png
│       ├── cert_hackviser.png
│       ├── cert_merdekasiber.png
│       └── event/
│           ├── photo1.jpg
│           ├── photo2.jpg
│           └── photo3.jpg
├── achievements.html       # (Arsip Versi Vanilla HTML/CSS)
├── contact.html            # (Arsip Versi Vanilla HTML/CSS)
└── skills.html             # (Arsip Versi Vanilla HTML/CSS)
```

---

## 🚀 Panduan Deployment & Verifikasi

### 1. Menjalankan Secara Lokal
Buka file `index.html` langsung melalui browser modern (Google Chrome, Mozilla Firefox, atau Microsoft Edge), atau gunakan ekstensi Live Server pada VS Code:
```bash
# Opsi melalui npx serve (opsional)
npx serve .
```

### 2. Publikasi ke Vercel
Website ini dikonfigurasi untuk deployment langsung di Vercel:
1. Hubungkan repositori GitHub `https://github.com/j12k14a/portfolio-jawsyan-htmlcss` ke akun Vercel.
2. Vercel secara otomatis mendeteksi konfigurasi statis `index.html` dan `vercel.json`.
3. Setiap pembaruan pada branch `main` akan di-build dan di-deploy secara otomatis ke domain produksi:  
   👉 **`https://portfolio-jawsyan-htmlcss.vercel.app`**

---

## 👨‍💻 Identitas Mahasiswa

- **Nama:** Muhammad Jawsyan  
- **NIM / Jurusan:** S1 Teknik Informatika  
- **Perguruan Tinggi:** Universitas Paramadina  
- **Mata Kuliah:** Pemrograman Web (Kelas A)  
- **Dosen Pengampu:** Rahmad Syalevi, S. Kom., M.T.I
