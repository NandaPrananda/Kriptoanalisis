import os
loop = "y"

while loop == "y" or loop == "Y":
    os.system('cls')
    print("==============================================================")
    print("Tugas Kriptoanalisis")
    print("Made Yayang Eka Prananda")
    print("1808561110")
    print("==============================================================")
    print("Pilihan : ")
    print("1. Cek Bilangan Prima")
    print("2. Faktorial")
    print("3. FPB")
    pilihan = int(input("Masukan pilihan : "))
    if pilihan is 1:
        prima = 0
        angka = int(input("Masukan Angka : "))
        for i in range(1, angka+1):
            if (angka % i) is 0:
                prima += 1
        if (prima <= 2):
            print(angka, "merupakan bilangan prima")
        else:
            print(angka, "bukan merupakan bilangan prima")

    elif pilihan is 2:
        faktorial = 1
        angka = int(input("Masukan Angka : "))
        for i in range(1, angka+1):
            faktorial = faktorial*i
        print("Faktorial dari", angka, "adalah", faktorial)

    elif pilihan is 3:
        angka1 = int(input("Masukan Angka Pertama : "))
        angka2 = int(input("Masukan Angka Kedua: "))
        if(angka1 < angka2):
            kecil = angka1
        else:
            kecil = angka2

        for i in range(1, kecil+1):
            if angka1 % i == 0 and angka2 % i == 0:
                fpb = i
        print("FPB dari", angka1, "dan", angka2, "adalah", fpb)
    else:
        print("Pilihan tidak tersedia")

    loop = input("Lanjut[y/n] : ")

print("==============================================================")
print("Terimakasih Sudah Menggunakan Program Ini")
