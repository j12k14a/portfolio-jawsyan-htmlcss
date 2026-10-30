<?php
/**
 * ==============================================================================
 * KONEKSI DATABASE MYSQL (PDO & MYSQLI DUAL COMPATIBILITY)
 * Mata Kuliah : Pemrograman Web (Kelas A) - Universitas Paramadina
 * Dosen       : Rahmad Syalevi, S. Kom., M.T.I
 * Referensi   : Modul Pertemuan 5 - PHP Server-Side Scripting & MySQL CRUD
 * ==============================================================================
 */

// Konfigurasi Kredensial Database MySQL
$db_host = "localhost";
$db_user = "root";
$db_pass = "";
$db_name = "db_portofolio";
$charset = "utf8mb4";

// 1. KONEKSI UTAMA MENGGUNAKAN PDO (Sesuai Materi Modul Kuliah Slide 21)
// PDO mendukung prepared statement otomatis guna mencegah kerentanan SQL Injection
$dsn = "mysql:host=" . $db_host . ";dbname=" . $db_name . ";charset=" . $charset;

$options = array(
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
);

try {
    $pdo = new PDO($dsn, $db_user, $db_pass, $options);
} catch (PDOException $e) {
    // Tampilkan pesan kegagalan ramah pengguna
    die("<div style='font-family:sans-serif; padding:20px; background:#fee2e2; color:#991b1b; border-radius:8px; margin:20px;'>
            <h3>⚠️ Koneksi Database (PDO) Gagal</h3>
            <p>Pastikan layanan MySQL di XAMPP / Laragon sudah aktif dan database <strong>" . $db_name . "</strong> telah diimpor.</p>
            <small>Detail Teknis: " . htmlspecialchars($e->getMessage()) . "</small>
         </div>");
}

// 2. KONEKSI PENDAMPING MYSQLI (Untuk Fleksibilitas Tambahan)
$koneksi = @mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if (!$koneksi) {
    // Fallback logging jika mysqli gagal
    error_log("Koneksi mysqli gagal: " . mysqli_connect_error());
}
?>
