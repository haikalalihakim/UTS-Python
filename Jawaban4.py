todo_list = {
    "Belajar Python": "Belum",
    "Cuci Baju": "Selesai"
}

def tambah_tugas():
  tugas_baru = input("Masukkan tugas baru: ")
  status_baru = input("Masukkan status tugas (Belum/Selesai): ")
  todo_list[tugas_baru] = status_baru
  print(f"Tugas '{tugas_baru}' berhasil ditambahkan.")

def ubah_status():
  tugas = input("Masukkan nama tugas yang ingin diubah statusnya: ")
  if tugas in todo_list:
    status_baru = input("Masukkan status baru (Belum/Selesai): ")
    todo_list[tugas] = status_baru
    print(f"Status tugas '{tugas}' berhasil diubah.")
  else:
    print(f"Tugas '{tugas}' tidak ditemukan.")

def tampilkan_daftar_tugas():
  status = input("Tampilkan tugas dengan status (Belum/Selesai/Semua): ")
  print("\nDaftar Tugas:")
  for tugas, status_tugas in todo_list.items():
    if status.lower() == "semua" or status_tugas.lower() == status.lower():
      print(f"- {tugas}: {status_tugas}")

while True:
  print("\nMenu:")
  print("1. Tambah Tugas Baru")
  print("2. Ubah Status Tugas")
  print("3. Tampilkan Daftar Tugas")
  print("4. Keluar")

  pilihan = input("Pilih menu (1/2/3/4): ")

  if pilihan == "1":
    tambah_tugas()
  elif pilihan == "2":
    ubah_status()
  elif pilihan == "3":
    tampilkan_daftar_tugas()
  elif pilihan == "4":
    print("Terima kasih!")
    break
  else:
    print("Pilihan tidak valid.")
