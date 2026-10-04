class Produk:
    # Class induk untuk semua produk
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self._stok = stok
        self.__kode_produk = "210407"

    # Menampilkan informasi produk
    def tampilkan_info(self):
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<19,}|")
        print(f"| {'Stok':<15} : {self._stok:<21}|")
        print("+----------------------------------------+")

    # Menambah stok
    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self._stok += jumlah
        else:
            print("Jumlah stok tidak valid.")

    # Mengurangi stok saat produk terjual
    def kurangi_stok(self, jumlah):
        if jumlah > 0 and jumlah <= self._stok:
            self._stok -= jumlah
            return True
        else:
            return False


class ProdukOlahraga(Produk):
    # Class untuk produk olahraga
    def __init__(self, nama, harga, stok, jenis_olahraga):
        super().__init__(nama, harga, stok)
        self.jenis_olahraga = jenis_olahraga

    # Menampilkan informasi produk olahraga
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<19,}|")
        print(f"| {'Stok':<15} : {self._stok:<21}|")
        print(f"| {'Jenis Olahraga':<15} : {self.jenis_olahraga:<21}|")
        print("+----------------------------------------+")


class ProdukElektronik(Produk):
    # Class untuk produk elektronik
    def __init__(self, nama, harga, stok, masa_garansi):
        super().__init__(nama, harga, stok)
        self.masa_garansi = masa_garansi

    # Menampilkan informasi produk elektronik
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<19,}|")
        print(f"| {'Stok':<15} : {self._stok:<21}|")
        print(f"| {'Masa Garansi':<15} : {str(self.masa_garansi) + ' bulan':<21}|")
        print("+----------------------------------------+")


class DetailPenjualan:
    # Menyimpan detail produk yang dibeli
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah
        self.total = produk.harga * jumlah

    # Menampilkan detail pembelian
    def tampilkan_detail(self):
        teks = f"{self.produk.nama} x {self.jumlah} = Rp{self.total:,}"
        print(f"| {teks:<39}|")


class Penjualan:
    # Class untuk mengatur transaksi
    def __init__(self, nomor_transaksi):
        self.nomor_transaksi = nomor_transaksi
        self._daftar_produk = []
        self._detail_penjualan = []

    # Menambahkan produk ke transaksi
    def tambah_produk(self, produk):
        if isinstance(produk, Produk):
            self._daftar_produk.append(produk)

    # Membuat detail produk yang dibeli
    def tambah_detail(self, produk, jumlah):
        if produk in self._daftar_produk:
            if produk.kurangi_stok(jumlah):
                detail = DetailPenjualan(produk, jumlah)
                self._detail_penjualan.append(detail)

    # Menampilkan transaksi
    def tampilkan_penjualan(self):
        print()
        print("+----------------------------------------+")
        print("|           DETAIL PENJUALAN             |")
        print("+----------------------------------------+")
        print(f"| {'Nomor Transaksi':<17} : {self.nomor_transaksi:<19}|")
        print("|                                        |")

        total_semua = 0

        for detail in self._detail_penjualan:
            detail.tampilkan_detail()
            total_semua += detail.total

        print("|                                        |")
        print("+----------------------------------------+")
        print(f"| {'Total Penjualan':<17} : Rp{total_semua:<17,}|")
        print("+----------------------------------------+")


class Pelanggan:
    # Class untuk menyimpan data pelanggan
    def __init__(self, nama, nomor_telepon):
        self.nama = nama
        self.nomor_telepon = nomor_telepon

    # Pelanggan membeli produk
    def beli(self, transaksi, produk, jumlah):
        transaksi.tambah_produk(produk)
        transaksi.tambah_detail(produk, jumlah)


# ========================================
# PROGRAM UTAMA
# ========================================

print("+----------------------------------------+")
print("|    SISTEM PENJUALAN TOKO PERLENGKAPAN  |")
print("|                OLAHRAGA                |")
print("+----------------------------------------+")


# Membuat produk
produk1 = ProdukOlahraga(
    "Bola Voli",
    170000,
    15,
    "Bola Voli"
)

produk2 = ProdukOlahraga(
    "Sepatu Futsal",
    499000,
    15,
    "Futsal"
)

produk3 = ProdukElektronik(
    "Papan Skor Digital",
    150000,
    10,
    12
)


# Menampilkan data produk
print()
print("+----------------------------------------+")
print("|              DATA PRODUK               |")
print("+----------------------------------------+")

produk1.tampilkan_info()
produk2.tampilkan_info()
produk3.tampilkan_info()


# Membuat pelanggan
pelanggan1 = Pelanggan(
    "Ni Komang Kariani",
    "081234567890"
)


# Membuat transaksi
penjualan1 = Penjualan("160705")


# Pelanggan membeli Bola Voli
pelanggan1.beli(
    penjualan1,
    produk1,
    2
)


# Menambahkan Sepatu Futsal
penjualan1.tambah_produk(produk2)
penjualan1.tambah_detail(
    produk2,
    1
)


# Menampilkan hasil transaksi
penjualan1.tampilkan_penjualan()


# Menampilkan stok setelah penjualan
print()
print("+----------------------------------------+")
print("|        STOK SETELAH PENJUALAN          |")
print("+----------------------------------------+")

produk1.tampilkan_info()
produk2.tampilkan_info()


# Mengecek inheritance
print()
print("+----------------------------------------+")
print("|          PENGUJIAN INHERITANCE         |")
print("+----------------------------------------+")
print(f"| {'produk1 adalah Produk':<28} : {str(isinstance(produk1, Produk)):<8}|")
print(f"| {'produk2 adalah Produk':<28} : {str(isinstance(produk2, Produk)):<8}|")
print(f"| {'produk3 adalah Produk':<28} : {str(isinstance(produk3, Produk)):<8}|")
print(f"| {'ProdukOlahraga subclass':<28} : {str(issubclass(ProdukOlahraga, Produk)):<8}|")
print(f"| {'ProdukElektronik subclass':<28} : {str(issubclass(ProdukElektronik, Produk)):<8}|")
print("+----------------------------------------+")