# Posttest 2 - Relasi UML dan Inheritance

## Sistem Manajemen Penjualan dan Stok Toko Perlengkapan Olahraga

### Identitas

- Nama: Ni Komang Kariani
- NIM: 2509106003
- Mata Kuliah: Pemrograman Berorientasi Objek

## Deskripsi Program

Program ini merupakan pengembangan dari program Posttest 1 dengan tema **Sistem Manajemen Penjualan dan Stok Toko Perlengkapan Olahraga**.

Pada Posttest 2 ini, program dikembangkan dengan menerapkan relasi UML dan inheritance sesuai dengan materi yang telah dipelajari. Relasi UML yang digunakan yaitu **Association, Aggregation, dan Composition**. Selain itu, program juga menerapkan inheritance dengan satu superclass dan dua subclass.

Program ini digunakan untuk mengelola data produk, stok produk, pelanggan, dan transaksi penjualan.

## Class yang Digunakan

Program ini memiliki 6 class, yaitu:

### 1. Produk

`Produk` merupakan class induk atau superclass yang menjadi dasar untuk produk yang ada di toko.

Atribut yang digunakan:
- `nama`
- `harga`
- `_stok`
- `__kode_produk`

Method yang digunakan:
- `tampilkan_info()`
- `tambah_stok()`
- `kurangi_stok()`

Atribut `_stok` digunakan sebagai atribut protected karena perlu diakses oleh class turunannya. Sedangkan `__kode_produk` digunakan sebagai atribut private yang hanya dimiliki oleh class `Produk`.

### 2. ProdukOlahraga

`ProdukOlahraga` merupakan subclass dari `Produk`.

Class ini memiliki atribut tambahan yang khusus untuk produk olahraga, yaitu:
- `jenis_olahraga`

Pada constructor-nya, class ini memanggil constructor superclass menggunakan:

```python
super().__init__(nama, harga, stok)
```

Class ini juga melakukan overriding pada method `tampilkan_info()` untuk menampilkan informasi tambahan berupa jenis olahraga.

### 3. ProdukElektronik

`ProdukElektronik` merupakan subclass dari `Produk`.

Class ini memiliki atribut tambahan yang khusus untuk produk elektronik, yaitu:
- `masa_garansi`

Pada constructor-nya, class ini memanggil constructor superclass menggunakan:

```python
super().__init__(nama, harga, stok)
```

Class ini juga melakukan overriding pada method `tampilkan_info()` untuk menampilkan informasi tambahan berupa masa garansi.

### 4. Pelanggan

`Pelanggan` digunakan untuk menyimpan data pelanggan.

Atribut yang digunakan:
- `nama`
- `nomor_telepon`

Class ini memiliki method `beli()` yang digunakan ketika pelanggan melakukan pembelian melalui transaksi.

### 5. Penjualan

`Penjualan` digunakan untuk mengatur transaksi penjualan.

Atribut yang digunakan:
- `nomor_transaksi`
- `_daftar_produk`
- `_detail_penjualan`

Method yang digunakan:
- `tambah_produk()`
- `tambah_detail()`
- `tampilkan_penjualan()`

Class ini digunakan untuk menambahkan produk ke transaksi, membuat detail pembelian, dan menampilkan hasil penjualan.

### 6. DetailPenjualan

`DetailPenjualan` digunakan untuk menyimpan detail produk yang dibeli dalam suatu transaksi.

Atribut yang digunakan:
- `produk`
- `jumlah`
- `total`

Method yang digunakan:
- `tampilkan_detail()`

Class ini digunakan untuk menampilkan nama produk, jumlah yang dibeli, dan total harga pembelian.

## Penerapan Relasi UML

### 1. Association

Association diterapkan antara class `Pelanggan` dan `Penjualan`.

Hubungan tersebut terlihat pada method `beli()`:

```python
def beli(self, transaksi, produk, jumlah):
    transaksi.tambah_produk(produk)
    transaksi.tambah_detail(produk, jumlah)
```

Pada bagian ini, `Pelanggan` menggunakan objek `Penjualan` untuk melakukan transaksi. Class `Pelanggan` tidak membuat objek `Penjualan`, tetapi menggunakan objek transaksi yang diberikan.

Jadi, hubungan antara `Pelanggan` dan `Penjualan` merupakan **Association**.

### 2. Aggregation

Aggregation diterapkan antara class `Penjualan` dan `Produk`.

Pada class `Penjualan` terdapat:

```python
self._daftar_produk = []
```

Kemudian produk ditambahkan ke dalam daftar menggunakan method:

```python
def tambah_produk(self, produk):
    if isinstance(produk, Produk):
        self._daftar_produk.append(produk)
```

Objek `Produk` dibuat terlebih dahulu di luar class `Penjualan`, kemudian dimasukkan ke dalam transaksi.

Jadi, `Penjualan` memiliki atau menggunakan `Produk`, tetapi objek `Produk` tetap dapat dibuat dan digunakan secara terpisah. Hal tersebut menunjukkan penerapan **Aggregation**.

### 3. Composition

Composition diterapkan antara class `Penjualan` dan `DetailPenjualan`.

