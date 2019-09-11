# fungsi untuk menampilkan menu
def show_menu():
    print "\n"
    print "----------- MENU ----------"
    print "[1] Show Data"
    print "[2] Insert Data"
    print "[3] Edit Data"
    print "[4] Delete Data"
    print "[5] Exit"
    
    menu = input("PILIH MENU> ")
    print "\n"

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print "Salah pilih!"