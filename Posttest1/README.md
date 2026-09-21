# Sistem Manajemen Penjualan dan Stok Toko Perlengkapan Olahraga

## Deskripsi Program

Program ini saya buat menggunakan bahasa Python dengan menerapkan konsep Object-Oriented Programming (OOP).

Program ini digunakan untuk mengelola data produk dan stok, data pelanggan, serta proses penjualan pada toko perlengkapan olahraga.

## Class yang Digunakan

Program ini memiliki 3 class utama, yaitu Produk, Pelanggan, dan Penjualan.

### 1. Produk

Class Produk: digunakan untuk menyimpan data barang yang ada di toko, seperti nama produk, harga, stok, dan kategori.

Beberapa method yang digunakan yaitu:
- tampilkan_produk()
- tambah_stok()
- kurangi_stok()
- dari_dict()
- validasi_harga()

Pada class ini, stok dibuat sebagai atribut private __stok. Untuk mengakses dan mengubah stok digunakan @property dan @stok.setter.

### 2. Pelanggan

Class Pelanggan: digunakan untuk menyimpan data pelanggan yang melakukan pembelian.

Data pelanggan yang digunakan yaitu nama dan nomor HP.

Beberapa method yang digunakan yaitu:
- tampilkan_pelanggan()
- ubah_jenis_pelanggan()
- validasi_no_hp()

### 3. Penjualan

Class Penjualan: digunakan untuk mengatur proses penjualan barang.

Data yang digunakan dalam class ini yaitu produk, pelanggan, jumlah barang yang dibeli, dan total harga.

Beberapa method yang digunakan yaitu:
- hitung_total()
- proses_penjualan()
- tampilkan_transaksi()

Class Penjualan juga menggunakan data dari class Produk dan Pelanggan dalam proses transaksi.

## Konsep OOP yang Digunakan

Dalam program ini saya menerapkan beberapa konsep OOP, yaitu:

- Class dan Object
- Atribut dan Method
- Encapsulation
- Property
- Getter dan Setter
- Instance Method
- Class Method
- Static Method

## Pengujian Program

Program ini saya buat dengan beberapa pengujian untuk memastikan setiap bagian dapat berjalan dengan baik.

Pengujian yang dilakukan meliputi:

- Menampilkan data produk
- Menambah stok produk
- Mengurangi stok produk
- Menguji getter pada stok
- Menguji setter dengan data yang valid
- Menguji setter dengan data yang tidak valid
- Mengecek validitas harga menggunakan static method
- Membuat produk dari dictionary menggunakan class method
- Menampilkan atribut kelas pada class Produk
- Menampilkan data pelanggan
- Mengubah jenis pelanggan menggunakan class method
- Mengecek validitas nomor HP menggunakan static method
- Menampilkan data penjualan
- Menjalankan proses penjualan
- Menampilkan jumlah transaksi
- Melihat stok setelah proses penjualan

## Cara Menjalankan Program

Untuk menjalankan program, langkah yang dilakukan yaitu:

1. Buka file Python program di Visual Studio Code.
2. Jalankan program menggunakan tombol Run atau melalui terminal.
3. Program akan menjalankan bagian main program yang sudah dibuat.
4. Hasil pengujian akan ditampilkan pada terminal.

## Hasil Program

Program akan menampilkan beberapa hasil pengujian, seperti data produk, data pelanggan, data penjualan, perubahan stok, validasi data, dan proses penjualan.

Hasil pengujian dapat dilihat pada laporan yang sudah dibuat.