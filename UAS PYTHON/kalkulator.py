#fungsi rumus
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

#minta user pilih operasi
while True:
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")


    #minta user memasukan angka
    if pilihan in ('1', '2', '3', '4'):
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        #fungsi utama
        if pilihan == '1':
            print(angka1, "+", angka2, "=", tambah(angka1, angka2))

        elif pilihan == '2':
            print(angka1, "-", angka2, "=", kurang(angka1, angka2))

        elif pilihan == '3':
            print(angka1, "*", angka2, "=", kali(angka1, angka2))

        elif pilihan == '4':
            print(angka1, "/", angka2, "=", bagi(angka1, angka2))

    elif pilihan == '5':
        print("Keluar dari kalkulator.")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")