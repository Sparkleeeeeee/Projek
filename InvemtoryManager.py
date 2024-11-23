class Item:
    def __init__(self, nama, jumlah, harga):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def __str__(self):
        return f"Item: {self.nama}, Jumlah: {self.jumlah}, Harga: {self.harga}"

class ManajerInventaris:
    def __init__(self):
        self.inventaris = []

    def tambah_item(self, item):
        self.inventaris.append(item)
        print(f"Item '{item.nama}' telah ditambahkan ke inventaris.")

    def edit_item(self, nama_item, jumlah_baru=None, harga_baru=None):
        for item in self.inventaris:
            if item.nama == nama_item:
                if jumlah_baru is not None:
                    item.jumlah = jumlah_baru
                if harga_baru is not None:
                    item.harga = harga_baru
                print(f"Item '{nama_item}' telah diperbarui.")
                return
        print(f"Item '{nama_item}' tidak ditemukan dalam inventaris.")

    def hapus_item(self, nama_item):
        for item in self.inventaris:
            if item.nama == nama_item:
                self.inventaris.remove(item)
                print(f"Item '{nama_item}' telah dihapus dari inventaris.")
                return
        print(f"Item '{nama_item}' tidak ditemukan dalam inventaris.")

    def lihat_inventaris(self):
        if not self.inventaris:
            print("Inventaris kosong.")
            return
        print("Inventaris Saat Ini:")
        for item in self.inventaris:
            print(item)

def main():
    manajer = ManajerInventaris()

    while True:
        print("\nMenu:")
        print("1. Tambah Item")
        print("2. Edit Item")
        print("3. Hapus Item")
        print("4. Lihat Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama item: ")
            jumlah = int(input("Masukkan jumlah item: "))
            harga = float(input("Masukkan harga item: "))
            item = Item(nama, jumlah, harga)
            manajer.tambah_item(item)

        elif pilihan == '2':
            nama = input("Masukkan nama item yang ingin diedit: ")
            jumlah_baru = input("Masukkan jumlah baru (biarkan kosong untuk mempertahankan yang lama): ")
            harga_baru = input("Masukkan harga baru (biarkan kosong untuk mempertahankan yang lama): ")

            jumlah_baru = int(jumlah_baru) if jumlah_baru else None
            harga_baru = float(harga_baru) if harga_baru else None

            manajer.edit_item(nama, jumlah_baru, harga_baru)

        elif pilihan == '3':
            nama = input("Masukkan nama item yang ingin dihapus: ")
            manajer.hapus_item(nama)

        elif pilihan == '4':
            manajer.lihat_inventaris()

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()