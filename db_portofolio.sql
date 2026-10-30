-- ==============================================================================
-- DATABASE PORTOFOLIO PRIBADI MUHAMMAD JAWSYAN
-- Mata Kuliah : Pemrograman Web (Kelas A) - Universitas Paramadina
-- Dosen       : Rahmad Syalevi, S. Kom., M.T.I
-- DBMS        : MySQL / MariaDB (phpMyAdmin)
-- ==============================================================================

CREATE DATABASE IF NOT EXISTS `db_portofolio` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `db_portofolio`;

-- ------------------------------------------------------------------------------
-- 1. TABEL: tbl_data_pribadi
-- Menyimpan informasi biodata inti, foto profil, dan status utama
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_data_pribadi`;
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
    `badge_kehormatan_2` VARCHAR(100) NOT NULL,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_data_pribadi` (
    `id`, `nama_lengkap`, `nama_panggilan`, `nim`, `program_studi`, `fakultas`, `universitas`, 
    `status_sistem`, `tagline`, `ringkasan_bio`, `tentang_lengkap`, `foto_profil`, 
    `badge_kehormatan_1`, `badge_kehormatan_2`
) VALUES (
    1,
    'Muhammad Jawsyan',
    'Jawsyan',
    '125103034',
    'S1 Teknik Informatika',
    'Fakultas Ilmu Rekayasa',
    'Universitas Paramadina',
    'SYSTEM_ONLINE // ETHICAL_HACKER',
    'Offensive Security, Vulnerability Disclosure & AI Engineering',
    'Mahasiswa Teknik Informatika Universitas Paramadina yang berdedikasi dalam memperkuat ketahanan infrastruktur siber melalui riset kerentanan etis serta eksplorasi sistem otonom berbasis Artificial Intelligence.',
    'Berdedikasi dalam memperkuat ketahanan infrastruktur siber nasional melalui riset celah keamanan (vulnerability research) secara etis yang telah diakui resmi oleh PUSSIBER TNI AD (Kartika CSIRT), BSSA Diskominfotik Pemprov DKI Jakarta, dan Diskominfo Kota Bandung, serta peraih Juara 4 Nasional Capture The Flag (CTF) Zero Day 2026.',
    'assets/img/profile.jpg',
    'Apresiasi PUSSIBER TNI AD',
    'Juara 4 CTF Zero Day'
);

-- ------------------------------------------------------------------------------
-- 2. TABEL: tbl_pendidikan
-- Menyimpan riwayat pendidikan formal dan fokus studi
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_pendidikan`;
CREATE TABLE `tbl_pendidikan` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `jenjang` VARCHAR(50) NOT NULL,
    `nama_institusi` VARCHAR(150) NOT NULL,
    `jurusan` VARCHAR(100) NOT NULL,
    `periode` VARCHAR(50) NOT NULL,
    `status` VARCHAR(50) NOT NULL,
    `keterangan` TEXT NOT NULL,
    `urutan` INT DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_pendidikan` (`id`, `jenjang`, `nama_institusi`, `jurusan`, `periode`, `status`, `keterangan`, `urutan`) VALUES
(1, 'Strata 1 (S1)', 'Universitas Paramadina', 'Teknik Informatika', '2024 - Sekarang', 'Mahasiswa Aktif', 'Fokus pada Keamanan Siber (Cyber Security), Arsitektur Web Lanjut, Rekayasa Perangkat Lunak, dan AI Engineering.', 1),
(2, 'Pelatihan & Sertifikasi', 'CSIRT & Lembaga Pertahanan Siber', 'Offensive Security & Incident Handling', '2024 - 2026', 'Certified / Awarded', 'Pendidikan vokasi kompetensi siber, ethical hacking, analisis malware, dan pelaporan kerentanan terstruktur.', 2);

