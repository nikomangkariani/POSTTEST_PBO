# =====================================================================
# POSTTEST 1 PEMROGRAMAN BERORIENTASI OBJEK
# TEMA : SISTEM MANAJEMEN PENJUALAN DAN STOK TOKO PERLENGKAPAN OLAHRAGA
# =====================================================================


#  Data produk

class Produk:

    # Nama toko dan jumlah produk yang dibuat
    nama_toko = "Toko Perlengkapan Olahraga"
    jumlah_produk = 0

    def __init__(self, nama, harga, stok, kategori):
        # Untuk menyimpan data produk
        self.nama = nama
        self.harga = harga
        self.kategori = kategori

        # Stok dibuat private supaya tidak bisa diubah sembarangan
        self.__stok = stok

        # Setiap membuat produk baru, jumlah produk bertambah
        Produk.jumlah_produk += 1

    
    # Getter

    @property
    # Untuk mengambil nilai stok yang disimpan
    def stok(self):
        return self.__stok

    # Setter

    @stok.setter
    # Mengubah stok sekaligus mengecek nilainya
    def stok(self, stok_baru):
        if stok_baru < 0:
            print("Stok tidak boleh negatif.")
        else:
            self.__stok = stok_baru
            print("Stok berhasil diperbarui.")


    # Menampilkan data produk

    def tampilkan_produk(self):
        print("Nama Produk :", self.nama)
        print("Harga       : Rp", self.harga)
        print("Stok        :", self.stok)
        print("Kategori    :", self.kategori)

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print("Stok", self.nama, "berhasil ditambah", jumlah)
        else:
            print("Jumlah stok yang ditambahkan harus lebih dari 0.")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah stok yang dikurangi harus lebih dari 0.")
        elif jumlah > self.__stok:
            print("Stok", self.nama, "tidak mencukupi.")
        else:
            self.__stok -= jumlah
            print("Stok", self.nama, "berhasil dikurangi", jumlah)


    # Membuat produk dari data dictionary

    @classmethod
    def dari_dict(cls, data):
        # Mengambil data produk dari dictionary
        return cls(
            data["nama"],
            data["harga"],
            data["stok"],
            data["kategori"]
        )


    # Cek harga yang dimasukkan
    @staticmethod
    def validasi_harga(harga):
        return harga > 0



# Data pelanggan

class Pelanggan:

    # Menentukan jenis pelanggan
    jenis_pelanggan = "Pelanggan Umum"

    def __init__(self, nama, no_hp):
        # Menyimpan data pelanggan
        self.nama = nama
        self.no_hp = no_hp

    
    # Menampilkan data pelanggan

    def tampilkan_pelanggan(self):
        print("Nama Pelanggan :", self.nama)
        print("No. HP         :", self.no_hp)


    # Mengubah jenis pelanggan

    @classmethod
    def ubah_jenis_pelanggan(cls, jenis_baru):
        if jenis_baru.strip() == "":
            print("Jenis pelanggan tidak boleh kosong.")
        else:
            cls.jenis_pelanggan = jenis_baru
            print("Jenis pelanggan berhasil diubah.")

    
    # Mengecek nomor HP pelanggan

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.isdigit() and len(no_hp) >= 10



# Bagian data penjualan

class Penjualan:

    # Menyimpan jumlah transaksi yang sudah dibuat
    total_transaksi = 0

    def __init__(self, produk, pelanggan, jumlah):
        # Menyimpan data yang berhubungan dengan penjualan
        self.produk = produk
        self.pelanggan = pelanggan
        self.jumlah = jumlah
        self.total = produk.harga * jumlah

        # Setiap ada transaksi baru, jumlahnya bertambah
        Penjualan.total_transaksi += 1

    
    # Menghitung total penjualan

    def hitung_total(self):
        self.total = self.produk.harga * self.jumlah
        return self.total

    def proses_penjualan(self):
        if self.jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0.")

        elif self.jumlah > self.produk.stok:
            print("Penjualan gagal.")
            print("Stok", self.produk.nama, "tidak mencukupi.")

        else:
            self.produk.kurangi_stok(self.jumlah)

            print("Penjualan berhasil.")
            print("Pelanggan :", self.pelanggan.nama)
            print("Produk    :", self.produk.nama)
            print("Jumlah    :", self.jumlah)
            print("Total     : Rp", self.hitung_total())

    def tampilkan_transaksi(self):
        print("Pelanggan :", self.pelanggan.nama)
        print("Produk    :", self.produk.nama)
        print("Jumlah    :", self.jumlah)
        print("Total     : Rp", self.total)



