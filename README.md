# Pertemuan 13 - Debugging dan Testing

Nama: Lyzna Nuraini
NIM: 2225250032
Kelas: 3E

## Kasus
Praktikum ini berfokus pada investigasi bug, teknik *tracing*, penggunaan *debugger* VS Code, perancangan *test case* (normal, batas, tidak valid), serta dokumentasi perbaikan kode Python dan pengunggahan riwayat *commit* ke GitHub.

## Test Case
| ID | Input | Expected | Actual Awal | Status |
|----|-------|----------|-------------|--------|
| T1 | [80, 60, 90, 70] (rata-rata) | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] (rata-rata) | 90.0 | 36.0 | FAIL |
| T3 | 60 (status kelulusan) | Lulus | Tidak lulus | FAIL |
| T4 | 59 (status kelulusan) | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] (tertinggi) | 90 | 0 | FAIL |

## Bug Report
1. **B01 (Fungsi `hitung_rata_rata`)**: Membagi total nilai dengan angka konstan `5` alih-alih menggunakan `len(nilai)`.
2. **B02 (Fungsi `status`)**: Menggunakan operator `>`, sehingga nilai `60` persis dianggap "Tidak lulus" (seharusnya `>= 60`).
3. **B03 (Fungsi `nilai_tertinggi`)**: Inisialisasi variabel `tertinggi = 0` dan logika perbandingan `<` keliru sehingga gagal mendeteksi nilai maksimum yang benar.

## Retest
Seluruh *test case* (T1 sampai T5) telah diuji ulang setelah perbaikan kode dan menghasilkan status **PASS** tanpa adanya regresi.

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py