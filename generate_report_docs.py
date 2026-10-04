# -*- coding: utf-8 -*-
"""
Script Generator Laporan Tugas Pemrograman Web (Format DOCX)
Penulis: Muhammad Jawsyan
Mata Kuliah: Pemrograman Web (Kelas A) - Universitas Paramadina
Dosen: Rahmad Syalevi, S. Kom., M.T.I
"""

import os
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Set background color of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tc_pr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner margins of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tc_pr.append(tc_mar)

def add_code_block(doc, code_text):
    """Add a shaded code block paragraph."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.right_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    
    # Border & shading via XML
    p_pr = p._p.get_or_add_pPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
    p_pr.append(shd)
    
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    return p

def add_callout(doc, title, text, border_color="008080"):
    """Add a callout box."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tc_pr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    run_t = p.add_run(title)
    run_t.font.name = 'Segoe UI'
    run_t.font.size = Pt(10.5)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(15, 23, 42)
    
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    run_b = p2.add_run(text)
    run_b.font.name = 'Segoe UI'
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = RGBColor(51, 65, 85)

def build_report():
    doc = Document()
    
    # Page Margins: 1 inch (Normal)
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
    # Styles Setup
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Segoe UI'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = RGBColor(30, 41, 59) # Slate 800
    normal_style.paragraph_format.line_spacing = 1.2
    normal_style.paragraph_format.space_after = Pt(5)

    # -------------------------------------------------------------
    # COVER / HEADER LAPORAN
    # -------------------------------------------------------------
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(20)
    title_p.paragraph_format.space_after = Pt(4)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = title_p.add_run("UNIVERSITAS PARAMADINA\nFAKULTAS ILMU REKAYASA - PROGRAM STUDI TEKNIK INFORMATIKA\n")
    r_uni.font.name = 'Segoe UI'
    r_uni.font.size = Pt(12)
    r_uni.font.bold = True
    r_uni.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    p_main_title = doc.add_paragraph()
    p_main_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main_title.paragraph_format.space_after = Pt(8)
    r_main = p_main_title.add_run("LAPORAN TUGAS INDIVIDU PEMROGRAMAN WEB\n")
    r_main.font.name = 'Segoe UI'
    r_main.font.size = Pt(16)
    r_main.font.bold = True
    r_main.font.color.rgb = RGBColor(14, 116, 144) # Cyan 700

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(25)
    r_sub = p_sub.add_run("Pengembangan Website Portofolio Pribadi Multi-Halaman\nMurni Komponen HTML5 & CSS3 (Tanpa Framework/Template)\nTopik: Keamanan Siber & Artificial Intelligence")
    r_sub.font.name = 'Segoe UI'
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(71, 85, 105)

    # Metadata Box Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.columns[0].width = Inches(2.2)
    meta_table.columns[1].width = Inches(4.3)
    
    meta_data = [
        ("Mata Kuliah", "Pemrograman Web (Kelas A)"),
        ("Dosen Pengampu", "Rahmad Syalevi, S. Kom., M.T.I"),
        ("Nama Mahasiswa", "Muhammad Jawsyan"),
        ("Program Studi", "S1 Teknik Informatika"),
        ("Tahun Akademik", "2026/2027 Ganjil (Batas Pengumpulan: 7 Okt 2026)"),
        ("Tautan Publikasi", "Live: https://j12k14a.github.io/portfolio-jawsyan-htmlcss/\nGitHub: https://github.com/j12k14a/portfolio-jawsyan-htmlcss")
    ]
    
    for idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(10)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.size = Pt(10)

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB I: PENDAHULUAN & PROFIL SISTEM
    # -------------------------------------------------------------
    h1 = doc.add_heading("BAB I: PENDAHULUAN & GAMBARAN UMUM SISTEM", level=1)
    h1.style.font.name = 'Segoe UI'
    h1.style.font.color.rgb = RGBColor(14, 116, 144)

    p = doc.add_paragraph()
    p.add_run("1.1 Latar Belakang & Tujuan Penugasan\n").bold = True
    p.add_run(
        "Tugas individu pada mata kuliah Pemrograman Web (Kelas A) di Universitas Paramadina ini bertujuan untuk menguji "
        "dan memvalidasi pemahaman mahasiswa mengenai fondasi inti rekayasa web berbasis standar World Wide Web Consortium (W3C), "
        "yakni HyperText Markup Language versi 5 (HTML5) dan Cascading Style Sheets level 3 (CSS3). "
        "Secara khusus, dosen pengampu menetapkan syarat mutlak bahwa implementasi website tidak boleh menggunakan framework "
        "CSS (seperti Bootstrap, Tailwind CSS, Bulma) maupun template siap pakai apapun. Seluruh komponen tampilan, tata letak antarmuka, "
        "dan hierarki dokumen harus ditulis secara mandiri dari awal (from scratch)."
    )

    p = doc.add_paragraph()
    p.add_run("1.2 Profil Personal & Arah Portofolio\n").bold = True
    p.add_run(
        "Website portofolio ini dibangun untuk merepresentasikan profil profesional Muhammad Jawsyan, seorang mahasiswa Teknik Informatika "
        "Universitas Paramadina yang aktif menggeluti bidang Keamanan Siber (Cybersecurity), khususnya Offensive Security / Red Team, "
        "Responsible Vulnerability Disclosure (Bug Bounty), serta rekayasa Artificial Intelligence (AI Agent). "
        "Portofolio ini secara khusus menonjolkan pencapaian predikat penghargaan bergengsi terbaru, antara lain:\n"
    )
    p_b1 = doc.add_paragraph(style='List Bullet')
    p_b1.add_run("Sertifikat Apresiasi dari PUSSIBER TNI ANGKATAN DARAT (Kartika CSIRT) ").bold = True
    p_b1.add_run("Nomor SERT/36/PUSSIBERAD/KARTIKA-CSIRT/IX/2026 atas kerja sama koordinasi temuan kerentanan dan pelaporan secara etis.")
    
    p_b2 = doc.add_paragraph(style='List Bullet')
    p_b2.add_run("Sertifikat Apresiasi dari Badan Siber Sandi dan Aplikasi (BSSA) Diskominfotik Pemprov DKI Jakarta ").bold = True
    p_b2.add_run("Nomor 113/BUG/BSSA/VIII/2026 atas kontribusi penemuan dan pelaporan kerentanan pada sistem elektronik pemerintah.")
    
    p_b3 = doc.add_paragraph(style='List Bullet')
    p_b3.add_run("Juara 4 (4th Place Scholar Battle Winner) ").bold = True
    p_b3.add_run("dalam kompetisi nasional Capture The Flag (CTF) - ZERO DAY 2026.")

    p = doc.add_paragraph()
    p.add_run("1.3 Filosofi & Konsep Desain (Terinspirasi iPortfolio)\n").bold = True
    p.add_run(
        "Sebagai acuan desain antarmuka, tugas ini mengadaptasi prinsip estetika dan tata letak dari demo iPortfolio (BootstrapMade), "
        "namun direkayasa ulang 100% menggunakan CSS murni (Native CSS Grid dan Flexbox). Desain mengadopsi struktur sidebar vertikal di sebelah kiri "
        "yang memuat foto profil, ringkasan identitas, menu navigasi berikon, serta tautan jejaring profesional. "
        "Area konten utama di sebelah kanan mengusung palet warna gelap modern (Cyber Theme / Dark Slate) yang nyaman dipandang, elegan, "
        "dan mencerminkan identitas dunia keamanan siber profesional."
    )

    # -------------------------------------------------------------
    # BAB II: MATRIKS EVALUASI & PEMENUHAN SELURUH SYARAT TUGAS
    # -------------------------------------------------------------
    h2 = doc.add_heading("BAB II: MATRIKS EVALUASI & PEMENUHAN SYARAT TUGAS", level=1)
    h2.style.font.name = 'Segoe UI'
    h2.style.font.color.rgb = RGBColor(14, 116, 144)

    p = doc.add_paragraph(
        "Berikut adalah tabel evaluasi komprehensif yang membuktikan bahwa seluruh instruksi dan kriteria penugasan yang tercantum "
        "pada sistem pembelajaran Edlink telah terpenuhi 100% tanpa ada satu pun yang terlewatkan:"
    )

    eval_table = doc.add_table(rows=14, cols=4)
    eval_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    eval_table.columns[0].width = Inches(0.5)
    eval_table.columns[1].width = Inches(1.8)
    eval_table.columns[2].width = Inches(2.2)
    eval_table.columns[3].width = Inches(2.0)

    eval_headers = ["No", "Ketentuan Tugas Dosen", "Implementasi Nyata pada Proyek", "Bukti Berkas & Lokasi Kode"]
    for i, title in enumerate(eval_headers):
        cell = eval_table.cell(0, i)
        set_cell_background(cell, "0E7490")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        r = p.add_run(title)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    eval_rows = [
        ("1", "Minimal 3 Halaman & Menu Navigasi", "Membangun 4 halaman terhubung penuh:\n• index.html (Home/About)\n• skills.html (Skills/Experience)\n• achievements.html (Tabel & Galeri)\n• contact.html (Kontak & SLA)", "Tag <nav> & <ul class='nav-menu'> dengan penanda kelas 'active' di seluruh file HTML"),
        ("2", "Memiliki Elemen Table (Tabel)", "Diterapkan di 3 tempat:\n1. Tabel Biodata Akademik (index.html)\n2. Tabel Rekap 11 Sertifikat (achievements.html)\n3. Tabel Respons SLA (contact.html)", "Tag <table>, <caption>, <thead>, <tbody>, <tfoot>, <tr>, <th>, <td> di index.html, achievements.html, contact.html"),
        ("3", "Memiliki Elemen Image (Gambar)", "Menyajikan foto profil lingkaran, 3 foto dokumentasi kegiatan lomba CTF, serta 11 gambar sertifikat piagam asli resolusi tinggi.", "Tag <img> dan <figure> dengan atribut alt, src, class di assets/img/"),
        ("4", "Memiliki Elemen Link (Tautan)", "Navigasi internal antar 4 halaman, link unduh berkas PDF sertifikat, link eksternal LinkedIn, GitHub, blog, mailto: dan tel:.", "Tag <a href='...'>, target='_blank', rel='noopener noreferrer', mailto:, tel:"),
        ("5", "Memiliki Elemen List (Daftar)", "Menerapkan 3 jenis list lengkap:\n• Unordered list <ul>\n• Ordered list <ol>\n• Definition list <dl>", "• <ul>: Daftar keahlian & menu\n• <ol>: 5 Tahapan Prosedur SOP\n• <dl>, <dt>, <dd>: Glosarium istilah siber"),
        ("6", "Memiliki Elemen Form (Formulir)", "Formulir pencarian dan filter database arsip sertifikat terstruktur pada achievements.html.", "Tag <form action='#' method='GET'> di achievements.html"),
        ("7", "Memiliki Elemen Input (Masukan)", "Menyediakan input pencarian kata kunci tipe search serta dropdown filter select.", "Tag <input type='search'> dan <select><option> di achievements.html"),
        ("8", "Memiliki Elemen Button (Tombol)", "Menyediakan tombol submit untuk eksekusi pencarian dan tombol reset untuk pembersihan form.", "Tag <button type='submit'> dan <button type='reset'> di achievements.html"),
        ("9", "Menerapkan CSS Eksternal", "Stylesheet global terpadu yang memuat variabel tema, reset, tipografi, flexbox, dan grid.", "File assets/css/style.css dihubungkan via <link rel='stylesheet'> di semua halaman"),
        ("10", "Menerapkan CSS Internal", "Tag <style> khusus di dalam <head> pada masing-masing dokumen HTML untuk aturan unik per halaman.", "Tag <style>...</style> di <head> pada index.html, skills.html, achievements.html, contact.html"),
        ("11", "Menerapkan CSS Inline", "Atribut style='...' langsung pada elemen HTML tertentu untuk membuktikan penguasaan inline style.", "Contoh: style='width: 92%;' pada skill bar, style='background: #10b981;' pada badge verifikasi"),
        ("12", "Struktur Dokumen HTML5", "Menggunakan standar deklarasi semantik HTML5 modern secara menyeluruh.", "<!DOCTYPE html>, <header>, <nav>, <main>, <section>, <article>, <aside>, <footer>"),
        ("13", "Tanpa Framework / Template", "100% Vanilla HTML5 & CSS3 buatan tangan sendiri tanpa Bootstrap, Tailwind, atau library JS.", "Murni kode native tanpa skrip CDN eksternal")
    ]

    for row_idx, rdata in enumerate(eval_rows):
        row = eval_table.rows[row_idx + 1]
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx in range(4):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            r = p.add_run(rdata[col_idx])
            r.font.size = Pt(8.5)
            if col_idx == 0 or col_idx == 1:
                r.font.bold = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB III: PENJELASAN MENDALAM SELURUH SYNTAX HTML5
    # -------------------------------------------------------------
    h3 = doc.add_heading("BAB III: PENJELASAN LENGKAP SELURUH SYNTAX HTML5", level=1)
    h3.style.font.name = 'Segoe UI'
    h3.style.font.color.rgb = RGBColor(14, 116, 144)

    p = doc.add_paragraph(
        "Bab ini mengupas secara mendalam seluruh tag, elemen, dan atribut HTML5 yang digunakan dalam proyek portofolio "
        "tanpa ada satu pun syntax yang terlewatkan. Setiap elemen dijelaskan fungsi semantik, peran teknis, serta contoh kodenya "
        "yang diambil langsung dari repositori proyek."
    )

    # 3.1 Metadata & Struktur Dasar
    doc.add_heading("3.1 Tag Deklarasi Dokumen & Metadata Kepala (<head>)", level=2)
    
    html_meta_tags = [
        ("<!DOCTYPE html>", "Document Type Declaration", "Mendeklarasikan kepada browser bahwa dokumen ini mematuhi standar spesifikasi HTML5 modern (HTML living standard). Tag ini wajib diletakkan di baris paling pertama dokumen."),
        ("<html>", "Root Element", "Elemen akar pembungkus seluruh konten web. Diberikan atribut lang='id' untuk mendeklarasikan bahasa utama halaman (Bahasa Indonesia) demi aksesibilitas pembaca layar (screen reader) dan SEO."),
        ("<head>", "Document Metadata Container", "Wadah tempat menyimpan instruksi teknis yang tidak tampil secara visual di jendela utama browser, mencakup character encoding, viewport seluler, deskripsi meta, judul, dan link ke stylesheet."),
        ("<meta charset='UTF-8'>", "Character Encoding Metadata", "Menetapkan sistem pengkodean karakter standar internasional UTF-8 sehingga teks web mendukung seluruh alfabet Latin, simbol siber, tanda baca khusus, hingga emotikon."),
        ("<meta name='viewport' content='width=device-width, initial-scale=1.0'>", "Responsive Viewport", "Menginstruksikan mesin peramban seluler (smartphone dan tablet) agar merender lebar halaman sesuai lebar fisik layar perangkat (device-width) dengan rasio perbesaran awal 1:1."),
        ("<meta name='description'>", "SEO Description Metadata", "Menyediakan ringkasan konten halaman untuk ditampilkan oleh mesin pencari Google pada cuplikan hasil pencarian (search snippet)."),
        ("<meta name='author'>", "Author Metadata", "Mendokumentasikan identitas pembuat dokumen web (Muhammad Jawsyan)."),
        ("<title>", "Document Title Tag", "Menentukan teks judul yang muncul pada tab jendela peramban dan penanda riwayat bookmark pengguna."),
        ("<link rel='stylesheet' href='assets/css/style.css'>", "External Stylesheet Link", "Menghubungkan dokumen HTML dengan file CSS eksternal terpisah. Ini merupakan implementasi dari CSS Eksternal yang disyaratkan tugas."),
        ("<style>", "Internal Stylesheet Container", "Tag khusus tempat meletakkan blok aturan CSS Internal langsung di dalam dokumen HTML untuk mengatur tampilan unik halaman tersebut."),
        ("<body>", "Document Body Container", "Elemen pembungkus seluruh materi visual yang akan ditampilkan kepada pengguna di jendela peramban.")
    ]

    for tag, name, desc in html_meta_tags:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.15)
        r_t = p.add_run(f"• {tag} ({name})\n")
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(14, 116, 144)
        p.add_run(desc)

    # 3.2 Tag Semantik Tata Letak
    doc.add_heading("3.2 Tag Semantik Tata Letak Dokumen (HTML5 Semantic Layout)", level=2)
    p_sem = doc.add_paragraph(
        "Berbeda dengan HTML4 lama yang menggunakan <div> generik untuk semua tata letak, HTML5 memperkenalkan elemen semantik "
        "yang memiliki makna struktural jelas bagi peramban, mesin pencari, dan teknologi bantu disabilitas (Accessibility):"
    )

    html_layout_tags = [
        ("<header class='sidebar'>", "Header / Banner Navigasi", "Digunakan sebagai panel sidebar kiri permanen yang membungkus identitas utama portofolio: avatar pengguna, nama profil, profesi, menu navigasi, dan informasi akademik."),
        ("<nav>", "Navigation Container", "Menandai area navigasi utama situs yang memuat daftar tautan menu antar halaman web."),
        ("<main class='main-content'>", "Main Content Area", "Menandai area utama dokumen yang memuat materi inti dan unik dari halaman tersebut. Elemen <main> tidak boleh memuat konten yang berulang antar halaman seperti sidebar dan footer."),
        ("<section>", "Sectioning Element", "Membagi dokumen ke dalam blok-blok bagian yang memiliki tema atau judul spesifik, seperti Hero Section, Section Biodata, Section Galeri, dan Section Matriks Keahlian."),
        ("<article>", "Self-Contained Content", "Digunakan untuk mengelompokkan konten yang mandiri dan dapat berdiri sendiri, seperti kartu sertifikat (<article class='cert-card'>) dan kelompok modul keahlian."),
        ("<aside>", "Complementary Content", "Menampung informasi pelengkap atau sekunder yang berkaitan dengan konten utama, seperti kotak glosarium definisi dan daftar ringkasan tautan cepat."),
        ("<footer>", "Footer Container", "Menandai bagian kaki halaman yang memuat hak cipta (&copy; 2026), informasi legalitas, dan navigasi pelengkap.")
    ]

    for tag, name, desc in html_layout_tags:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.15)
        r_t = p.add_run(f"• {tag} ({name})\n")
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(15, 23, 42)
        p.add_run(desc)

    # 3.3 Tag Pengelompokan & List
    doc.add_heading("3.3 Tag Pengelompokan Daftar (List Elements: ul, ol, dl)", level=2)
    p = doc.add_paragraph("Proyek ini menerapkan seluruh 3 ragam elemen list yang disediakan oleh standar HTML5:")
    
    add_callout(doc, "1. Unordered List (<ul> & <li>)", 
                "Digunakan pada menu navigasi (<ul class='nav-menu'>) dan daftar kompetensi teknis (<ul class='list-styled'>). "
                "Secara default menghasilkan poin-poin bullet yang kemudian di-custom menggunakan CSS pseudo-element ::before berbentuk panah siber (▹).", "0E7490")
    
    add_callout(doc, "2. Ordered List (<ol> & <li>)", 
                "Digunakan pada halaman skills.html untuk menyajikan '5 Tahapan Prosedur Pelaporan Kerentanan Etis (Ethical Disclosure SOP)'. "
                "Elemen ini menghasilkan urutan numerik berangka (1, 2, 3...) yang menunjukkan alur proses metodologis berurutan.", "F59E0B")
    
    add_callout(doc, "3. Definition List (<dl>, <dt>, & <dd>)", 
                "Digunakan pada glosarium istilah siber di skills.html. Tag <dl> membungkus daftar definisi, <dt> (definition term) menandai istilah "
                "(seperti CSIRT, Red Team, Zero-Day), dan <dd> (definition description) memuat penjelasan detail istilah tersebut.", "10B981")

    # 3.4 Tag Tabel Data
    doc.add_heading("3.4 Tag Tabel Data (Table Elements)", level=2)
    p = doc.add_paragraph(
        "Tabel data dibangun dengan kepatuhan semantik penuh untuk mengorganisasi informasi multidimensi secara terstruktur:"
    )

    html_table_tags = [
        ("<table>", "Wadah utama pembentuk tabel tabular."),
        ("<caption>", "Memberikan judul resmi dan deskripsi tabel yang dibaca pertama kali oleh pembaca layar tunanetra (contoh: 'Tabel Rekapitulasi Prestasi, Apresiasi & Sertifikasi Resmi')."),
        ("<thead>", "Membungkus baris kepala kolom (header) yang mendefinisikan nama-nama variabel kolom."),
        ("<tbody>", "Membungkus baris-baris data inti isi tabel."),
        ("<tfoot>", "Membungkus baris ringkasan atau kesimpulan di bagian paling bawah tabel (contoh: total rekap 11 sertifikat sah)."),
        ("<tr>", "Table Row — Mendefinisikan baris horizontal tabel."),
        ("<th>", "Table Header — Sel kepala kolom yang secara default ditebalkan dan ditengahkan oleh peramban."),
        ("<td>", "Table Data — Sel penampung data nilai tabel."),
        ("colspan='4'", "Atribut penggabungan kolom horizontal pada <tfoot> untuk menyatukan beberapa sel menjadi satu baris kesimpulan.")
    ]

    for tag, desc in html_table_tags:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.15)
        r_t = p.add_run(f"• {tag} : ")
        r_t.font.bold = True
        p.add_run(desc)

    # 3.5 Form, Input, Button
    doc.add_heading("3.5 Tag Formulir, Masukan & Tombol (Form, Input, Button)", level=2)
    p = doc.add_paragraph(
        "Sesuai rubrik wajib penugasan, elemen form diimplementasikan pada halaman achievements.html sebagai fitur pencarian "
        "dan filter data sertifikat interaktif:"
    )

    html_form_tags = [
        ("<form action='#' method='GET'>", "Mendefinisikan formulir interaktif dengan metode pengiriman data GET untuk operasi pencarian arsip."),
        ("<input type='search' name='keyword'>", "Elemen masukan khusus untuk pencarian teks kata kunci yang memiliki fitur pembersihan instan bawaan peramban."),
        ("<select name='kategori'> & <option>", "Menu dropdown pilihan kategori filter (Semua, Predikat Khusus, Kompetisi CTF, MOOC SEVIMA, Global)."),
        ("<button type='submit'>", "Tombol pengiriman formulir (Cari Arsip) yang memicu event submit pencarian."),
        ("<button type='reset'>", "Tombol pembersih formulir yang mengembalikan seluruh input ke kondisi semula.")
    ]

    for tag, desc in html_form_tags:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.15)
        r_t = p.add_run(f"• {tag} : ")
        r_t.font.bold = True
        p.add_run(desc)

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB IV: PENJELASAN MENDALAM SELURUH SYNTAX CSS3
    # -------------------------------------------------------------
    h4 = doc.add_heading("BAB IV: PENJELASAN LENGKAP SELURUH SYNTAX CSS3", level=1)
    h4.style.font.name = 'Segoe UI'
    h4.style.font.color.rgb = RGBColor(14, 116, 144)

    p = doc.add_paragraph(
        "Cascading Style Sheets (CSS3) pada proyek ini dibangun secara modular, terstruktur, dan murni tanpa bantuan framework "
        "ataupun preprocessor. Bab ini menguraikan ketiga metode styling yang disyaratkan serta seluruh properti CSS yang digunakan."
    )

    # 4.1 Tiga Metode Penerapan CSS
    doc.add_heading("4.1 Implementasi Tiga Metode CSS (Eksternal, Internal, Inline)", level=2)
    
    add_callout(doc, "A. CSS Eksternal (assets/css/style.css)", 
                "Dihubungkan via <link rel='stylesheet' href='assets/css/style.css'> pada seluruh file HTML. "
                "Berisi aturan arsitektur global, CSS Variables (:root), CSS Reset, typography skala, tata letak sidebar desktop & mobile, "
                "sistem kartu glassmorphism, tombol utama, dan breakpoints responsive design. Metode ini mengoptimalkan pemisahan struktur (HTML) dan presentasi (CSS) serta memanfaatkan browser caching.", "0E7490")

    add_callout(doc, "B. CSS Internal (<style> di dalam <head>)", 
                "Diterapkan di setiap halaman HTML untuk styling modular khusus. Contohnya:\n"
                "• index.html: Mengatur efek radial glow .hero-banner dan styling .biodata-table.\n"
                "• skills.html: Mengatur tata letak .skills-matrix dan styling grid glosarium .glossary-dl.\n"
                "• achievements.html: Mengatur dekorasi zebra table .achieve-table dan grid galeri kartu.\n"
                "• contact.html: Mengatur lebar kontainer .contact-layout dan tabel SLA.", "3B82F6")

    add_callout(doc, "C. CSS Inline (Atribut style='...')", 
                "Diterapkan langsung pada tag HTML tertentu untuk mendemonstrasikan penguasaan penimpaan aturan spesifisitas inline. Contohnya:\n"
                "• skills.html: style='width: 92%;' pada skill bar untuk menetapkan nilai progres dinamis.\n"
                "• achievements.html: style='background-color: #10b981; color: #fff; padding: 4px 10px; border-radius: 4px;' untuk badge status terverifikasi sah.\n"
                "• index.html: style='box-shadow: 0 4px 15px rgba(0, 242, 254, 0.4);' untuk efek pendaran tombol hero.", "F59E0B")

    # 4.2 Properti-Properti CSS Lengkap
    doc.add_heading("4.2 Rincian Properti CSS3 Berdasarkan Kategori Fungsional", level=2)

    css_categories = [
        ("1. CSS Variables & Custom Properties", [
            (":root", "Pseudo-class akar dokumen yang digunakan untuk mendefinisikan variabel global agar konsisten dan mudah diatur."),
            ("--primary: #00f2fe", "Variabel warna primer (Neon Cyan) untuk identitas aksen keamanan siber."),
            ("--bg-body: #090d16", "Variabel warna latar belakang utama berupa palet Deep Dark Slate."),
            ("--bg-sidebar: #050811", "Variabel warna sidebar kiri bertema True Dark Navy."),
            ("var(--primary)", "Fungsi pemanggil nilai variabel pada selektor CSS manapun.")
        ]),
        ("2. Box Model, Sizing & Display", [
            ("box-sizing: border-box", "Menetapkan model kotak di mana padding dan border dihitung di dalam dimensi total elemen, mencegah overflow layout tak terkendali."),
            ("margin & padding", "Mengatur spasi luar (margin) dan bantalan dalam (padding) antar elemen menggunakan satuan rem dan piksel."),
            ("width & height", "Menentukan dimensi lebar dan tinggi elemen."),
            ("max-width & min-height", "Membatasi dimensi maksimum dan minimum agar elemen tetap adaptif pada beragam resolusi layar."),
            ("aspect-ratio: 16/10", "Mempertahankan proporsi rasio gambar sertifikat secara konsisten agar tidak terdistorsi saat resolusi layar berubah.")
        ]),
        ("3. Layout: CSS Flexbox & CSS Grid", [
            ("display: flex", "Mengaktifkan model Flexible Box 1 dimensi untuk penataan komponen seperti navbar, tombol, dan kartu profil."),
            ("flex-direction: column / row", "Mengatur sumbu utama arah aliran elemen anak (vertikal atau horizontal)."),
            ("justify-content & align-items", "Mengatur perataan elemen sepanjang sumbu utama (main axis) dan sumbu silang (cross axis)."),
            ("gap: 1.5rem", "Menentukan jarak spasi seragam antar item flex atau grid tanpa memerlukan margin manual."),
            ("display: grid", "Mengaktifkan model Grid 2 dimensi untuk tata letak matriks keahlian dan galeri sertifikat."),
            ("grid-template-columns: repeat(auto-fill, minmax(320px, 1fr))", "Membuat grid kartu responsif otomatis yang mengisi ruang kosong tanpa memerlukan penulisan berulang media query.")
        ]),
        ("4. Positioning & Stacking Context", [
            ("position: fixed", "Mengunci posisi sidebar kiri di viewport sehingga tetap terlihat saat pengguna menggulir halaman."),
            ("position: relative & absolute", "Membangun sistem koordinat tumpuk, seperti meletakkan lencana centang aktif di atas foto profil avatar."),
            ("z-index: 100", "Mengatur urutan tumpukan lapisan visual elemen (stacking order) di atas konten lainnya.")
        ]),
        ("5. Tipografi & Teks", [
            ("font-family", "Menentukan keluarga huruf utama ('Segoe UI', 'Inter', monospace)."),
            ("font-size & font-weight", "Mengatur ukuran huruf (rem/pt) dan ketebalan huruf (400 normal, 600 semi-bold, 700 bold)."),
            ("line-height: 1.6", "Mengatur jarak antar baris teks untuk kenyamanan keterbacaan (readability)."),
            ("letter-spacing: 0.05em", "Mengatur kerning atau kerapatan jarak horizontal antar karakter huruf."),
            ("text-transform: uppercase", "Mengubah teks menjadi huruf kapital secara otomatis untuk label dan badge.")
        ]),
        ("6. Warna, Efek Visual & Dekorasi", [
            ("background: linear-gradient(...)", "Membuat gradasi warna linear halus untuk tombol primer dan pendaran aksen kartu."),
            ("background: radial-gradient(...)", "Membuat efek pendaran cahaya lingkaran di sudut banner hero."),
            ("border-radius: 12px / 50%", "Membuat sudut elemen membulat atau lingkaran sempurna (border-radius 50% pada avatar)."),
            ("box-shadow: 0 10px 25px rgba(...)", "Memberikan kedalaman elevasi 3D dan bayangan lembut pada kartu panel."),
            ("box-shadow: 0 0 20px rgba(0, 242, 254, 0.2)", "Memberikan efek pendaran cahaya neon (glow effect) khas tema siber.")
        ]),
        ("7. Transisi, Transformasi & Pseudo-Selectors", [
            ("transition: all 0.3s ease", "Memberikan animasi perubahan halus saat elemen berinteraksi (hover / focus)."),
            ("transform: translateY(-5px)", "Memberikan efek pengangkatan kartu secara vertikal saat disentuh kursor pengguna."),
            ("transform: scale(1.05)", "Memberikan efek perbesaran halus pada gambar sertifikat di dalam wadahnya."),
            (":hover & :focus", "Pseudo-class untuk menangkap status kursor mouse dan status fokus input formulir."),
            (":nth-child(even)", "Pseudo-class untuk mewarnai baris genap tabel (zebra striping) secara otomatis."),
            ("::before & ::after", "Pseudo-element untuk menyisipkan ikon hiasan tanpa menambah tag HTML tambahan.")
        ]),
        ("8. Desain Responsif (Responsive Media Queries)", [
            ("@media (max-width: 992px)", "Breakpoint tablet: Mengubah sidebar kiri menjadi bilah navigasi atas horizontal dan merestrukturisasi grid 2 kolom menjadi 1 kolom."),
            ("@media (max-width: 768px)", "Breakpoint seluler: Menyesuaikan ukuran tipografi judul, menyederhanakan padding, dan memastikan tabel dapat digulir secara horizontal via .table-responsive.")
        ])
    ]

    for cat_title, prop_list in css_categories:
        doc.add_heading(cat_title, level=3)
        for prop, desc in prop_list:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.15)
            r_p = p.add_run(f"• {prop} : ")
            r_p.font.bold = True
            r_p.font.color.rgb = RGBColor(30, 41, 59)
            p.add_run(desc)

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB V: RINGKASAN KONTEN PORTOFOLIO & REKAPITULASI DOKUMEN
    # -------------------------------------------------------------
    h5 = doc.add_heading("BAB V: KONTEN PORTOFOLIO & REKAP PRESTASI RESMI", level=1)
    h5.style.font.name = 'Segoe UI'
    h5.style.font.color.rgb = RGBColor(14, 116, 144)

    p = doc.add_paragraph(
        "Seluruh materi yang disajikan di dalam website portofolio merupakan data nyata yang diverifikasi melalui dokumen "
        "resmi piagam, surat keputusan, dan sertifikat beresolusi tinggi yang disimpan di dalam direktori assets/img/. "
        "Berikut adalah rincian 11 pencapaian utama yang dipublikasikan:"
    )

    cert_summary_data = [
        ("01", "03 Sep 2026", "Sertifikat Apresiasi: Temuan Kerentanan & Pelaporan Etis", "PUSSIBER TNI ANGKATAN DARAT (Kartika CSIRT)", "SERT/36/PUSSIBERAD/KARTIKA-CSIRT/IX/2026", "Predikat Khusus Keamanan Siber"),
        ("02", "20 Agu 2026", "Sertifikat Apresiasi: Pelaporan Vulnerability Sistem Elektronik", "BSSA Diskominfotik Provinsi DKI Jakarta", "113/BUG/BSSA/VIII/2026", "Predikat Khusus Pemprov DKI"),
        ("03", "28 Jun 2026", "Juara 4 (4th Place Scholar Battle Winner) - CTF ZERO DAY", "DSG & Fakultas Ilmu Komputer", "ZD-2026-CHAMP-04", "Kompetisi Siber Nasional"),
        ("04", "29 Jun 2026", "Cyber Threat Intelligence sebagai Core Intelligence IT", "SEVIMA (Sentra Vidya Utama)", "1000/SRTFK/SVM/VI/2026", "Pelatihan & MOOC"),
        ("05", "22 Jun 2026", "AI Disruptions on Cyber Security World", "SEVIMA (Sentra Vidya Utama)", "994/SRTFK/SVM/VI/2026", "Pelatihan & MOOC"),
        ("06", "15 Jun 2026", "SEVIMA Security Challenge 2026 (10 JP, Online MOOC)", "SEVIMA (Sentra Vidya Utama)", "903/SRTFK/SVM/VI/2026", "Pelatihan 10 Jam Pelajaran"),
        ("07", "19 Jun 2024", "CORE Cybersecurity Foundations", "Hackviser Online Security Academy", "HV-CORE-CERT-2024", "Sertifikasi Global"),
        ("08", "2024", "Certified Ransomware Protection Officer (CRPO)", "EU Cyber Academy", "CRPO-EU-CERT-64D6", "Sertifikasi Spesialis"),
        ("09", "31 Jan 2024", "Generative AI for Youth Training", "Microsoft AI Skills", "MS-GENAI-2024-ID", "Pelatihan Kecerdasan Buatan"),
        ("10", "21 Jan 2024", "Introduction to Cybersecurity Course Completion", "Cisco Networking Academy", "CISCO-NETACAD-INTRO", "Kursus Industri Global"),
        ("11", "20 Jan 2024", "Bootcamp Online Cyber Security Beginner Batch 1", "Merdeka Siber Academy", "MS/BOCSE/COE/24/2026/011", "Bootcamp Praktis")
    ]

    t_cert = doc.add_table(rows=12, cols=6)
    t_cert.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_cert.columns[0].width = Inches(0.4)
    t_cert.columns[1].width = Inches(0.9)
    t_cert.columns[2].width = Inches(1.8)
    t_cert.columns[3].width = Inches(1.4)
    t_cert.columns[4].width = Inches(1.2)
    t_cert.columns[5].width = Inches(0.8)

    t_headers = ["No", "Tanggal", "Nama Prestasi / Sertifikasi", "Penyelenggara", "No. Registrasi", "Kategori"]
    for i, title in enumerate(t_headers):
        cell = t_cert.cell(0, i)
        set_cell_background(cell, "0E7490")
        set_cell_margins(cell, top=80, bottom=80, left=70, right=70)
        p = cell.paragraphs[0]
        r = p.add_run(title)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(8.5)

    for row_idx, rdata in enumerate(cert_summary_data):
        row = t_cert.rows[row_idx + 1]
        bg = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        if row_idx in [0, 1]:
            bg = "FEF3C7" if row_idx == 0 else "E0F2FE" # Highlight for PUSSIBER and BSSA
        for col_idx in range(6):
            cell = row.cells[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            r = p.add_run(rdata[col_idx])
            r.font.size = Pt(8.0)
            if col_idx in [0, 2]:
                r.font.bold = True

    # -------------------------------------------------------------
    # BAB VI: KESIMPULAN & PENUTUP
    # -------------------------------------------------------------
    doc.add_heading("BAB VI: KESIMPULAN & REFLEKSI PEMBELAJARAN", level=1)

    p = doc.add_paragraph(
        "Berdasarkan perancangan, implementasi kode, dan deployment yang telah dilakukan, dapat disimpulkan bahwa:\n"
        "1. Proyek website portofolio pribadi Muhammad Jawsyan telah berhasil dibangun secara mandiri dengan memenuhi seluruh "
        "ketentuan akademis yang ditetapkan oleh dosen pengampu Bapak Rahmad Syalevi, S. Kom., M.T.I pada mata kuliah Pemrograman Web.\n"
        "2. Seluruh 13 butir kriteria evaluasi teknis (minimal 3 halaman, elemen table, image, link, list, form, input, button, "
        "tiga metode CSS eksternal/internal/inline, struktur semantik HTML5, serta kemurnian vanilla tanpa framework) telah dipenuhi dan diuji dengan sempurna.\n"
        "3. Pemanfaatan standar web modern W3C membuktikan bahwa tampilan yang memukau, responsif, dan interaktif bergaya ala iPortfolio "
        "dapat direalisasikan secara elegan menggunakan kekuatan murni CSS3 (Grid, Flexbox, Variables, Shadows, dan Media Queries) "
        "tanpa ketergantungan pada pustaka pihak ketiga.\n"
        "4. Proyek telah diarsipkan secara profesional pada sistem kendali versi Git, dipublikasikan secara terbuka di repositori GitHub "
        "(https://github.com/j12k14a/portfolio-jawsyan-htmlcss), dan telah aktif ter-deploy di server GitHub Pages "
        "(https://j12k14a.github.io/portfolio-jawsyan-htmlcss/) sehingga dapat diakses dan dievaluasi secara langsung."
    )

    # Output file paths
    repo_dst = r"C:\Users\user\.gemini\antigravity\scratch\portfolio-jawsyan-htmlcss\Laporan_Tugas_Pemrograman_Web_Muhammad_Jawsyan.docx"
    downloads_dst = r"C:\Users\user\Downloads\Laporan_Tugas_Pemrograman_Web_Muhammad_Jawsyan.docx"
    
    doc.save(repo_dst)
    shutil.copy2(repo_dst, downloads_dst)
    
    print(f"Laporan DOCX berhasil dibuat di:")
    print(f"1. {repo_dst}")
    print(f"2. {downloads_dst}")

if __name__ == "__main__":
    build_report()
