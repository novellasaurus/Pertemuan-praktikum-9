# 1. Diberikan list berikut: 
# kendaraan = ['motor', 'mobil', 'sepeda', 'bus'] 
# a. Tambahkan 'truk' di akhir list 
# b. Sisipkan becak' pada index ke-1 
# c. Hapus data yang berada paling belakang dari list tersebut. 
# d. Ubah elemen 'sepeda' menjadi 'skuter'. 
# e. Tampilkan informasi jumlah total data di dalam list tersebut 

kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan truk di akhir list
kendaraan.append('truk')
print("a. Setelah ditambahkan truk:", kendaraan)

# b. Sisipkan becak pada index ke-1
kendaraan.insert(1, 'becak')
print("b. Setelah disisipkan becak:", kendaraan)

# c. Hapus data paling belakang
kendaraan.pop()
print("c. Setelah data terakhir dihapus:", kendaraan)

# d. Ubah sepeda menjadi skuter
kendaraan[2] = 'skuter'
print("d. Setelah sepeda diubah menjadi skuter:", kendaraan)

# e. Tampilkan jumlah total data
print("e. Jumlah total kendaraan:", len(kendaraan))

#2. Diberikan list berikut:
#  angka = [75, 80, 90, 75, 85, 100, 65] 
# a. Cari tahu di indeks ke berapa skor 100 berada. 
# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75. 
# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar. 
# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.

angka = [75, 80, 90, 75, 85, 100, 65]

# a. Mencari indeks skor 100
index_100 = angka.index(100)
print("a. Indeks skor 100:", index_100)

# b. Menghitung jumlah skor 75
jumlah_75 = angka.count(75)
print("b. Jumlah siswa yang mendapat skor 75:", jumlah_75)

# c. Mengurutkan angka dari terkecil ke terbesar
angka.sort()
print("c. Urutan dari terkecil ke terbesar:", angka)

# d. Membalik urutan angka
angka.reverse()
print("d. Urutan dari terbesar ke terkecil:", angka)

#3. menu_utama = ["Nasi Goreng", "Mie Ayam"] 
# menu_tambahan = ["Kerupuk", "Es Teh"] 
# Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, 
# kemudian tampilkan hasil dari data gabungan tersebut. 
# Latihan 3 - Menggabungkan List

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan kedua list menggunakan extend()
menu_utama.extend(menu_tambahan)

# Menampilkan hasil gabungan
print("Menu makanan setelah digabungkan:", menu_utama)

#4. Diberikan data nested list berupa informasi nama barang dan harganya: 
# data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 
# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut. 
# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan 
# format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya.
# Latihan 4 - Nested List

data_barang = [
    ["Buku", 5000],
    ["Pensil", 2000],
    ["Penggaris", 3000]
]

# a. Menampilkan harga Pensil
print("a. Harga Pensil:", data_barang[1][1])

# b. Menampilkan seluruh data menggunakan perulangan
print("\nb. Daftar Data Barang:")

for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")