-- ------------------------------------------------------------------------------
-- 3. TABEL: tbl_skill
-- Menyimpan daftar keahlian teknis, persentase keahlian, dan kategori
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_skill`;
CREATE TABLE `tbl_skill` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama_skill` VARCHAR(100) NOT NULL,
    `kategori` VARCHAR(50) NOT NULL,
    `persentase` INT NOT NULL,
    `level` VARCHAR(50) NOT NULL,
    `ikon` VARCHAR(50) NOT NULL,
    `urutan` INT DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_skill` (`id`, `nama_skill`, `kategori`, `persentase`, `level`, `ikon`, `urutan`) VALUES
(1, 'Web Vulnerability Assessment & Pen-Testing', 'Cyber Security', 95, 'Expert', 'bi-shield-shaded', 1),
(2, 'Ethical Hacking & Bug Disclosure Prosedur', 'Cyber Security', 92, 'Expert', 'bi-bug', 2),
(3, 'Autonomous AI Agent & Prompt Engineering', 'Artificial Intelligence', 88, 'Advanced', 'bi-robot', 3),
(4, 'Python Exploit Development & Automation', 'Programming', 90, 'Advanced', 'bi-terminal', 4),
(5, 'Linux Hardening & Network Forensics', 'System & Network', 89, 'Advanced', 'bi-hdd-network', 5),
(6, 'Fullstack Web (PHP, MySQL, Bootstrap 5)', 'Web Development', 87, 'Advanced', 'bi-code-slash', 6);

-- ------------------------------------------------------------------------------
-- 4. TABEL: tbl_portofolio
-- Menyimpan katalog karya proyek unggulan beserta teknologi dan repositori
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_portofolio`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_portofolio` (`id`, `judul_proyek`, `kategori`, `badge_text`, `badge_color`, `deskripsi`, `fitur_1`, `fitur_2`, `fitur_3`, `teknologi`, `link_github`, `ikon`, `urutan`) VALUES
(1, 'Fufufafa AI Agent (Autonomous Bug Hunter)', 'AI & Security', 'AI & Security', 'primary', 'Agen kecerdasan buatan otonom yang dikembangkan untuk membantu audit keamanan sistem secara otomatis. Mampu menjalankan reconnaissance permukaan web, identifikasi miskonfigurasi, serta menyusun simulasi validasi celah keamanan secara terukur.', 'Automated Endpoint & Directory Surface Mapping', 'CWE/CVE Vulnerability Scoring & Classification', 'Proof of Concept (PoC) Safe Reporting Generator', 'Python 3, Google Gemini API, Agent Development Kit (ADK), Bash Automation', 'https://github.com/j12k14a', 'bi-robot', 1),
(2, 'CTF Offensive Toolkit & Exploit Solver', 'Offensive Security', 'Juara 4 Nasional', 'warning', 'Kumpulan toolkit eksploitasi modular dan skrip pemecah tantangan kompetisi Capture The Flag (CTF) yang berhasil mengantarkan tim meraih predikat 4th Place Scholar Battle Winner di ajang ZERO DAY 2026.', 'Custom Cryptography Decoders (RSA, AES, Custom XOR)', 'Web Exploitation Helper (IDOR, SQLi, SSTI Payload Injector)', 'Memory Dump & Network Traffic Forensics Analyzer', 'Python, Kali Linux, Burp Suite, Wireshark, Cryptool', 'https://github.com/j12k14a', 'bi-flag-fill', 2),
(3, 'ADK UAS (Kreativitas & Inovasi Agentic AI)', 'AI Engineering', 'Academic Project', 'info', 'Proyek rekayasa sistem terintegrasi yang menghubungkan berbagai antarmuka Application Programming Interface (API) backend dengan arsitektur agen cerdas untuk otomasi alur kerja dan pengolahan data terstruktur secara asinkron.', 'Multi-Agent Communication Protocols', 'Asynchronous API Client with Exponential Backoff', 'Modular Tool Registry & Dynamic Function Calling', 'Python 3.11, RESTful API, AsyncIO, JSON-RPC', 'https://github.com/j12k14a', 'bi-cpu', 3),
(4, 'Script Kiddie of Linux (Portal Riset Siber)', 'Education & Media', 'Open Knowledge', 'success', 'Platform publikasi daring dan dokumentasi riset keamanan informasi yang berfokus pada panduan praktis hardening sistem operasi Linux, penulisan write-up kompetisi CTF, dan edukasi penanggulangan serangan siber.', 'Comprehensive Linux Hardening Guidelines', 'CTF Write-ups & Offensive Research Analysis', 'Open Discussion Hub for InfoSec Enthusiasts', 'Web Platform, Markdown Docs Engine, Bash, Linux Tools', 'https://scriptkiddieoflinux.blogspot.com', 'bi-journal-code', 4);

-- ------------------------------------------------------------------------------
-- 5. TABEL: tbl_kontak
-- Menyimpan informasi saluran komunikasi resmi dan link eksternal
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_kontak`;
CREATE TABLE `tbl_kontak` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `jenis` VARCHAR(50) NOT NULL,
    `label` VARCHAR(100) NOT NULL,
    `nilai` VARCHAR(255) NOT NULL,
    `tautan` VARCHAR(255) NOT NULL,
    `ikon` VARCHAR(50) NOT NULL,
    `keterangan` VARCHAR(100) NOT NULL,
    `urutan` INT DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_kontak` (`id`, `jenis`, `label`, `nilai`, `tautan`, `ikon`, `keterangan`, `urutan`) VALUES
(1, 'Email', 'Email Resmi Kampus', 'muhammad.jawsyan@paramadina.ac.id', 'mailto:muhammad.jawsyan@paramadina.ac.id', 'bi-envelope', 'Saluran koordinasi akademik & verifikasi identitas resmi', 1),
(2, 'WhatsApp', 'WhatsApp Langsung', '+62 811-1541-514', 'https://wa.me/628111541514', 'bi-whatsapp', 'Respons cepat untuk diskusi teknis siber & darurat', 2),
(3, 'Lokasi', 'Afiliasi Kampus', 'Universitas Paramadina, Jakarta Selatan', 'https://paramadina.ac.id', 'bi-geo-alt', 'Kampus Cipayung & Kuningan, DKI Jakarta', 3),
(4, 'Blog', 'Blog Edukasi Siber', 'scriptkiddieoflinux.blogspot.com', 'https://scriptkiddieoflinux.blogspot.com', 'bi-globe', 'Media publikasi riset dan artikel teknikal keamanan siber', 4),
(5, 'LinkedIn', 'LinkedIn Profile', 'linkedin.com/in/muhammadjawsyan', 'https://www.linkedin.com/in/muhammadjawsyan/', 'bi-linkedin', 'Jejaring profesional dan rekam jejak karir', 5),
(6, 'GitHub', 'GitHub Repositories', 'github.com/j12k14a', 'https://github.com/j12k14a', 'bi-github', 'Repositori kode sumber proyek dan portofolio', 6);

-- ------------------------------------------------------------------------------
-- 6. TABEL: tbl_prestasi
-- Menyimpan rekapitulasi sertifikasi resmi dan piagam apresiasi pemerintah/militer
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_prestasi`;
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
    `urutan` INT DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `tbl_prestasi` (`id`, `tanggal`, `tgl_urut`, `judul_prestasi`, `kategori`, `penyelenggara`, `no_registrasi`, `status_verifikasi`, `badge_class`, `gambar_piagam`, `is_featured`, `urutan`) VALUES
