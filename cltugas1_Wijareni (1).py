class AlatMusik:
  pass

alat1 = AlatMusik()
alat2 = AlatMusik()


alat1 = AlatMusik()

alat1.nama = "Fender Stratocaster"
alat1.jenis = "Gitar Elektrik"
alat1.warna = "Sunburst"
alat1.tahun_rilis = 1954
alat1.harga = 35000000

alat2 = AlatMusik()

alat2.nama = "Yamaha Grand Piano C3"
alat2.jenis = "Piano Akustik"
alat2.warna = "Hitam Glossy"
alat2.tahun_rilis = 2021
alat2.harga = 180000000

print("\n--- Detail Alat Musik 1 ---")
print(f"Nama: {alat1.nama}")
print(f"Jenis: {alat1.jenis}")
print(f"Warna: {alat1.warna}")
print(f"Tahun Rilis: {alat1.tahun_rilis}")
print(f"Harga: Rp{alat1.harga:,}")

print("\n--- Detail Alat Musik 2 ---")
print(f"Nama: {alat2.nama}")
print(f"Jenis: {alat2.jenis}")
print(f"Warna: {alat2.warna}")
print(f"Tahun Rilis: {alat2.tahun_rilis}")
print(f"Harga: Rp{alat2.harga:,}")