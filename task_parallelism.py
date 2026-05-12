import multiprocessing
import time
import os

# Tugas 1: Simulasi mengunduh file besar
def task_download_video(file_name):
    print(f"[DOWNLOAD] Memulai unduhan: {file_name}...")
    print(f"[DOWNLOAD] Berjalan di Process ID: {os.getpid()}")
    time.sleep(4)  # Simulasi waktu unduh
    print(f"[DOWNLOAD] Selesai! File {file_name} siap digunakan.")

# Tugas 2: Simulasi melakukan enkripsi/kompresi data
def task_encrypt_data(data_size):
    print(f"[ENCRYPT] Memulai enkripsi data sebesar {data_size}MB...")
    print(f"[ENCRYPT] Berjalan di Process ID: {os.getpid()}")
    time.sleep(2)  # Simulasi waktu proses CPU
    print(f"[ENCRYPT] Selesai! Data telah terenkripsi.")

if __name__ == "__main__":
    print("--- Memulai Task Parallelism ---")
    start_time = time.time()

    # Mendefinisikan dua tugas yang BERBEDA
    process_1 = multiprocessing.Process(target=task_download_video, args=("movie_4k.mp4",))
    process_2 = multiprocessing.Process(target=task_encrypt_data, args=(500,))

    # Menjalankan kedua tugas secara bersamaan
    process_1.start()
    process_2.start()

    # Menunggu kedua tugas selesai
    process_1.join()
    process_2.join()

    duration = time.time() - start_time
    print(f"--- Semua tugas selesai dalam {duration:.2f} detik ---")