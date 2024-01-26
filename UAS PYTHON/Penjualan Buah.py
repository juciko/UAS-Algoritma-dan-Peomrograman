# Buat daftar nama dan harga buah
fruits = [("Apel", 2000), ("Mangga", 3000), ("Pisang", 1500), ("Kiwi", 2500)]

# Buat fungsi untuk menampilkan daftar buah
def display_fruits():
  print("Daftar Buah:")
  for i, fruit in enumerate(fruits):
    print(f"{i+1}. {fruit[0]} - Rp{fruit[1]}")

# Buat fungsi untuk memproses pembelian
def process_purchase():
  # Tampilkan daftar buah
  display_fruits()

  # Minta input dari pengguna
  fruit_index = int(input("Pilih buah yang ingin dibeli (masukkan nomor): "))
  fruit_quantity = int(input("Masukkan jumlah yang ingin dibeli: "))

  # Cari buah yang dipilih
  chosen_fruit = fruits[fruit_index-1]

  # Hitung total harga
  total_price = chosen_fruit[1] * fruit_quantity

  # Tampilkan total harga
  print(f"Total harga: Rp{total_price}")

  # Minta input pembayaran dari pengguna
  payment = int(input("Masukkan jumlah pembayaran: Rp"))

  # Hitung kembalian
  change = payment - total_price
  print(f"Kembalian: Rp{change}")

# Buat fungsi untuk menampilkan laporan penjualan
def display_sales_report():
  total_sales = 0
  for fruit in fruits:
    total_sales += fruit[1]
  print(f"Total penjualan hari ini: Rp{total_sales}")

# Buat fungsi utama
def main():
  while True:
    # Tampilkan menu
    print("Selamat datang di toko buah kami!")
    print("1. Lihat daftar buah")
    print("2. Lakukan pembelian")
    print("3. Lihat laporan penjualan")
    print("4. Keluar")
    choice = int(input("Masukkan pilihan Anda (1-4): "))

    if choice == 1:
      display_fruits()
    elif choice == 2:
      process_purchase()
    elif choice == 3:
      display_sales_report()
    else:
      break

# Panggil fungsi utama
main()