import random

angka_rahasia = random.randint(1, 20)

print("coba tebak angkanya")
print("saya menyimpan angka dari 1 sampai 20")

tebakan = 0

while tebakan !=angka_rahasia:
    tebakan = int(input("tebak angka: "))

    if tebakan < angka_rahasia:
        print("terlalu kecil")
    elif tebakan > angka_rahasia:
        print("terlalu besar")
    else:
        print("kamu benar!!!!")