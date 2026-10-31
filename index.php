<?php
/**
 * ==============================================================================
 * PORTFOLIO OF MUHAMMAD JAWSYAN (DYNAMIC PHP + MYSQL VERSION)
 * Framework    : Bootstrap 5.3.3 + Custom Cyber Dark Aesthetics
 * Database     : MySQL (db_portofolio) via PDO (PHP Data Objects)
 * Mata Kuliah  : Pemrograman Web (Kelas A) - Universitas Paramadina
 * Dosen        : Rahmad Syalevi, S. Kom., M.T.I
 * ==============================================================================
 */

// 1. Memuat Koneksi Database
require_once 'koneksi.php';

// 2. Pemrosesan Formulir Pesan Masuk (POST Request Handling - Sesuai Modul Pertemuan 3 & 4)
$pesan_alert = '';
if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['kirim_pesan'])) {
    $nama    = trim(isset($_POST['nama']) ? $_POST['nama'] : '');
    $email   = trim(isset($_POST['email']) ? $_POST['email'] : '');
    $subjek  = trim(isset($_POST['subjek']) ? $_POST['subjek'] : '');
    $pesan   = trim(isset($_POST['pesan']) ? $_POST['pesan'] : '');
    $ip_user = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '127.0.0.1';

    if ($nama !== '' && $email !== '' && $pesan !== '') {
        try {
            $stmt = $pdo->prepare("INSERT INTO tbl_pesan (nama, email, subjek, pesan, ip_address) VALUES (?, ?, ?, ?, ?)");
            $stmt->execute(array($nama, $email, $subjek, $pesan, $ip_user));
            $pesan_alert = 'sukses';
        } catch (Exception $e) {
            $pesan_alert = 'error';
        }
    } else {
        $pesan_alert = 'kosong';
    }
}

// 3. Query Pengambilan Data Dinamis dari Database MySQL
// A. Data Pribadi Inti
$stmt_pribadi = $pdo->query("SELECT * FROM tbl_data_pribadi LIMIT 1");
$pribadi = $stmt_pribadi->fetch();

// B. Data Riwayat Pendidikan
$stmt_pendidikan = $pdo->query("SELECT * FROM tbl_pendidikan ORDER BY urutan ASC");
$data_pendidikan = $stmt_pendidikan->fetchAll();

// C. Data Keahlian Teknis (Skills)
$stmt_skill = $pdo->query("SELECT * FROM tbl_skill ORDER BY urutan ASC");
$data_skill = $stmt_skill->fetchAll();

// D. Data Portofolio Proyek Unggulan
$stmt_portofolio = $pdo->query("SELECT * FROM tbl_portofolio ORDER BY urutan ASC");
$data_portofolio = $stmt_portofolio->fetchAll();

// E. Data Saluran Kontak Resmi
$stmt_kontak = $pdo->query("SELECT * FROM tbl_kontak ORDER BY urutan ASC");
$data_kontak = $stmt_kontak->fetchAll();

// F. Data Rekapitulasi Prestasi & Lisensi Resmi
$stmt_prestasi = $pdo->query("SELECT * FROM tbl_prestasi ORDER BY urutan ASC");
$data_prestasi = $stmt_prestasi->fetchAll();

