import re
import os.path
from collections import Counter

os.system('cls')

print('PROGRAM MENGHITUNG FREKUENSI KARAKTER DARI SEBUAH TEKS DOKUMENT')
print('Made Yayang Eka Prananda')
print('1808561110 \n')

document = input('Nama dokumen : ')

# di cek apabila user input nama dokumen tanpa txt
if(document.find('.txt') == -1):
    document = document+'.txt'

# mencari nama file
if (os.path.exists(document)):
    a = bool(1)
    print('\n-----------File Tersedia-----------\n')
else:
    print('EROR! File Yang Anda Masukkan Tidak Ada!')
    exit()

if (os.path.exists(document)):
    # Membuka dokumen
    file = open(document, 'r+')
# Membaca line pertama pada dokumen
string = ((' ').join(line.strip() for line in file))

# Convert ke lower string
mystring = string.lower()

# Cek Alfabet
cek_kata = re.compile('[^a-z]')
mystring = cek_kata.sub('', mystring)

# Menganalisa n (banyak karakter) dengan dokumen
n = int(input('Banyak karakter yang di analisa : '))
frekuensi = {}
array = [(mystring[i:i + n]) for i in range(0, len(mystring), n)]
frekuensi = Counter(array)

# Mencetak output
print('\nHasil :')
counter = 0
for i in sorted(frekuensi):
    counter += 1
    print('Karakter: ' + i + ',\t| Karakter Yang Sama: ' +
          str(frekuensi[i]) + ',\t| Peluang : ' + str(1/int(frekuensi[i])))
print('Jumlah Silabel atau Total Karakter Keseluruhan: ' + str(counter))