(1, '06 Okt 2026', '2026-10-06', 'Sertifikat Apresiasi: Temuan Kerentanan Sistem', 'Pemda Kota Bandung', 'DISKOMINFO Kota Bandung', '0105/KS.02.23/2026/DISKOMINFO', 'Terverifikasi Sah', 'bg-success', 'assets/img/cert_diskominfo_bandung.png', 1, 1),
(2, '03 Sep 2026', '2026-09-03', 'Sertifikat Apresiasi: Temuan Kerentanan & Pelaporan Etis', 'Predikat Khusus Siber Militer', 'PUSSIBER TNI AD (Kartika CSIRT)', 'SERT/36/PUSSIBERAD/KARTIKA-CSIRT/IX/2026', 'Dokumen Sah', 'bg-warning text-dark', 'assets/img/cert_pussiber_tni_ad.png', 1, 2),
(3, '20 Agu 2026', '2026-08-20', 'Sertifikat Apresiasi: Pelaporan Vulnerability Sistem Elektronik', 'Predikat Khusus Pemprov DKI', 'BSSA Diskominfotik Pemprov DKI Jakarta', '113/BUG/BSSA/VIII/2026', 'Dokumen Sah', 'bg-info text-dark', 'assets/img/cert_bssa_dki_jakarta.png', 1, 3),
(4, '28 Jun 2026', '2026-06-28', 'Juara 4 - 4th Place Scholar Battle Winner', 'Capture The Flag (CTF) Competition - ZERO DAY', 'DSG & Fakultas Ilmu Komputer', 'ZD-2026-CHAMP-04', 'Juara 4 Nasional', 'bg-primary', 'assets/img/cert_zeroday.png', 1, 4),
(5, '29 Jun 2026', '2026-06-29', 'SEVIMA Cyber Threat Intelligence sebagai Core Intel IT', 'Pelatihan Nasional Keamanan IT', 'PT Sentra Vidya Utama (SEVIMA)', '1000/SRTFK/SVM/VI/2026', 'Lulus Pelatihan', 'bg-secondary', 'assets/img/cert_sevima_cti.jpg', 0, 5),
(6, '22 Jun 2026', '2026-06-22', 'SEVIMA Security Challenge: AI Disruptions on Cyber Security', 'Workshop Ketahanan Siber & AI', 'PT Sentra Vidya Utama (SEVIMA)', '994/SRTFK/SVM/VI/2026', 'Lulus Pelatihan', 'bg-secondary', 'assets/img/cert_sevima_ai.jpg', 0, 6),
(7, '22 Jun 2026', '2026-06-22', 'MOOC 10 JP: Cyber Security Awareness & Incident Handling', 'Pelatihan Daring Mandiri Berkelanjutan', 'PT Sentra Vidya Utama (SEVIMA)', '986/SRTFK/SVM/VI/2026', 'Lulus Bersertifikat', 'bg-secondary', 'assets/img/cert_sevima_10jp.jpg', 0, 7),
(8, '07 Mei 2024', '2024-05-07', 'CRPO: Cyber Resilience Program Officer Course', 'Standar Ketahanan Siber Uni Eropa', 'EU Cyber Academy', 'EU-CRPO-88219', 'Certified', 'bg-secondary', 'assets/img/cert_crpo.png', 0, 8),
(9, '12 Feb 2024', '2024-02-12', 'Certified Network Security Practitioner (CNSP)', 'Praktisi Keamanan Jaringan Terakreditasi', 'Hackviser Academy', 'HCK-CNSP-2024-90', 'Certified', 'bg-secondary', 'assets/img/cert_hackviser.png', 0, 9),
(10, '31 Jan 2024', '2024-01-31', 'Generative AI for Youth Training', 'Pelatihan Kecerdasan Buatan Generatif', 'Microsoft AI Skills', 'MS-GENAI-2024-ID', 'Certified', 'bg-secondary', 'assets/img/cert_microsoft_ai.png', 0, 10),
(11, '21 Jan 2024', '2024-01-21', 'Introduction to Cybersecurity Course Completion', 'Fondasi Fundamental Keamanan Jaringan', 'Cisco Networking Academy', 'CISCO-NETACAD-INTRO', 'Completed', 'bg-secondary', 'assets/img/cert_cisco.png', 0, 11),
(12, '20 Jan 2024', '2024-01-20', 'Bootcamp Online Cyber Security Beginner Batch 1', 'Pelatihan Intensif Pemula Keamanan Siber', 'Merdeka Siber Academy', 'MS/BOCSE/COE/24/2026/011', 'Lulus Predikat Baik', 'bg-secondary', 'assets/img/cert_merdekasiber.png', 0, 12);

-- ------------------------------------------------------------------------------
-- 7. TABEL: tbl_pesan
-- Menyimpan pesan masuk dari formulir kontak web profil (Fitur Form POST)
-- ------------------------------------------------------------------------------
DROP TABLE IF EXISTS `tbl_pesan`;
CREATE TABLE `tbl_pesan` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nama` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `subjek` VARCHAR(150) NOT NULL,
    `pesan` TEXT NOT NULL,
    `ip_address` VARCHAR(50) DEFAULT NULL,
    `tgl_kirim` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Contoh data pesan awal
INSERT INTO `tbl_pesan` (`id`, `nama`, `email`, `subjek`, `pesan`, `ip_address`, `tgl_kirim`) VALUES
(1, 'Budi Santoso', 'budi.santoso@example.com', 'Kolaborasi Riset Keamanan Sistem', 'Halo Jawsyan, kami sangat tertarik dengan riset kerentanan etis yang Anda lakukan. Kami ingin mengajak diskusi kolaborasi.', '127.0.0.1', CURRENT_TIMESTAMP);
