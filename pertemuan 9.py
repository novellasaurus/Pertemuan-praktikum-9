# PROGRAM 9.1 LIST
## --- LIST ---

# Kumpulan data numbers
data_angka = [1, 5, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(data_angka)

# Kumpulan data string
data_string = ["novel", "nur", "fahmi"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "novel", 2, "nur", "fahmi", True, "adit", False]
print(data_campuran)

## Cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start, stop, step)
print(data_range)

data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop (list comprehension)
list_for = [i ** 2 for i in range(0, 10)]
print(list_for)

# Membuat list pakai for dan if
list_for_if = [i for i in range(0, 10) if i != 5]
print(list_for_if)

# Membuat list bilangan genap
list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)

# Membuat list bilangan ganjil
list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_for_if)

#PROGRAM 9.2 MANIPULASI LIST
## --- OPERASI LIST ---
# index 0(-3) 1(-2) 2(-1)
data = ["novel", "nur", "fahmi"]

# mengambil data dari list
data_0 = data[0]
print(f"data index 0: {data_0}")

data_terakhir = data[-1]
print(f"data index terakhir: {data_terakhir}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"jumlah data dalam list: {panjang_data}")

# manipulasi data list
#menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

#data.insert(posisi,item)

data.insert(1,"teddy")
print(f"data setelah ditambah = \n{data}")

#menambah diakhir list
data.append("fufufafa")
print(f"data ditambah lagi = \n{data}")

#menambahkan list dengan list
data_baru = ["fahmi", "adit","novel"]
data.extend(data_baru)
print(f"data digabung = \n{data}")

#merubah data
#kita rubah data 2 menjadi jarwo
data[2] = "jarwo"
print(f"data rubah = \n{data}")

#menghapus data
data.remove("novel")
print(f"data hapus = \n{data}")

#menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")

#PROGRAM 9.3 OPERASI LIST

## --- Operasi LIST ---

# Data angka
data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]

print(f"data angka = \n{data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# Mengambil posisi data
data = ["Rendi", "Iqbal", "Gana", "Khairil"]

print(f"data = {data}")

index_Iqbal = data.index("Iqbal")
index_Gana = data.index("Gana")

print(f"index si Iqbal = {index_Iqbal}")
print(f"index si Gana = {index_Gana}")

# Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# Membalik urutan list
data_angka.reverse()
data.reverse()

print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

#PROGRAM 9.4 NESTED LIST
## --- Nested LIST ---

data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2D = {list_2D}")

# Contoh penggunaan Nested List

peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")
    