Pada method `tambah_detail()`, objek `DetailPenjualan` dibuat di dalam proses transaksi:

```python
detail = DetailPenjualan(produk, jumlah)
self._detail_penjualan.append(detail)
```

`DetailPenjualan` dibuat sebagai bagian dari transaksi untuk menyimpan informasi produk yang dibeli, jumlah barang, dan total harga.

Jadi, hubungan antara `Penjualan` dan `DetailPenjualan` merupakan penerapan **Composition**.

## Penerapan Inheritance

Inheritance diterapkan dengan menjadikan `Produk` sebagai superclass dan `ProdukOlahraga` serta `ProdukElektronik` sebagai subclass.

Struktur inheritance yang digunakan:

```text
Produk
├── ProdukOlahraga
└── ProdukElektronik
```

### Superclass dan Subclass

Superclass yang digunakan adalah `Produk`, sedangkan subclass yang digunakan adalah `ProdukOlahraga` dan `ProdukElektronik`.

```python
class Produk:
```

```python
class ProdukOlahraga(Produk):
```

```python
class ProdukElektronik(Produk):
```

Dengan begitu, program memiliki satu superclass dan dua subclass sesuai dengan ketentuan.

### Penggunaan super()

Kedua subclass memanggil constructor dari superclass menggunakan `super().__init__()`.

Pada `ProdukOlahraga`:

```python
super().__init__(nama, harga, stok)
```

Pada `ProdukElektronik`:

```python
super().__init__(nama, harga, stok)
```

### Atribut Tambahan pada Subclass

Setiap subclass memiliki atribut khusus yang berbeda.

Pada `ProdukOlahraga` terdapat:

```python
self.jenis_olahraga = jenis_olahraga
```

Sedangkan pada `ProdukElektronik` terdapat:

```python
self.masa_garansi = masa_garansi
```

Atribut tersebut menjadi pembeda antara kedua subclass.

### Method Overriding

Method `tampilkan_info()` pada class `Produk` di-override pada `ProdukOlahraga` dan `ProdukElektronik`.

Pada `ProdukOlahraga`, method tersebut digunakan untuk menampilkan informasi tambahan berupa jenis olahraga.

Pada `ProdukElektronik`, method tersebut digunakan untuk menampilkan informasi tambahan berupa masa garansi.

Dengan begitu, kedua subclass memiliki perilaku yang berbeda dalam menampilkan informasi produk.

### Protected Attribute

Pada superclass `Produk` terdapat atribut:

```python
self._stok = stok
```

Atribut `_stok` merupakan atribut protected karena menggunakan satu garis bawah.

Atribut tersebut digunakan oleh subclass untuk mengakses data stok produk, contohnya:

```python
self._stok
```

### Private Attribute

Pada superclass `Produk` terdapat atribut:

```python
self.__kode_produk = "210407"
```

Atribut `__kode_produk` merupakan atribut private karena menggunakan dua garis bawah.

Atribut tersebut menjadi data yang bersifat khusus untuk class `Produk`.

## Alur Program

Alur program yang dijalankan yaitu:

1. Membuat beberapa objek produk.
2. Menampilkan data produk.
3. Membuat data pelanggan.
4. Membuat transaksi penjualan.
5. Pelanggan membeli produk.
6. Produk dimasukkan ke dalam transaksi.
7. Stok produk dikurangi sesuai jumlah pembelian.
8. Detail pembelian dibuat.
9. Total penjualan ditampilkan.
10. Menampilkan stok produk setelah penjualan.
11. Melakukan pengujian inheritance menggunakan `isinstance()` dan `issubclass()`.

## Contoh Produk

Produk yang digunakan dalam program yaitu:

- Bola Voli
- Sepatu Futsal
- Papan Skor Digital

Bola Voli dan Sepatu Futsal merupakan `ProdukOlahraga`, sedangkan Papan Skor Digital merupakan `ProdukElektronik`.

## Pengujian Inheritance

Program melakukan pengujian inheritance menggunakan `isinstance()` dan `issubclass()`.

`isinstance()` digunakan untuk mengecek apakah objek termasuk dari class tertentu. Sedangkan `issubclass()` digunakan untuk mengecek apakah suatu class merupakan subclass dari class lainnya.

Pengujian ini digunakan untuk memastikan bahwa `ProdukOlahraga` dan `ProdukElektronik` mewarisi class `Produk`.


## Kesimpulan

Pada Posttest 2 ini, program **Sistem Manajemen Penjualan dan Stok Toko Perlengkapan Olahraga** telah menerapkan tiga relasi UML yaitu **Association, Aggregation, dan Composition**.

Program juga telah menerapkan inheritance dengan `Produk` sebagai superclass serta `ProdukOlahraga` dan `ProdukElektronik` sebagai subclass. Kedua subclass menggunakan `super().__init__()`, memiliki atribut tambahan masing-masing, dan melakukan overriding pada method `tampilkan_info()`.

Selain itu, program menggunakan atribut protected `_stok` dan atribut private `__kode_produk` sesuai dengan ketentuan tingkat akses pada inheritance.