// G. Data Galeri Piagam Unggulan (is_featured = 1)
$stmt_featured = $pdo->query("SELECT * FROM tbl_prestasi WHERE is_featured = 1 ORDER BY urutan ASC LIMIT 4");
$data_featured = $stmt_featured->fetchAll();
?>
<!DOCTYPE html>
<html lang="id" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portofolio Dinamis <?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?> - Berbasis PHP & Database MySQL">
    <meta name="author" content="<?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?>">
    <title><?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?> | Dynamic Portfolio - Cyber Security & AI</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;700&family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    
    <!-- 1. Bootstrap 5.3.3 CSS Framework -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
    <!-- Bootstrap Icons 1.11.3 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    
    <!-- Custom Cyber Dark Theme Stylesheet -->
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body data-bs-spy="scroll" data-bs-target="#mainNavbar" data-bs-offset="100" tabindex="0">

    <!-- ==========================================
         SEMANTIC HEADER & NAVBAR BOOTSTRAP 5
         ========================================== -->
    <header class="sticky-top">
        <nav id="mainNavbar" class="navbar navbar-expand-lg custom-navbar">
            <div class="container">
                <a class="navbar-brand d-flex align-items-center gap-2" href="#beranda">
                    <span class="text-cyan font-mono">&gt;</span>
                    <span><?= htmlspecialchars($pribadi['nama_panggilan'], ENT_QUOTES, 'UTF-8') ?><span>_</span></span>
                </a>
                
                <!-- Mobile Toggler Button (375px Responsive) -->
                <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <!-- Nav Links -->
                <div class="collapse navbar-collapse" id="navbarContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0 gap-lg-1">
                        <li class="nav-item">
                            <a class="nav-link active" href="#beranda"><i class="bi bi-house-door me-1"></i> Beranda</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#tentang"><i class="bi bi-person me-1"></i> Tentang Saya</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#proyek"><i class="bi bi-code-slash me-1"></i> Proyek</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#prestasi"><i class="bi bi-trophy me-1"></i> Prestasi</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#kontak"><i class="bi bi-envelope me-1"></i> Kontak</a>
                        </li>
                    </ul>
                    
                    <div class="ms-lg-3 mt-3 mt-lg-0">
                        <a href="#kontak" class="btn btn-sm btn-primary px-3">
                            <i class="bi bi-send me-1"></i> Hubungi Saya
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <!-- ==========================================
         MAIN CONTENT AREA (SEMANTIC <main>)
         Semua data dirender dinamis dari MySQL
         ========================================== -->
    <main>

        <!-- 1. BAGIAN BERANDA (HERO SECTION) -->
        <section id="beranda" class="hero-section d-flex align-items-center min-vh-100">
            <div class="container">
                <div class="row align-items-center gy-5">
                    
                    <!-- Text Content (Kiri) - Data Dinamis tbl_data_pribadi -->
                    <div class="col-12 col-lg-7 text-center text-lg-start">
                        <div class="section-tag font-mono">
                            <i class="bi bi-terminal me-1"></i> <?= htmlspecialchars($pribadi['status_sistem'], ENT_QUOTES, 'UTF-8') ?>
                        </div>
                        
                        <h1 class="display-4 fw-bold text-white mb-2">
                            Muhammad <span class="text-cyan"><?= htmlspecialchars($pribadi['nama_panggilan'], ENT_QUOTES, 'UTF-8') ?></span>
                        </h1>
                        
                        <p class="lead text-secondary mb-3">
                            Mahasiswa <strong class="text-white"><?= htmlspecialchars($pribadi['program_studi'], ENT_QUOTES, 'UTF-8') ?> <?= htmlspecialchars($pribadi['universitas'], ENT_QUOTES, 'UTF-8') ?></strong> | 
                            <span class="text-cyan fw-semibold"><?= htmlspecialchars($pribadi['tagline'], ENT_QUOTES, 'UTF-8') ?></span>
                        </p>
                        
                        <p class="text-muted mb-4 pe-lg-4" style="font-size: 0.95rem;">
                            <?= htmlspecialchars($pribadi['ringkasan_bio'], ENT_QUOTES, 'UTF-8') ?>
                        </p>
                        
                        <!-- CTA Buttons (Responsive 375px Friendly) -->
                        <div class="d-flex flex-wrap gap-2 justify-content-center justify-content-lg-start mb-4 btn-group-responsive">
                            <a href="#proyek" class="btn btn-primary px-4 py-2">
                                <i class="bi bi-grid-3x3-gap me-1"></i> Lihat Proyek Unggulan
                            </a>
                            <a href="#prestasi" class="btn btn-outline-primary px-4 py-2">
                                <i class="bi bi-award me-1"></i> Rekap Sertifikasi Resmi
                            </a>
                        </div>
                        
                        <!-- Social Media Links (Dinamis dari tbl_kontak) -->
                        <div class="d-flex gap-3 justify-content-center justify-content-lg-start align-items-center">
                            <span class="text-muted small">Jejaring Resmi:</span>
                            <?php foreach ($data_kontak as $ktk): ?>
                                <?php if ($ktk['jenis'] !== 'Lokasi'): ?>
                                    <a href="<?= htmlspecialchars($ktk['tautan'], ENT_QUOTES, 'UTF-8') ?>" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-secondary rounded-circle" title="<?= htmlspecialchars($ktk['label'], ENT_QUOTES, 'UTF-8') ?>">
                                        <i class="bi <?= htmlspecialchars($ktk['ikon'], ENT_QUOTES, 'UTF-8') ?>"></i>
                                    </a>
                                <?php endif; ?>
                            <?php endforeach; ?>
                        </div>
                    </div>
                    
                    <!-- Avatar Portrait (Kanan) -->
                    <div class="col-12 col-lg-5 text-center">
                        <div class="hero-avatar-wrapper">
                            <img src="<?= htmlspecialchars($pribadi['foto_profil'], ENT_QUOTES, 'UTF-8') ?>" alt="Foto Profil <?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?>" class="hero-avatar">
                            
                            <!-- Badges Desktop -->
                            <div class="floating-badge badge-top-right d-none d-lg-inline-flex">
                                <i class="bi bi-shield-check text-warning"></i>
                                <span><?= htmlspecialchars($pribadi['badge_kehormatan_1'], ENT_QUOTES, 'UTF-8') ?></span>
                            </div>
                            <div class="floating-badge badge-bottom-left d-none d-lg-inline-flex">
                                <i class="bi bi-trophy text-cyan"></i>
                                <span><?= htmlspecialchars($pribadi['badge_kehormatan_2'], ENT_QUOTES, 'UTF-8') ?></span>
                            </div>
                        </div>
                        
                        <!-- Badges Mobile Fallback (375px) -->
                        <div class="hero-badges-container d-lg-none mt-3">
                            <span class="floating-badge">
                                <i class="bi bi-shield-check text-warning"></i> <?= htmlspecialchars($pribadi['badge_kehormatan_1'], ENT_QUOTES, 'UTF-8') ?>
                            </span>
                            <span class="floating-badge">
                                <i class="bi bi-trophy text-cyan"></i> <?= htmlspecialchars($pribadi['badge_kehormatan_2'], ENT_QUOTES, 'UTF-8') ?>
                            </span>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>

        <!-- 2. BAGIAN TENTANG SAYA (ABOUT ME) -->
        <section id="tentang" class="py-5">
            <div class="container">
                
                <header class="text-center mb-5">
                    <span class="section-tag"><i class="bi bi-person-badge me-1"></i> TENTANG SAYA</span>
                    <h2 class="section-title">Profil & Rekam Jejak</h2>
                    <p class="section-desc mx-auto">
                        Dedikasi akademis dan profesional dalam ranah teknologi informasi, keamanan siber pertahanan, serta rekayasa kecerdasan buatan cerdas.
                    </p>
                </header>
                
                <!-- Highlight Predikat Apresiasi Khusus (Sorotan Militer, CTF Juara 4 & Instansi Resmi) -->
                <div class="row g-4 mb-5">
                    <!-- 1. SATSIBER TNI (MABES TNI) - KATEGORI MILITER -->
                    <div class="col-12 col-md-6 col-xl-3">
                        <article class="custom-card card-gold p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <span class="badge bg-warning text-dark fw-bold"><i class="bi bi-shield-fill-check me-1"></i> SIBER MILITER</span>
                                    <small class="text-warning font-mono">12 Okt 2026</small>
                                </div>
                                <h4 class="text-white h5 mb-2">SATSIBER TNI (MABES TNI)</h4>
                                <p class="text-muted small mb-3">
                                    <strong>Nomor:</strong> <code>SERT/SSTNI/63/X/2026</code><br>
                                    Piagam Penghargaan resmi dari Dansatsiber TNI (Brigjen TNI J.O. Sembiring) atas temuan celah kerentanan Sistem Informasi Mabes TNI.
                                </p>
                            </div>
                            <a href="assets/img/cert_satsiber_tni.png" target="_blank" class="btn btn-sm btn-outline-warning w-100">
                                <i class="bi bi-zoom-in me-1"></i> Buka Piagam Mabes TNI
                            </a>
                        </article>
                    </div>

                    <!-- 2. PUSSIBER TNI AD (KARTIKA CSIRT) - KATEGORI MILITER -->
                    <div class="col-12 col-md-6 col-xl-3">
                        <article class="custom-card card-gold p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <span class="badge bg-warning text-dark fw-bold"><i class="bi bi-shield-shaded me-1"></i> SIBER MILITER</span>
                                    <small class="text-warning font-mono">03 Sep 2026</small>
                                </div>
                                <h4 class="text-white h5 mb-2">PUSSIBER TNI AD</h4>
                                <p class="text-muted small mb-3">
                                    <strong>Nomor:</strong> <code>SERT/36/PUSSIBERAD/IX/2026</code><br>
                                    Apresiasi Dansatlak Penangkalan Siber Pussiberad (Kartika CSIRT) atas kerja sama koordinasi temuan kerentanan dan pelaporan etis.
                                </p>
                            </div>
                            <a href="assets/img/cert_pussiber_tni_ad.png" target="_blank" class="btn btn-sm btn-outline-warning w-100">
                                <i class="bi bi-zoom-in me-1"></i> Buka Piagam TNI AD
                            </a>
                        </article>
                    </div>

                    <!-- 3. JUARA 4 NASIONAL CTF ZERO DAY 2026 - KATEGORI KOMPETISI -->
                    <div class="col-12 col-md-6 col-xl-3">
                        <article class="custom-card card-cyan p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <span class="badge bg-primary text-dark fw-bold"><i class="bi bi-trophy-fill me-1"></i> JUARA 4 NASIONAL</span>
                                    <small class="text-cyan font-mono">28 Jun 2026</small>
                                </div>
                                <h4 class="text-white h5 mb-2">CTF ZERO DAY 2026</h4>
                                <p class="text-muted small mb-3">
                                    <strong>Nomor:</strong> <code>ZD-2026-CHAMP-04</code><br>
                                    Predikat 4th Place Scholar Battle Winner pada kompetisi Capture The Flag (CTF) tingkat nasional yang diselenggarakan DSG & Filkom.
                                </p>
                            </div>
                            <a href="assets/img/cert_zeroday.png" target="_blank" class="btn btn-sm btn-outline-primary w-100">
                                <i class="bi bi-zoom-in me-1"></i> Buka Piagam Juara CTF
                            </a>
                        </article>
                    </div>

                    <!-- 4. CSIRT BMKG - LEMBAGA PEMERINTAH NON-KEMENTERIAN -->
                    <div class="col-12 col-md-6 col-xl-3">
                        <article class="custom-card card-cyan p-4 h-100 d-flex flex-column justify-content-between">
                            <div>
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <span class="badge bg-info text-dark fw-bold"><i class="bi bi-building-check me-1"></i> CSIRT BMKG</span>
                                    <small class="text-cyan font-mono">05 Okt 2026</small>
                                </div>
                                <h4 class="text-white h5 mb-2">BADAN METEOROLOGI (BMKG)</h4>
                                <p class="text-muted small mb-3">
                                    <strong>Nomor:</strong> <code>146/KI.10.05/CSIRT/BMKG</code><br>
                                    Sertifikat apresiasi resmi penemuan & pelaporan kerentanan etis bertanda tangan elektronik BSrE Badan Siber dan Sandi Negara (BSSN).
                                </p>
                            </div>
                            <a href="assets/img/cert_bmkg.png" target="_blank" class="btn btn-sm btn-outline-info w-100">
                                <i class="bi bi-zoom-in me-1"></i> Buka Piagam BMKG
                            </a>
                        </article>
                    </div>
                </div>

                <!-- Detail Biodata & Fokus Keahlian Dinamis dari Database -->
                <div class="row g-4 align-items-center">
                    
                    <!-- Biodata & Pendidikan (tbl_pendidikan & tbl_data_pribadi) -->
                    <div class="col-12 col-lg-6">
                        <div class="custom-card p-4 h-100">
                            <h3 class="h4 text-white mb-3"><i class="bi bi-mortarboard text-cyan me-2"></i> Latar Belakang & Pendidikan</h3>
                            <p class="text-secondary small mb-3">
                                <?= htmlspecialchars($pribadi['tentang_lengkap'], ENT_QUOTES, 'UTF-8') ?>
                            </p>
                            
                            <ul class="list-unstyled mb-0 d-flex flex-column gap-2 small">
                                <li class="d-flex justify-content-between border-bottom pb-2 border-secondary border-opacity-25">
                                    <span class="text-muted"><i class="bi bi-person me-2"></i> Nama Lengkap:</span>
                                    <span class="text-white fw-semibold"><?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?></span>
                                </li>
                                <li class="d-flex justify-content-between border-bottom pb-2 border-secondary border-opacity-25">
                                    <span class="text-muted"><i class="bi bi-card-text me-2"></i> NIM:</span>
                                    <span class="text-cyan font-mono fw-semibold"><?= htmlspecialchars($pribadi['nim'], ENT_QUOTES, 'UTF-8') ?></span>
                                </li>
                                <li class="d-flex justify-content-between border-bottom pb-2 border-secondary border-opacity-25">
                                    <span class="text-muted"><i class="bi bi-book me-2"></i> Program Studi:</span>
                                    <span class="text-white fw-semibold"><?= htmlspecialchars($pribadi['program_studi'], ENT_QUOTES, 'UTF-8') ?> (<?= htmlspecialchars($pribadi['fakultas'], ENT_QUOTES, 'UTF-8') ?>)</span>
                                </li>
                                <li class="d-flex justify-content-between border-bottom pb-2 border-secondary border-opacity-25">
                                    <span class="text-muted"><i class="bi bi-geo-alt me-2"></i> Kampus:</span>
                                    <span class="text-white fw-semibold"><?= htmlspecialchars($pribadi['universitas'], ENT_QUOTES, 'UTF-8') ?></span>
                                </li>
                                <?php foreach ($data_pendidikan as $pend): ?>
                                <li class="d-flex justify-content-between border-bottom pb-2 border-secondary border-opacity-25">
                                    <span class="text-muted"><i class="bi bi-mortarboard-fill me-2"></i> <?= htmlspecialchars($pend['jenjang'], ENT_QUOTES, 'UTF-8') ?>:</span>
                                    <span class="text-cyan fw-semibold"><?= htmlspecialchars($pend['nama_institusi'], ENT_QUOTES, 'UTF-8') ?> (<?= htmlspecialchars($pend['periode'], ENT_QUOTES, 'UTF-8') ?>)</span>
                                </li>
                                <?php endforeach; ?>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- Skill Dinamis dari Database (tbl_skill) -->
                    <div class="col-12 col-lg-6">
                        <div class="custom-card p-4 h-100">
                            <h3 class="h4 text-white mb-3"><i class="bi bi-speedometer2 text-cyan me-2"></i> Tingkat Penguasaan Kompetensi (DB)</h3>
                            
                            <?php foreach ($data_skill as $sk): ?>
                            <div class="mb-3">
                                <div class="d-flex justify-content-between small mb-1">
                                    <span class="text-white"><i class="bi <?= htmlspecialchars($sk['ikon'], ENT_QUOTES, 'UTF-8') ?> text-cyan me-1"></i> <?= htmlspecialchars($sk['nama_skill'], ENT_QUOTES, 'UTF-8') ?></span>
                                    <span class="text-cyan fw-bold"><?= (int)$sk['persentase'] ?>% (<?= htmlspecialchars($sk['level'], ENT_QUOTES, 'UTF-8') ?>)</span>
                                </div>
                                <div class="progress" style="height: 8px;">
                                    <div class="progress-bar bg-info" role="progressbar" style="width: <?= (int)$sk['persentase'] ?>%;" aria-valuenow="<?= (int)$sk['persentase'] ?>" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <?php endforeach; ?>

                        </div>
                    </div>
                </div>
                
            </div>
        </section>

        <!-- 3. BAGIAN PROYEK (PROJECTS - MINIMAL 3 ITEM SESUAI KETENTUAN) -->
        <section id="proyek" class="py-5 bg-darker">
            <div class="container">
                
                <header class="text-center mb-5">
                    <span class="section-tag"><i class="bi bi-briefcase me-1"></i> SHOWCASE KARYA</span>
                    <h2 class="section-title">Portofolio Proyek (Dinamis MySQL)</h2>
                    <p class="section-desc mx-auto">
                        Koleksi implementasi nyata proyek perangkat lunak, automasi kecerdasan buatan, dan piranti pengujian keamanan siber yang diambil langsung dari tabel <code>tbl_portofolio</code>.
                    </p>
                </header>
                
                <div class="row g-4">
                    
                    <!-- Loop Dinamis Proyek dari Database -->
                    <?php foreach ($data_portofolio as $port): ?>
                    <div class="col-12 col-md-6 col-lg-6">
                        <article class="custom-card p-4 project-card">
                            <div>
                                <div class="d-flex align-items-center justify-content-between mb-3">
                                    <div class="project-icon-box">
                                        <i class="bi <?= htmlspecialchars($port['ikon'], ENT_QUOTES, 'UTF-8') ?>"></i>
                                    </div>
                                    <span class="badge bg-<?= htmlspecialchars($port['badge_color'], ENT_QUOTES, 'UTF-8') ?> text-dark fw-bold">
                                        <?= htmlspecialchars($port['badge_text'], ENT_QUOTES, 'UTF-8') ?>
                                    </span>
                                </div>
                                
                                <h3 class="h4 text-white mb-2"><?= htmlspecialchars($port['judul_proyek'], ENT_QUOTES, 'UTF-8') ?></h3>
                                
                                <p class="text-secondary small mb-3">
                                    <?= htmlspecialchars($port['deskripsi'], ENT_QUOTES, 'UTF-8') ?>
                                </p>
                                
                                <div class="mb-3">
                                    <strong class="d-block text-white small mb-2"><i class="bi bi-check-circle-fill text-cyan me-1"></i> Fitur Utama:</strong>
                                    <ul class="text-muted small ps-3 mb-0">
                                        <li><?= htmlspecialchars($port['fitur_1'], ENT_QUOTES, 'UTF-8') ?></li>
                                        <li><?= htmlspecialchars($port['fitur_2'], ENT_QUOTES, 'UTF-8') ?></li>
                                        <li><?= htmlspecialchars($port['fitur_3'], ENT_QUOTES, 'UTF-8') ?></li>
                                    </ul>
                                </div>
                            </div>
                            
                            <div>
                                <div class="mb-3">
                                    <?php 
                                    $tech_list = explode(',', $port['teknologi']);
                                    foreach ($tech_list as $t): 
                                    ?>
                                        <span class="tech-tag"><?= htmlspecialchars(trim($t), ENT_QUOTES, 'UTF-8') ?></span>
                                    <?php endforeach; ?>
                                </div>
                                <a href="<?= htmlspecialchars($port['link_github'], ENT_QUOTES, 'UTF-8') ?>" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-primary w-100">
                                    <i class="bi bi-box-arrow-up-right me-1"></i> Buka Tautan Proyek
                                </a>
                            </div>
                        </article>
                    </div>
                    <?php endforeach; ?>

                </div>
            </div>
        </section>

        <!-- 4. BAGIAN PRESTASI & SERTIFIKASI (ACHIEVEMENTS) -->
        <section id="prestasi" class="py-5">
            <div class="container">
                
                <header class="text-center mb-5">
                    <span class="section-tag"><i class="bi bi-patch-check me-1"></i> DOKUMEN RESMI</span>
                    <h2 class="section-title">Prestasi & Rekapitulasi Sertifikasi</h2>
                    <p class="section-desc mx-auto">
                        Tabel rekapitulasi data piagam penghargaan dan lisensi kompetensi yang terverifikasi secara sah, dimuat dinamis dari tabel <code>tbl_prestasi</code>.
                    </p>
                </header>
                
                <!-- Tabel Rekapitulasi Dinamis Bootstrap 5 -->
                <div class="custom-card p-3 p-md-4 mb-5">
                    <div class="table-responsive">
                        <table class="table custom-table table-hover align-middle mb-0 text-nowrap">
                            <caption class="text-muted small px-2">Rekapitulasi <?= count($data_prestasi) ?> Dokumen Prestasi & Lisensi Resmi <?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?> (Live DB)</caption>
                            <thead>
                                <tr>
                                    <th>No</th>
                                    <th>Tanggal</th>
                                    <th>Nama Prestasi / Sertifikasi</th>
                                    <th>Penyelenggara / Instansi</th>
                                    <th>No. Registrasi Dokumen</th>
                                    <th>Status Verifikasi</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php 
                                $no = 1;
                                foreach ($data_prestasi as $pres): 
                                    $is_mil = !empty($pres['is_militer']);
                                    $is_ctf = strpos($pres['judul_prestasi'], 'Juara 4') !== false;
                                    $row_class = '';
                                    if ($is_mil) {
                                        $row_class = 'table-warning bg-opacity-25';
                                    } elseif ($is_ctf) {
                                        $row_class = 'table-primary bg-opacity-25';
                                    }
                                ?>
                                <tr class="<?= $row_class ?>">
                                    <td class="fw-bold"><?= sprintf("%02d", $no++) ?></td>
                                    <td><?= htmlspecialchars($pres['tanggal'], ENT_QUOTES, 'UTF-8') ?></td>
                                    <td>
                                        <strong class="text-white"><?= htmlspecialchars($pres['judul_prestasi'], ENT_QUOTES, 'UTF-8') ?></strong><br>
                                        <?php if ($is_mil): ?>
                                            <small class="text-warning"><i class="bi bi-shield-fill-check me-1"></i> <strong>Siber Militer & Pertahanan Nasional</strong></small>
                                        <?php elseif ($is_ctf): ?>
                                            <small class="text-cyan"><i class="bi bi-trophy-fill me-1"></i> <strong>Juara 4 Nasional Scholar Battle Winner</strong></small>
                                        <?php else: ?>
                                            <small class="text-cyan"><i class="bi bi-award me-1"></i> <?= htmlspecialchars($pres['kategori'], ENT_QUOTES, 'UTF-8') ?></small>
                                        <?php endif; ?>
                                    </td>
                                    <td><?= htmlspecialchars($pres['penyelenggara'], ENT_QUOTES, 'UTF-8') ?></td>
                                    <td><code><?= htmlspecialchars($pres['no_registrasi'], ENT_QUOTES, 'UTF-8') ?></code></td>
                                    <td><span class="badge <?= htmlspecialchars($pres['badge_class'], ENT_QUOTES, 'UTF-8') ?>"><?= htmlspecialchars($pres['status_verifikasi'], ENT_QUOTES, 'UTF-8') ?></span></td>
                                </tr>
                                <?php endforeach; ?>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- Galeri Kartu Visual Teratas (Dinamis dari is_featured = 1) -->
                <div class="row g-4">
                    <?php foreach ($data_featured as $feat): ?>
                    <div class="col-12 col-sm-6 col-lg-3">
                        <article class="custom-card h-100 overflow-hidden d-flex flex-column justify-content-between">
                            <div>
                                <img src="<?= htmlspecialchars($feat['gambar_piagam'], ENT_QUOTES, 'UTF-8') ?>" alt="<?= htmlspecialchars($feat['judul_prestasi'], ENT_QUOTES, 'UTF-8') ?>" class="img-fluid w-100" style="height: 180px; object-fit: cover;">
                                <div class="p-3">
                                    <span class="badge <?= htmlspecialchars($feat['badge_class'], ENT_QUOTES, 'UTF-8') ?> mb-2"><?= htmlspecialchars($feat['penyelenggara'], ENT_QUOTES, 'UTF-8') ?></span>
                                    <h5 class="text-white h6 mb-1"><?= htmlspecialchars($feat['judul_prestasi'], ENT_QUOTES, 'UTF-8') ?></h5>
                                    <p class="text-muted small mb-0">No: <?= htmlspecialchars($feat['no_registrasi'], ENT_QUOTES, 'UTF-8') ?></p>
                                </div>
                            </div>
                            <div class="p-3 pt-0">
                                <a href="<?= htmlspecialchars($feat['gambar_piagam'], ENT_QUOTES, 'UTF-8') ?>" target="_blank" class="btn btn-sm btn-outline-primary w-100">
                                    <i class="bi bi-eye me-1"></i> Buka Resolusi Penuh
                                </a>
                            </div>
                        </article>
                    </div>
                    <?php endforeach; ?>
                </div>

            </div>
        </section>

        <!-- 5. BAGIAN KONTAK (CONTACT) -->
        <section id="kontak" class="py-5 bg-darker">
            <div class="container">
                
                <header class="text-center mb-5">
                    <span class="section-tag"><i class="bi bi-chat-dots me-1"></i> HUBUNGI SAYA</span>
                    <h2 class="section-title">Inisialisasi Komunikasi & Kolaborasi</h2>
                    <p class="section-desc mx-auto">
                        Terbuka untuk diskusi mengenai riset keamanan siber etis, pengembangan agen AI, koordinasi tim CTF, maupun keperluan akademik.
                    </p>
                </header>
                
                <div class="row g-4 justify-content-center">
                    
                    <!-- Informasi Kontak Langsung (Dinamis dari tbl_kontak) -->
                    <div class="col-12 col-lg-5">
                        <aside class="custom-card card-cyan p-4 h-100">
                            <h3 class="h4 text-white mb-3">Saluran Kontak Resmi</h3>
                            <p class="text-secondary small mb-4">
                                Silakan hubungi langsung melalui media kontak resmi di bawah ini (Data dari tabel <code>tbl_kontak</code>):
                            </p>
                            
                            <div class="d-flex flex-column gap-3 mb-4">
                                <?php foreach ($data_kontak as $ktk): ?>
                                <div class="d-flex align-items-center gap-3">
                                    <div class="project-icon-box mb-0 flex-shrink-0" style="width: 42px; height: 42px; font-size: 1.15rem;">
                                        <i class="bi <?= htmlspecialchars($ktk['ikon'], ENT_QUOTES, 'UTF-8') ?>"></i>
                                    </div>
                                    <div>
                                        <small class="text-muted d-block"><?= htmlspecialchars($ktk['label'], ENT_QUOTES, 'UTF-8') ?>:</small>
                                        <?php if ($ktk['jenis'] === 'Lokasi'): ?>
                                            <span class="text-white fw-semibold small"><?= htmlspecialchars($ktk['nilai'], ENT_QUOTES, 'UTF-8') ?></span>
                                        <?php else: ?>
                                            <a href="<?= htmlspecialchars($ktk['tautan'], ENT_QUOTES, 'UTF-8') ?>" target="_blank" rel="noopener noreferrer" class="text-white text-decoration-none fw-semibold small">
                                                <?= htmlspecialchars($ktk['nilai'], ENT_QUOTES, 'UTF-8') ?>
                                            </a>
                                        <?php endif; ?>
                                    </div>
                                </div>
                                <?php endforeach; ?>
                            </div>
                            
                            <!-- SLA Response Table -->
                            <div class="border-top border-secondary border-opacity-25 pt-3">
                                <h4 class="h6 text-cyan mb-2"><i class="bi bi-clock-history me-1"></i> Estimasi Respons Komunikasi:</h4>
                                <table class="table table-sm table-bordered custom-table small mb-0">
                                    <tbody>
                                        <tr>
                                            <td class="text-muted">Pelaporan Kerentanan / CSIRT</td>
                                            <td class="text-success fw-bold text-end">Prioritas (&lt; 12 Jam)</td>
                                        </tr>
                                        <tr>
                                            <td class="text-muted">Koordinasi Akademik & Proyek</td>
                                            <td class="text-white text-end">1 x 24 Jam</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </aside>
                    </div>
                    
                    <!-- Formulir Kontak PHP & MySQL (Menyimpan ke tbl_pesan) -->
                    <div class="col-12 col-lg-7">
                        <div class="custom-card p-4 h-100">
                            <h3 class="h4 text-white mb-2">Formulir Pesan Interaktif (PHP & MySQL)</h3>
                            <p class="text-secondary small mb-4">
                                Silakan tinggalkan pesan. Data yang diisi akan divalidasi dan disimpan secara permanen ke tabel <code>tbl_pesan</code> menggunakan prepared statement PDO:
                            </p>
                            
                            <!-- Notifikasi Alert Hasil Submit PHP -->
                            <?php if ($pesan_alert === 'sukses'): ?>
                                <div class="alert alert-success alert-dismissible fade show" role="alert">
                                    <i class="bi bi-check-circle-fill me-2"></i>
                                    <strong>Pesan Berhasil Terkirim!</strong> Data Anda telah tersimpan secara aman ke database MySQL (<code>tbl_pesan</code>).
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                </div>
                            <?php elseif ($pesan_alert === 'error'): ?>
                                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                                    <i class="bi bi-exclamation-triangle-fill me-2"></i>
                                    <strong>Gagal Mengirim Pesan!</strong> Terjadi kendala saat menyimpan ke database MySQL.
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                </div>
                            <?php elseif ($pesan_alert === 'kosong'): ?>
                                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                                    <i class="bi bi-exclamation-circle-fill me-2"></i>
                                    <strong>Mohon Lengkapi Data!</strong> Kolom Nama, Email, dan Pesan wajib diisi.
                                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                                </div>
                            <?php endif; ?>
                            
                            <form action="index.php#kontak" method="POST" class="needs-validation">
                                <input type="hidden" name="kirim_pesan" value="1">
                                <div class="row g-3">
                                    
                                    <!-- Input Nama -->
                                    <div class="col-12 col-md-6">
                                        <div class="form-floating">
                                            <input type="text" class="form-control" id="contactNama" name="nama" placeholder="Nama Lengkap" required>
                                            <label for="contactNama">Nama Lengkap *</label>
                                        </div>
                                    </div>
                                    
                                    <!-- Input Email -->
                                    <div class="col-12 col-md-6">
                                        <div class="form-floating">
                                            <input type="email" class="form-control" id="contactEmail" name="email" placeholder="nama@email.com" required>
                                            <label for="contactEmail">Alamat Email *</label>
                                        </div>
                                    </div>
                                    
                                    <!-- Input Subjek -->
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <input type="text" class="form-control" id="contactSubject" name="subjek" placeholder="Subjek Pesan" required>
                                            <label for="contactSubject">Subjek / Topik Diskusi *</label>
                                        </div>
                                    </div>
                                    
                                    <!-- Textarea Pesan -->
                                    <div class="col-12">
                                        <div class="form-floating">
                                            <textarea class="form-control" placeholder="Pesan Anda" id="contactMessage" name="pesan" style="height: 130px;" required></textarea>
                                            <label for="contactMessage">Isi Pesan atau Agenda Kolaborasi *</label>
                                        </div>
                                    </div>
                                    
                                    <!-- Checkbox Etis -->
                                    <div class="col-12">
                                        <div class="form-check small text-muted">
                                            <input class="form-check-input" type="checkbox" id="checkEtika" required checked>
                                            <label class="form-check-label" for="checkEtika">
                                                Saya menyetujui pengiriman pesan ini untuk koordinasi yang etis dan bermanfaat.
                                            </label>
                                        </div>
                                    </div>
                                    
                                    <!-- Submit & Reset Buttons -->
                                    <div class="col-12 d-flex gap-2 btn-group-responsive">
                                        <button type="submit" class="btn btn-primary px-4 py-2 flex-grow-1">
                                            <i class="bi bi-send-fill me-1"></i> Simpan & Kirim Pesan (POST MySQL)
                                        </button>
                                        <button type="reset" class="btn btn-outline-secondary px-3 py-2">
                                            <i class="bi bi-arrow-counterclockwise me-1"></i> Reset
                                        </button>
                                    </div>
                                    
                                </div>
                            </form>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>

    </main>

    <!-- ==========================================
         SEMANTIC FOOTER
         ========================================== -->
    <footer class="py-4 border-top border-secondary border-opacity-25 bg-black">
        <div class="container text-center">
            <div class="d-flex flex-wrap justify-content-between align-items-center gap-3">
                <div class="text-start">
                    <p class="mb-0 text-white fw-semibold small">
                        &copy; <?= date('Y') ?> <?= htmlspecialchars($pribadi['nama_lengkap'], ENT_QUOTES, 'UTF-8') ?>. All rights reserved.
                    </p>
                    <p class="mb-0 text-muted small" style="font-size: 0.8rem;">
                        Tugas Pemrograman Web (Kelas A) - <strong><?= htmlspecialchars($pribadi['universitas'], ENT_QUOTES, 'UTF-8') ?></strong> | Terkoneksi Database MySQL (PDO)
                    </p>
                </div>
                
                <ul class="nav gap-2">
                    <li class="nav-item"><a href="#beranda" class="nav-link px-2 text-muted small">Beranda</a></li>
                    <li class="nav-item"><a href="#tentang" class="nav-link px-2 text-muted small">Tentang Saya</a></li>
                    <li class="nav-item"><a href="#proyek" class="nav-link px-2 text-muted small">Proyek</a></li>
                    <li class="nav-item"><a href="#prestasi" class="nav-link px-2 text-muted small">Prestasi</a></li>
                    <li class="nav-item"><a href="#kontak" class="nav-link px-2 text-muted small">Kontak</a></li>
                </ul>
            </div>
        </div>
    </footer>

    <!-- Bootstrap 5.3.3 Bundle with Popper JS CDN -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

</body>
</html>
