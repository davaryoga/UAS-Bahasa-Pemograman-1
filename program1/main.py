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