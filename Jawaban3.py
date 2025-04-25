def analyze_transactions(transactions):
  saldo_akhir = 0
  pengeluaran_terbesar = 0
  hari_pengeluaran_terbesar = ""
  hari_tanpa_transaksi = []

  for hari, jumlah in transactions:
    saldo_akhir += jumlah
    if jumlah < 0 and abs(jumlah) > pengeluaran_terbesar:
      pengeluaran_terbesar = abs(jumlah)
      hari_pengeluaran_terbesar = hari
    if jumlah == 0:
      hari_tanpa_transaksi.append(hari)

  return saldo_akhir, hari_pengeluaran_terbesar, hari_tanpa_transaksi

transactions = [("Senin", 50000), ("Selasa", -20000), ("Rabu", 0), ("Kamis", 100000)]
saldo_akhir, hari_pengeluaran_terbesar, hari_tanpa_transaksi = analyze_transactions(transactions)

print(f"Saldo Akhir : {saldo_akhir}")
print(f"Hari pengeluaran terbesar : {hari_pengeluaran_terbesar}")
print(f"Hari Tanpa Transaksi : {', '.join(hari_tanpa_transaksi)}")
