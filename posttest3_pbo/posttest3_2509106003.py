from abc import ABC, abstractmethod

# Class untuk metode pembayaran
class MetodePembayaran(ABC):
    def __init__(self, nama_metode):
        self.nama_metode = nama_metode

    # Buat proses pembayaran
    @abstractmethod
    def proses_pembayaran(self, total):
        pass

    # Untuk nampilkan bukti pembayaran
    @abstractmethod
    def tampilkan_bukti(self):
        pass

    # Untuk nampilkan status metode pembayaran
    def tampilkan_status(self):
        print(f"| Metode {self.nama_metode} siap digunakan.           |")

    # Menjalankan proses pembayaran
    def bayar(self, total):
        self.tampilkan_status()

        if self.proses_pembayaran(total):
            self.tampilkan_bukti()
            print("| Pembayaran berhasil.                   |")
            return True
        else:
            print("| Pembayaran gagal.                      |")
        return False

        
# Class untuk pembayaran tunai
class PembayaranTunai(MetodePembayaran):
    def __init__(self, uang_dibayar):
        super().__init__("Tunai")
        self.uang_dibayar = uang_dibayar

    # Untuk proses pembayaran tunai
    def proses_pembayaran(self, total):
        if self.uang_dibayar >= total:
            return True
        return False

    # Untuk nampilkan bukti pembayaran
    def tampilkan_bukti(self):
        print("| Pembayaran dilakukan secara tunai.     |")


# Class untuk pembayaran transfer
class PembayaranTransfer(MetodePembayaran):
    def __init__(self, nomor_referensi):
        super().__init__("Transfer")
        self.nomor_referensi = nomor_referensi

    # Untuk proses pembayaran transfer
    def proses_pembayaran(self, total):
        if total > 0:
            return True
        return False

    # Untuk nampilkan bukti pembayaran
    def tampilkan_bukti(self):
        print(f"Nomor referensi: {self.nomor_referensi}")

# Class induk untuk semua produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self._stok = stok
        self.__kode_produk = "210407"

    # Menampilkan informasi produk
    def tampilkan_info(self):
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<10,}".replace(",", ".") + " " * 9 + "|")
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


# Class untuk produk olahraga
class ProdukOlahraga(Produk):
    def __init__(self, nama, harga, stok, jenis_olahraga):
        super().__init__(nama, harga, stok)
        self.jenis_olahraga = jenis_olahraga

    # Menampilkan informasi produk olahraga
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<10,}".replace(",", ".") + " " * 9 + "|")
        print(f"| {'Stok':<15} : {self._stok:<21}|")
        print(f"| {'Jenis Olahraga':<15} : {self.jenis_olahraga:<21}|")
        print("+----------------------------------------+")


# Class untuk produk elektronik
class ProdukElektronik(Produk):
    def __init__(self, nama, harga, stok, masa_garansi):
        super().__init__(nama, harga, stok)
        self.masa_garansi = masa_garansi

    # Menampilkan informasi produk elektronik
    def tampilkan_info(self):
        print("+----------------------------------------+")
        print(f"| {'Nama Produk':<15} : {self.nama:<21}|")
        print(f"| {'Harga':<15} : Rp{self.harga:<10,}".replace(",", ".") + " " * 9 + "|")
        print(f"| {'Stok':<15} : {self._stok:<21}|")
        print(f"| {'Masa Garansi':<15} : {str(self.masa_garansi) + ' bulan':<21}|")
        print("+----------------------------------------+")


# Menyimpan detail produk yang dibeli
class DetailPenjualan:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah
        self.total = produk.harga * jumlah

    # Menampilkan detail pembelian
    def tampilkan_detail(self):
        teks = f"{self.produk.nama} x {self.jumlah} = Rp{self.total:,}".replace(",", ".")
        print(f"| {teks:<39}|")


# Class untuk mengatur transaksi
class Penjualan:
    def __init__(self, nomor_transaksi):
        self.nomor_transaksi = nomor_transaksi
        self._daftar_produk = []
        self._detail_penjualan = []

    # Menghitung jumlah detail produk dalam transaksi
    def __len__(self):
        return len(self._detail_penjualan)

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

    # Memproses pembayaran melalui metode yang dipilih
    def proses_pembayaran(self, metode: MetodePembayaran, total):
        return metode.bayar(total)

    # Menampilkan ringkasan penjualan
    def tampilkan_ringkasan(self):
        print(f"| Nomor Transaksi: {self.nomor_transaksi:<22}|")
        print(f"| Jumlah Detail Produk: {len(self):<17}|")


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
        print(f"| {'Total Penjualan':<17} : Rp{total_semua:<17,}|".replace(",", "."))
        print("+----------------------------------------+")
        return total_semua


# Class untuk menyimpan data pelanggan
class Pelanggan:
    def __init__(self, nama, nomor_telepon):
        self.nama = nama
        self.nomor_telepon = nomor_telepon

    # Menampilkan ringkasan pelanggan
    def tampilkan_ringkasan(self):
        print(f"| Nama Pelanggan : {self.nama:<22}|")
        print(f"| Nomor Telepon  : {self.nomor_telepon:<22}|")

    # Pelanggan membeli produk
    def beli(self, transaksi, produk, jumlah):
        transaksi.tambah_produk(produk)
        transaksi.tambah_detail(produk, jumlah)


# Fungsi untuk duck typing
def tampilkan_ringkasan(objek):
    objek.tampilkan_ringkasan()


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

daftar_produk = [produk1, produk2, produk3]

for produk in daftar_produk:
    produk.tampilkan_info()


# Membuat pelanggan
pelanggan1 = Pelanggan(
    "Komang",
    "082150522176"
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

# Pengujian duck typing
print()
print("+----------------------------------------+")
print("|              DUCK TYPING               |")
print("+----------------------------------------+")

tampilkan_ringkasan(pelanggan1)
tampilkan_ringkasan(penjualan1)

print("+----------------------------------------+")

# Menampilkan hasil transaksi
total_bayar = penjualan1.tampilkan_penjualan()


# Memproses pembayaran tunai
print()
print("+----------------------------------------+")
print("|            PROSES PEMBAYARAN           |")
print("+----------------------------------------+")

pembayaran = PembayaranTunai(total_bayar)
penjualan1.proses_pembayaran(pembayaran, total_bayar)

print("+----------------------------------------+")


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


# Untuk mengecek abstract class
print()
print("+----------------------------------------+")
print("|           PENGUJIAN ABSTRAKSI          |")
print("+----------------------------------------+")
print("| Abstract class tidak bisa dibuat objek.|")
print("| Method abstrak yang belum diterapkan:  |")
print("| - proses_pembayaran()                  |")
print("| - tampilkan_bukti()                    |")
print("+----------------------------------------+")

try:
    metode = MetodePembayaran("Pembayaran")
except TypeError:
    print("| Pengujian berhasil: objek ditolak.     |")
    print("+----------------------------------------+")
else:
    print("| Pengujian gagal.                       |")
    print("+----------------------------------------+")