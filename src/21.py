# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = input("Inputkan ID buku: ")
    if(indeks > len(buku)):
        print "ID salah"
    else:
        buku.remove(buku[indeks])