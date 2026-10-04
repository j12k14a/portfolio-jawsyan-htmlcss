# 🌐 Portofolio Pribadi - Muhammad Jawsyan (Pure HTML5 & CSS3)

> **Tugas Individu: Halaman Web HTML & CSS**  
> **Mata Kuliah:** Pemrograman Web (Kelas A)  
> **Dosen Pengajar:** Rahmad Syalevi, S. Kom., M.T.I  
> **Program Studi:** S1 Teknik Informatika  
> **Perguruan Tinggi:** Universitas Paramadina  
> **Live Demo (GitHub Pages):** [https://j12k14a.github.io/portfolio-jawsyan-htmlcss/](https://j12k14a.github.io/portfolio-jawsyan-htmlcss/)

---

## 📌 Deskripsi Proyek
Website portofolio pribadi ini dirancang dan dibangun dari awal (**from scratch**) murni hanya menggunakan komponen standar **HTML5 dan CSS3** tanpa menggunakan template atau framework CSS/JS apapun (seperti Bootstrap, Tailwind, atau jQuery), sesuai dengan instruksi penugasan akademik.

Desain tata letak terinspirasi dari konsep **iPortfolio** dengan navigasi sidebar modern, tipografi bersih berorientasi tema *Cyber Security & Artificial Intelligence*, serta tata letak responsif (*mobile-friendly*).

---

## ✅ Pemenuhan Seluruh Kriteria Penugasan

| No | Kriteria Tugas | Implementasi pada Proyek | Lokasi Bukti Kode |
|---|---|---|---|
| 1 | **Minimal 3 Halaman & Menu Navigasi** | Memiliki **4 Halaman** terintegrasi: `index.html` (Home/About), `skills.html` (Skills/Experience), `achievements.html` (Achievements/Table), dan `contact.html` (Kontak/Form) dengan menu navigasi konsisten. | `<header class="sidebar"><nav><ul class="nav-menu">...</ul></nav></header>` di semua halaman |
| 2 | **Elemen `table`** | Tabel data biodata akademik pada `index.html`, **Tabel rekapitulasi 11 sertifikat lengkap** pada `achievements.html`, dan tabel SLA kontak pada `contact.html`. | `<table class="achieve-table">` di `achievements.html` & `<table class="biodata-table">` di `index.html` |
| 3 | **Elemen `image`** | Foto profil personal, dokumentasi foto acara Capture The Flag (CTF), serta galeri gambar piagam/sertifikat beresolusi tinggi. | `<img src="assets/img/profile.jpg">`, `cert_pussiber_tni_ad.png`, `cert_bssa_dki_jakarta.png`, dll. |
| 4 | **Elemen `link`** | Tautan internal antar menu halaman, link dokumen PDF sertifikat, link profil LinkedIn, GitHub, dan blog edukasi. | `<a href="...">`, `<a href="mailto:...">`, `<a href="tel:...">`, link download PDF |
| 5 | **Elemen `list`** | Daftar keahlian (`<ul>`), prosedur standar pelaporan kerentanan (`<ol>`), dan glosarium istilah siber (`<dl>`, `<dt>`, `<dd>`). | Terdapat di `skills.html` dan `index.html` |
| 6 | **Elemen `form`** | Formulir filter & pencarian arsip sertifikat terstruktur. | `<form action="#" method="GET">` di `achievements.html` |
| 7 | **Elemen `input`** | Input pencarian kata kunci (`type="search"`) serta dropdown kategori (`<select>`). | Terdapat di dalam form pada `achievements.html` |
| 8 | **Elemen `button`** | Tombol aksi `<button type="submit">` (Cari Arsip) dan `<button type="reset">` (Reset Filter). | Terdapat di form `achievements.html` |
| 9 | **CSS Eksternal** | File stylesheet global `assets/css/style.css` yang mengatur variabel warna, grid/flexbox, typography, dan responsivitas. | `<link rel="stylesheet" href="assets/css/style.css">` |
| 10 | **CSS Internal** | Tag `<style>` di dalam `<head>` pada setiap file HTML yang menangani styling khusus per halaman. | `<style>...</style>` di `<head>` pada `index.html`, `skills.html`, `achievements.html`, `contact.html` |
| 11 | **CSS Inline** | Atribut `style="..."` pada elemen tertentu seperti penentuan width progress bar dinamis, badge terverifikasi, dan aksen warna khusus. | Contoh: `style="width: 92%;"`, `style="color: var(--accent-gold);"`, dsb. |
| 12 | **Struktur Dokumen HTML5** | Penggunaan semantic tags HTML5: `<!DOCTYPE html>`, `<html lang="id">`, `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<figure>`, `<figcaption>`. | Terstruktur rapi di seluruh dokumen |
| 13 | **Tanpa Template / Framework** | 100% Vanilla HTML5 & CSS3 buatan tangan sendiri tanpa library eksternal. | Murni kode native HTML & CSS |

---

## 🏆 Sorotan Khusus Prestasi (Featured Content)
1. **Pusat Siber TNI Angkatan Darat (PUSSIBER TNI AD) - Kartika CSIRT**
   - *Sertifikat Apresiasi:* Koordinasi Temuan Kerentanan & Pelaporan Etis (Nomor: `SERT/36/PUSSIBERAD/KARTIKA-CSIRT/IX/2026`).
2. **Badan Siber Sandi dan Aplikasi (BSSA) - Diskominfotik Pemprov DKI Jakarta**
   - *Sertifikat Apresiasi:* Penemuan & Pelaporan Vulnerability Sistem Elektronik (Nomor: `113/BUG/BSSA/VIII/2026`).
3. **Juara 4 Nasional Scholar Battle Winner** - Capture The Flag (CTF) Competition: ZERO DAY 2026.
4. **SEVIMA Security Challenge 2026** (3 Rangkaian Sertifikasi: MOOC 10 JP, AI Disruptions, & Cyber Threat Intelligence).
5. Sertifikasi industri internasional lainnya: **Cisco Networking Academy**, **EU Cyber Academy (CRPO)**, **Microsoft AI Skills**, **Hackviser**, dan **Merdeka Siber**.

---

## 📁 Struktur Direktori
```text
portfolio-jawsyan-htmlcss/
├── index.html          # Halaman Utama (Home & About Me / Biodata Diri)
├── skills.html         # Halaman Keahlian (Skills, Tools & Pengalaman)
├── achievements.html   # Halaman Prestasi (Tabel Data & Galeri Sertifikat)
├── contact.html        # Halaman Kontak (Informasi Kontak & Form Interaktif)
├── README.md           # Dokumentasi Penugasan Akademik
└── assets/
    ├── css/
    │   └── style.css   # Stylesheet Eksternal (Pure CSS3)
    └── img/            # Aset Gambar & Berkas PDF Sertifikat
        ├── profile.jpg
        ├── cert_pussiber_tni_ad.png
        ├── cert_pussiber_tni_ad.pdf
        ├── cert_bssa_dki_jakarta.png
        ├── cert_bssa_dki_jakarta.pdf
        ├── cert_zeroday.png
        ├── cert_sevima_10jp.jpg
        ├── cert_sevima_ai.jpg
        ├── cert_sevima_cti.jpg
        ├── cert_cisco.png
        ├── cert_crpo.png
        ├── cert_microsoft_ai.png
        ├── cert_hackviser.png
        ├── cert_merdekasiber.png
        └── event/
            ├── photo1.jpg
            ├── photo2.jpg
            └── photo3.jpg
```
