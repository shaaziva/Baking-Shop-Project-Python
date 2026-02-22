# ˙ . ꒷ 🍰 . 𖦹˙—
# PROGRAM BAKING SHOP
# ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹

daftar_kue = {
    1: {"nama": "ꜰʀɪᴇᴅ ᴜʙᴇᴇ", "harga": 20000},
    2: {"nama": "ꜱᴀʟᴛ ʙʀᴇᴀᴅ", "harga": 10000},
    3: {"nama": "Cheesecake", "harga": 25000}
}

data_transaksi = []

def tampil_kue():
    print("⋆.𐙚 ̊ CAKE LIST")
    for kode in daftar_kue:
        print(kode, ".", 
              daftar_kue[kode]["nama"], 
              "- Rp", 
              daftar_kue[kode]["harga"])


def tambah_transaksi():
    try:
        tampil_kue()
        pilih = int(input("Choose cake number: "))
        jumlah = int(input("Jumlah beli: "))

        if pilih in daftar_kue:
            nama = daftar_kue[pilih]["nama"]
            harga = daftar_kue[pilih]["harga"]
            total = harga * jumlah

            transaksi = {
                "nama": nama,
                "jumlah": jumlah,
                "total": total
            }

            data_transaksi.append(transaksi)
            print("Transaksi berhasil ditambahkan!")
        else:
            print("Nomor Kue tidak ada .ᐟ.ᐟ")

    except:
        print("INPUT HARUS ANGKA")


def lihat_transaksi():
    print("⋆.𐙚 ̊  DATA TRANSAKSI")
    if len(data_transaksi) == 0:
        print("Belum ada transaksi.")
    else:
        for i in range(len(data_transaksi)):
            print(i+1, ".", 
                  data_transaksi[i]["nama"], 
                  "-", data_transaksi[i]["jumlah"], 
                  "pcs - Rp", 
                  data_transaksi[i]["total"])


def hitung_total():
    total = 0
    for i in range(len(data_transaksi)):
        total = total + data_transaksi[i]["total"]

    print("Total semua belanja: Rp", total)


def simpan_file():
    if len(data_transaksi) == 0:
        print("Belum ada transaksi untuk disimpan.")
        return

    with open("data_transaksi.txt", "a") as file:
        for i in range(len(data_transaksi)):
            file.write(data_transaksi[i]["nama"] + " | ")
            file.write(str(data_transaksi[i]["jumlah"]) + " pcs | ")
            file.write("Rp" + str(data_transaksi[i]["total"]) + "\n")

    print("Data berhasil disimpan!")


def menu():
    while True:
        print("  Bake Shop  ꒷ 🍰 ")
        print("1. Lihat Daftar Kue")
        print("2. Tambah Transaksi")
        print("3. Lihat Transaksi")
        print("4. Hitung Total")
        print("5. Simpan ke File")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))

            if pilih == 1:
                tampil_kue()
            elif pilih == 2:
                tambah_transaksi()
            elif pilih == 3:
                lihat_transaksi()
            elif pilih == 4:
                hitung_total()
            elif pilih == 5:
                simpan_file()
            elif pilih == 6:
                print("Thank u for Order")
                break
            else:
                print("Menu tidak tersedia!")

        except:
            print("Masukkan angka ya!")

menu()