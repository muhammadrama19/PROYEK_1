import os


def printheader():
    print("+======================================================================================+")
    print("||   _____  _                      ____              _                                ||")
    print("||  |  __ \| |                    |  _ \            | |        /\                     ||")
    print("||  | |__) | |__   ___  _ __   ___| |_) | ___   ___ | | __    /  \   _ __  _ __       ||")
    print("||  |  ___/| '_ \ / _ \| '_ \ / _ \  _ < / _ \ / _ \| |/ /   / /\ \ | '_ \| '_ \      ||")
    print("||  | |    | | | | (_) | | | |  __/ |_) | (_) | (_) |   <   / ____ \| |_) | |_) |     ||")
    print("||  |_|    |_| |_|\___/|_| |_|\___|____/ \___/ \___/|_|\_\ /_/    \_\ .__/| .__/      ||")
    print("||                                                                  | |   | |         ||")
    print("||                                                                  |_|   |_|         ||")
    print("+======================================================================================+")
    print("                                                   created by: Muhammad Rama Nurimani")
    print("                                                                            221524021\n")
    print("Masukan pilihan anda:")
    print("1. Buat Kontak")
    print("2. Tampilkan Kontak")
    print("3. Perbaharui Kontak")
    print("4. Hapus Kontak")
    print("5. Cari Kontak")
    print("6. Keluar")


def load_phonebook():
    phonebook = {}
    try:
        with open("phonebook.txt", "r") as f:
            for line in f:
                if "," in line:
                    name, phone_number = line.strip().split(",")
                    phonebook[name] = phone_number
    except FileNotFoundError:
        pass
    return phonebook


def save_phonebook(phonebook):
    with open("phonebook.txt", "w") as f:
        for name, phone_number in phonebook.items():
            f.write(f"{name},{phone_number}\n")


def create_contact(name, phone_number):
    phonebook = load_phonebook()
    if name in phonebook:
        print("Kontak dengan nama tersebut sudah ada")
        return
    phonebook[name] = phone_number
    save_phonebook(phonebook)
    print(f"Kontak {name} telah dibuat dengan nomor:{phone_number}")


def printform():
    print("=================================================================================")
    print("                                 PHONEBOOK                                        ")
    print("=================================================================================")
    print("NO.|             NAMA             |          PHONE NUMBER          |")
    print("---------------------------------------------------------------------------------")


def read_phonebook():
    printform()
    if os.path.isfile("phonebook.txt"):
        with open("phonebook.txt", "r") as f:
            i = 1
            for line in f:
                if "," in line:
                    name, phone_number = line.strip().split(",")
                    print(f"{i:>2}.| {name:<28} | {phone_number:<30} |")
                    i += 1
    else:
        print("Phonebook file tidak ada")


def update_contact(name, phone_number):
    phonebook = load_phonebook()
    name_lower = name.lower()
    if name_lower in [n.lower() for n in phonebook.keys()]:
        for contact in phonebook:
            if contact.lower() == name_lower:
                phonebook[contact] = phone_number
                break
        save_phonebook(phonebook)
        print(f"Kontak {name} sudah diupdate menjadi {phone_number}")
    else:
        print(f"Kontak {name} tidak ada")

def delete_contact(name):
    phonebook = load_phonebook()
    name_lower = name.lower()
    if name_lower in [n.lower() for n in phonebook.keys()]:
        for contact, number in phonebook.items():
            if contact.lower() == name_lower:
                del phonebook[contact]
                save_phonebook(phonebook)
                print(f"Kontak {name} terhapus")
                return
    else:
        print(f"Kontak {name} tidak ada")


def search_contact(name):
    phonebook = load_phonebook()
    name_lower = name.lower()
    results = [number for contact, number in phonebook.items()
               if contact.lower() == name_lower]
    if results:
        print(f"Kontak dengan nama {name}:")
        for number in results:
            print(f"{name}: {number}")
    else:
        print(f"Tidak ada kontak dengan nama {name}")

def main():
    run_program = True
    while run_program:
        printheader()
        choice = input(": ")
        if choice == "1":
            name = input("Masukan Nama: ")
            phone_number = input("Masukan Nomor: ")
            create_contact(name, phone_number)
        elif choice == "2":
            os.system('cls')
            read_phonebook()
            input("Click Enter untuk next")
        elif choice == "3":
            name = input("Masukan Nama: ")
            phone_number = input("Masukan Nomor: ")
            update_contact(name, phone_number)
        elif choice == "4":
            name = input("Masukan Nama: ")
            delete_contact(name)
        elif choice == "5":
            name = input("Masukan Nama: ")
            search_contact(name)
        elif choice == "6":
            run_program = False
            print("Program selesai. Apakah Anda ingin menjalankannya lagi? (Y/N)")
            user_choice = input(": ")
            if user_choice.lower() == "y":
                main()
        else:
            print("Invalid choice ulangi!")

main()
