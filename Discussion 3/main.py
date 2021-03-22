import re
import os.path
import os
from collections import Counter


def menu():
    os.system('cls')
    print('==================================================')
    print("Made Yayang Eka Prananda")
    print("1808561110")
    print('==================================================')
    print("\nMENU:")
    print("1. Cek Dokumen")
    print("2. Cek Statistik Karakter Pada Dokumen")
    print("3. Mengganti Karakter Pada Dokumen")
    print("0. Keluar")


def pilihmenu():
    menu = int(input("\nPilih Menu: "))
    if menu == 1:
        cek_dokumen()
    elif menu == 2:
        cek_statistik()
    elif menu == 3:
        ganti_karakter()
    elif menu == 0:
        exit()
    else:
        print("EROR! Menu Tidak Ada!")
        pilihmenu()


def cek_dokumen():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        file = open(dokumen_file, 'r')
        teks = file.read()
        print("\nIsi Dokumen:")
        print(teks)
        file.close()
    else:
        print("\nEROR! Dokumen Tidak Ada!")
        cek_dokumen()


def cek_statistik():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        file = open(dokumen_file, 'r')
    else:
        print("\nEROR! Dokumen Tidak Ada!")
        cek_statistik()
    string = ((' ').join(line.strip() for line in file))
    mystring = string.lower()
    cek_kata = re.compile('^.')
    mystring = cek_kata.sub('', mystring)
    n = 1
    array = [(mystring[i:i + n]) for i in range(0, len(mystring), n)]
    frekuensi = Counter(array)
    print('\nHasil Statistik:')
    counter = 0
    for i in sorted(frekuensi):
        counter += 1
        print('Karakter: ' + i + ',\t| Frekuensi: ' + str(frekuensi[i]) + ',\t| Peluang : ' + str(
            1 / int(frekuensi[i])))
    print('Total Karakter: ' + str(counter))
    file.close()


def ganti_karakter():
    dokumen_file = input("\nMasukkan Nama Dokumen : ")
    if (dokumen_file.find(".txt") == -1):
        dokumen_file = dokumen_file + ".txt"
    if (os.path.exists(dokumen_file)):
        with open(dokumen_file) as carikarakter:
            karaktersebelum = input("\nKarakter Yang Diganti : ")
            if karaktersebelum in carikarakter.read():
                karaktersesudah = input(
                    "\nKarakter (" + karaktersebelum + ") Diganti Dengan : ")
                with open(dokumen_file, 'r+') as karakter:
                    file = karakter.read()
                    file = re.sub(karaktersebelum, karaktersesudah, file)
                    karakter.seek(0)
                    karakter.write(file)
                    karakter.truncate()
            else:
                print("\nEROR! Karakter Yang Akan Dicari Tidak Ada!")
                ganti_karakter()
    else:
        print("\nEROR! Dokumen Tidak Ada!")
        ganti_karakter()


def keluar():
    print("\nTerima Kasih Sudah Menggunakan Program Ini")
    exit()


def main():
    menu()
    pilihmenu()
    loop = input("\nLanjut?[y/n]")
    if loop == 'y':
        main()
    elif loop == 'n':
        exit()
    else:
        print('Pilihan Salah')
        exit()


main()
