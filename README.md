# WFA-Parallelism

# Tugas WFA - Komputasi Paralel dan Sistem Distribusi

**Nama:** Alsani Abdul Rofiq  
**NRP:** 152024129 - Ganjil  
**Topik:** Implementasi Task Parallelism menggunakan Python

---

## Deskripsi Tugas
Tugas ini bertujuan untuk mendemonstrasikan pemahaman mengenai **Task Parallelism** pada nomor NRP ganjil. Program ini mensimulasikan dua tugas (task) berbeda yang dijalankan secara simultan untuk meningkatkan efisiensi waktu eksekusi.

## Studi Kasus
Program mensimulasikan **Media Processing System** yang melakukan dua operasi berbeda secara bersamaan:
1. **Task A (Download Video):** Mensimulasikan proses I/O bound (mengunduh file).
2. **Task B (Encrypt Data):** Mensimulasikan proses CPU bound (melakukan enkripsi/komputasi data).

## Penjelasan Teknis
* **Library:** Menggunakan modul `multiprocessing` untuk bypass Global Interpreter Lock (GIL).
* **Parallelism:** Setiap task dialokasikan ke Process ID (PID) yang berbeda oleh OS Scheduler.
* **Efisiensi:** Total waktu eksekusi dipangkas menjadi durasi task terlama (paralel), bukan total akumulasi kedua task (sekuensial).

## Cara Menjalankan
1. Pastikan Python 3.x sudah terinstall.
2. Jalankan perintah:
   ```bash
   python task_parallelism.py
