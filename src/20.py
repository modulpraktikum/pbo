# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print "ID salah"
    else:
        judul_baru = raw_input("Judul baru: ")
        buku[indeks] = judul_baru