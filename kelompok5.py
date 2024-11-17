class Reminder:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

    def display(self):
        return f"{self.title} - {self.description} pada {self.date} jam {self.time}"

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, title, description, date, time):
        reminder = Reminder(title, description, date, time)
        self.reminders.append(reminder)
        print(f"\nPengingat '{title}' berhasil ditambahkan.\n")

    def edit_reminder(self, index, title=None, description=None, date=None, time=None):
        if 0 <= index < len(self.reminders):
            reminder = self.reminders[index]
            reminder.title = title if title else reminder.title
            reminder.description = description if description else reminder.description
            reminder.date = date if date else reminder.date
            reminder.time = time if time else reminder.time
            print(f"\nPengingat '{reminder.title}' berhasil diubah.\n")
        else:
            print("\nPengingat tidak ditemukan.\n")

    def delete_reminder(self, index):
        if 0 <= index < len(self.reminders):
            removed_reminder = self.reminders.pop(index)
            print(f"\nPengingat '{removed_reminder.title}' berhasil dihapus.\n")
        else:
            print("\nPengingat tidak ditemukan.\n")

    def list_reminders(self):
        if not self.reminders:
            print("\nTidak ada pengingat yang tersimpan.\n")
        else:
            print("\nDaftar Pengingat:")
            for i, reminder in enumerate(self.reminders):
                print(f"{i + 1}. {reminder.display()}")
            print()

def main():
    manager = ReminderManager()
    
    while True:
        print("=== Aplikasi Reminder Sederhana ===")
        print("1. Tambah Pengingat")
        print("2. Edit Pengingat")
        print("3. Hapus Pengingat")
        print("4. Lihat Semua Pengingat")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            title = input("Masukkan judul pengingat: ")
            description = input("Masukkan deskripsi pengingat: ")
            date = input("Masukkan tanggal pengingat (YYYY-MM-DD): ")
            time = input("Masukkan waktu pengingat (HH:MM): ")
            manager.add_reminder(title, description, date, time)
        
        elif pilihan == "2":
            manager.list_reminders()
            try:
                index = int(input("Masukkan nomor pengingat yang ingin diedit: ")) - 1
                title = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
                description = input("Masukkan deskripsi baru (kosongkan jika tidak ingin mengubah): ")
                date = input("Masukkan tanggal baru (kosongkan jika tidak ingin mengubah): ")
                time = input("Masukkan waktu baru (kosongkan jika tidak ingin mengubah): ")
                manager.edit_reminder(index, title, description, date, time)
            except ValueError:
                print("\nInput tidak valid. Pastikan memasukkan angka.\n")

        elif pilihan == "3":
            manager.list_reminders()
            try:
                index = int(input("Masukkan nomor pengingat yang ingin dihapus: ")) - 1
                manager.delete_reminder(index)
            except ValueError:
                print("\nInput tidak valid. Pastikan memasukkan angka.\n")

        elif pilihan == "4":
            manager.list_reminders()
        
        elif pilihan == "5":
            print("\n=== Keluar dari Aplikasi. Terima kasih sudah menggunakan aplikasi ini.! ===")
            break
        
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
