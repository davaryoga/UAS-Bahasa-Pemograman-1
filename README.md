# UAS-Bahasa-Pemograman
```
Nama  : Muhammad Dava Aryoga
NIM   : 312110552
Kelas : TI.21.C.3
Prodi : Teknik Informatika
```
![Screenshot (87)](https://user-images.githubusercontent.com/92939686/149641142-a1f6c741-0cd4-4fd0-9e4c-91562f02cced.png)

## daftar_nilai.py
```python
from view.input_nilai import *

dataMahasiswa = {}


def tambah_data():
    global dataMahasiswa
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUts()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Berhasil Ditambahkan!")
    return dataMahasiswa

def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in dataMahasiswa.keys():
        nim = input_nim()
        nilaiTugas = input_nilaiTugas()
        nilaiUts = input_nilaiUts()
        nilaiUas = input_nilaiUas()
        nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Di Ubah!")
    else:
        print("Data tidak ditemukan!")


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in dataMahasiswa.keys():
        del dataMahasiswa[nama]
        print("Data",nama, "Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nama))
 ```
daftar_nilai.py berisi modul untuk `tambah_data`, `ubah_data`, `hapus_data`, dan `cari_data`.
1. `tambah_data` digunakan untuk menambahkan/menginput data ke dalam `library`
2. `ubah_data` digunakan untuk mengubah data yang sudah ada di dalam `library`
3. `hapus_data` digunakan untuk menghapus/menghilangkan data di dalam `library`
4. `cari_data` digunakan untuk mencari/menemukan data yang terdapat didalam `library`

## input_nilai.py
```python
def input_nama():
    global nama
    nama = input("Masukkan Nama        : ")
    return nama


def input_nim():
    global nim
    nim = input("Masukkan NIM         : ")
    return nim


def input_nilaiTugas():
    global nilaiTugas
    nilaiTugas = int(input("Masukkan Nilai Tugas : "))
    return nilaiTugas


def input_nilaiUts():
    global nilaiUts
    nilaiUts = int(input("Masukkan Nilai UTS   : "))
    return nilaiUts


def input_nilaiUas():
    global nilaiUas
    nilaiUas = int(input("Masukkan Nilai UAS   : "))
    return nilaiUas
```
`input_nilai.py` berisi modul untuk `input_data` yang meminta pengguna memasukkan data. Nantinya data yang diinput akan masuk ke `library`. Data-data yang harus diinput yaitu:
1. Nama
2. NIM
3. Nilai Tugas
4. Nilai UTS
5. Nilai UAS

## view_nilai.py
```python
rom model.daftar_nilai import *


def cetak_daftar_nilai():
    if dataMahasiswa.items():
        print("\n                    DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        i = 0
        for x in dataMahasiswa.items():
            i += 1
            print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("==================================================================")
    else:
        print("\n                    DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        print("|                        TIDAK ADA DATA!                         |")
        print("==================================================================")


def cetak_hasil_pencarian():
    nama = input("Masukkan Nama        : ")
    if nama in dataMahasiswa.keys():
        print("\n                   DAFTAR NILAI MAHASISWA                   ")
        print("==============================================================")
        print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
        print("==============================================================")
        print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6}  |".format(nama, dataMahasiswa[nama][0], dataMahasiswa[nama][1], dataMahasiswa[nama][2], dataMahasiswa[nama][3], dataMahasiswa[nama][4]))
        print("==============================================================")
    else:
        print("Datanya {0} Tidak Ada ".format(nama))
```
`view_nilai.py` berisi modul untuk `cetak_daftar_nilai`, `cetak_hasil_pencarian`. Nantinya `cetak_daftar_nilai` berisi nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS, dan Nilai Akhir. Nilai Akhir merupakan Nilai rata-rata Yang dimana diakumulasi dari Nilai Tugas, Nilai UTS, dan Nilai UAS.

## main.py
```python
from view import *


def menu():
    print('=====================================')
    print('    Pustaka Data Nilai Mahasiswa')
    print('     Universitas Pelita Bangsa')
    print('=====================================')
    print('|    1. Tambah Data                 |')
    print('|    2. Cari Data                   |')
    print('|    3. Tampilkan Data Mahasiswa    |')
    print('|    4. Ubah Data Mahasiswa         |')
    print('|    5. Hapus Data Mahasiswa        |')
    print('|    6. Selesai                     |')
    print('=====================================')


while True:
    menu()
    choose = input('Pilih Menu  : ')

    if choose == '1':
        tambah_data()
        input('Untuk kembali ke menu utama, tekan enter')

    elif choose == '2':
        cetak_hasil_pencarian()
        input('Untuk kembali ke menu utama, tekan enter')

    elif choose == '3':
        cetak_daftar_nilai()
        input('Untuk kembali ke menu utama, tekan enter')

    elif choose == '4':
        ubah_data()
        input('Untuk kembali ke menu utama, tekan enter')

    elif choose == '5':
        hapus_data()
        input('Untuk kembali ke menu utama, tekan enter')

    elif choose == '6':
        exit()



    else:
        print("Menu yang anda maksud tidak tersedia, Silahkan pilih menu yang tersedia")
```
`main.py` berisi program utama (menu pilihan yang memanggil semua menu yang ada). Program ini merupakan inti dari semua modul yang terdapat didalam `package`.Menu-menu yang disajikan ada 6 yaitu:
1. Tambah data
2. Cari data
3. Tampilkan Data Mahasiswa
4. Ubah Data Mahasiswa
5. Hapus Data Mahasiswa
6. Selesai

Jika program dijalankan akan ditampilkan seperti berikut:

![Screenshot (88)](https://user-images.githubusercontent.com/92939686/149641077-0286dfad-aefa-42c4-b25c-b72401949ceb.png)

- Kemudain kita pilih menu 1 untuk menambahkan data, ketik 1 kemudian tekan enter. Setelah menu dipilih kita akan diperintahkan untuk menginput Nama, NIM, Nilai UTS, dan, Nilai UAS

![Screenshot (89)](https://user-images.githubusercontent.com/92939686/149641127-0b6f2581-71d1-4a2a-b308-93bf04cfcde3.png)

- tekan enter untuk kembali ke menu utama
- Pilih menu nomor 2 untuk mencari data yang sudah diinput, ketik 2 lalu tekan enter. Setelah menu dipilih kita akan diperintahkan untuk memasukan nama, kemudian akan ditampilkan data yang dicari

![Screenshot (92)](https://user-images.githubusercontent.com/92939686/149641176-05146d78-8a3f-4ac7-b0e8-327867136e41.png)

- tekan enter untuk kembali ke menu utama
- Pilih menu nomor 3 untuk menampilkan semua data yang sudah diinput, ketik 3 lalu tekan enter. Setelah menu dipilih akan ditampilkan semua data yang terdapat didalam `library`

![Screenshot (91)](https://user-images.githubusercontent.com/92939686/149641197-5f46da0b-ef4f-4476-a256-36f72b8e2ebb.png)

- Tekan enter untuk kembali ke menu utama
- Pilih menu nomor 4 untuk mengubah data yang terdapat di dalam `library`, ketik 4 lalu tekan enter. Setelah menu dipilih kita akan diperintahkan untuk menginput Nama, Nilai Tugas, Nilai UTS, dan Nilai UAS yang mau diubah

![Screenshot (93)](https://user-images.githubusercontent.com/92939686/149641224-28617929-d753-4add-ae94-13f94976054f.png)

- Tekan enter untuk kembali ke menu utama
- Pilih Menu nomor 5 untuk menghapus data yang terdapat di dalam `library`, ketik 5 lalu teklan enter. Setelah menu dipilih kita diperintahkan untuk memasukan Nama yang akan dihapus

![Screenshot (94)](https://user-images.githubusercontent.com/92939686/149641393-9ee65c96-8bc0-46b2-8b65-0ae6f52d5f4b.png)

- Kemudian pilih 6 untuk mengakhiri program, ketik 6 lalu tekan enter

## Sekian Terima kasih








      
