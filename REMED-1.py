jenis = input("Masukkan jenis produk (Elektronik/Pakaian/Makanan/Kosmetik): ")
harga = int(input("Masukkan harga produk: "))
penjualan = int(input("Masukkan jumlah produk terjual: "))

if jenis() == "elektronik":
    kategori = "Elektronik"
elif jenis() == "pakaian":
    kategori = "Pakaian"
elif jenis() == "makanan":
    kategori = "Makanan"
elif jenis() == "kosmetik":
    kategori = "Kosmetik"
else:
    kategori = "Tidak diketahui"

if harga > 100000:
    label_harga = "Premium"
elif 50000 <= harga <= 100000:
    label_harga = "Menengah"
else:
    label_harga = "Terjangkau"

if penjualan >= 100:
    status = "Best Seller"
elif 50 <= penjualan < 100:
    status = "Populer"
else:
    status = "Normal"