# Main Program

print("|=======================================|")
print("|  SISTEM MANAJEMEN PENJUALAN DAN STOK  |") 
print("|     TOKO PERLENGKAPAN OLAHRAGA        |")
print("|=======================================|")


# Pembuatan 2 objek class program

print("\n========== DATA PRODUK ==========")

produk1 = Produk(
    "Bola Basket",
    350000,
    15,
    "Bola"
)

produk2 = Produk(
    "Raket Badminton",
    500000,
    25,
    "Raket"
)

produk1.tampilkan_produk()
print()

produk2.tampilkan_produk()


# Mencoba fungsi untuk menambah dan mengurangi stok

print("\n========== INSTANCE METHOD PRODUK ==========")

produk1.tambah_stok(5)

print("Stok Bola Basket sekarang :", produk1.stok)

produk2.kurangi_stok(2)

print("Stok Raket Badminton sekarang :", produk2.stok)


# Melihat stok melalui getter

print("\n========== PENGUJIAN GETTER ==========")

print("Stok produk 1 :", produk1.stok)
print("Stok produk 2 :", produk2.stok)


# Mencoba mengubah stok dengan data yang benar

print("\n========== SETTER DATA VALID ==========")

produk1.stok = 20

print("Stok Bola Basket setelah diubah :", produk1.stok)


# Mencoba mengubah stok dengan angka negatif

print("\n========== SETTER DATA TIDAK VALID ==========")

produk1.stok = -5

print("Stok Bola Basket tetap :", produk1.stok)


# Mengecek apakah harga yang dimasukkan valid

print("\n========== STATIC METHOD PRODUK ==========")

print(
    "Harga 150000 valid :",
    Produk.validasi_harga(150000)
)

print(
    "Harga -5000 valid  :",
    Produk.validasi_harga(-5000)
)


# Membuat produk dari data dictionary

print("\n========== CLASS METHOD PRODUK ==========")

data_produk = {
    "nama": "Sepatu Futsal",
    "harga": 450000,
    "stok": 20,
    "kategori": "Sepatu"
}

produk3 = Produk.dari_dict(data_produk)

produk3.tampilkan_produk()


# Melihat data yang termasuk atribut kelas

print("\n========== ATRIBUT KELAS PRODUK ==========")

print("Nama toko :", Produk.nama_toko)
print("Jumlah produk yang dibuat :", Produk.jumlah_produk)


# Membuat 2 data pelanggan

print("\n========== DATA PELANGGAN ==========")

pelanggan1 = Pelanggan(
    "Miming",
    "082150522176"
)

pelanggan2 = Pelanggan(
    "Raditya",
    "085751386350"
)

pelanggan1.tampilkan_pelanggan()
print()

pelanggan2.tampilkan_pelanggan()


# Mengubah jenis pelanggan

print("\n========== CLASS METHOD PELANGGAN ==========")

Pelanggan.ubah_jenis_pelanggan("Member")

print("Jenis pelanggan :", Pelanggan.jenis_pelanggan)


# Mengecek nomor HP pelanggan

print("\n========== STATIC METHOD PELANGGAN ==========")

print(
    "No HP pelanggan 1 valid :",
    Pelanggan.validasi_no_hp(pelanggan1.no_hp)
)

print(
    "No HP 123 valid         :",
    Pelanggan.validasi_no_hp("123")
)


# Membuat 2 data penjualan

print("\n========== DATA PENJUALAN ==========")

penjualan1 = Penjualan(
    produk1,
    pelanggan1,
    2
)

penjualan2 = Penjualan(
    produk2,
    pelanggan2,
    1
)

penjualan1.tampilkan_transaksi()
print()

penjualan2.tampilkan_transaksi()


# Mencoba menjalankan proses penjualan

print("\n========== PROSES PENJUALAN ==========")

penjualan1.proses_penjualan()

print()

penjualan2.proses_penjualan()


# Melihat jumlah transaksi yang sudah dibuat

print("\n========== ATRIBUT KELAS PENJUALAN ==========")

print(
    "Total transaksi :",
    Penjualan.total_transaksi
)


# Melihat stok setelah produk terjual

print("\n========== STOK SETELAH PENJUALAN ==========")

print(
    "Stok Bola Basket :",
    produk1.stok
)

print(
    "Stok Raket Badminton :",
    produk2.stok
)


# program sudah selesai dijalankan

print("\n==================================================")
print(" PROGRAM SELESAI")
print("==================================================")