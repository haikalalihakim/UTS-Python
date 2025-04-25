usia = int(input("Masukkan usia Anda: "))

if usia < 12:
  print("Anak-anak")
elif usia >= 12 and usia <= 17:
  print("Remaja")
elif usia >= 18 and usia <= 59:
  print("Dewasa")
else:
  print("Lansia")
