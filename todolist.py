todolist = []

while True:
    print("\n===TO DO LIST===")
    print("1. Lihat Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if len(todolist) == 0:
            print("Belum ada tugas")
        else:
            print("\n--- daftar tugas ---")
            for i, tugas in enumerate(todolist):
                print(f"{i + 1}. {tugas}")
        input("\nTekan enter untuk kembali ke menu ")

    elif pilihan == "2":
        tugas = input("Masukan tugas baru: ")
        todolist.append(tugas)
        print("tugas berhasil ditambahkan")
        
    elif pilihan == "3":
        nomor = int(input("Masukan noomor tugas yang mau dihapus: "))
        if nomor <= len(todolist) and nomor > 0:
            todolist.pop(nomor - 1)
            print("Tugas dihapus")
        else:
            print("NOmor tidak valid")

    elif pilihan == "4":
        print("Program selesai")
        break
    else:
        print("pilihan tidak ada")
