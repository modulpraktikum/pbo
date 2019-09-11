# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print "BELUM ADA DATA"
    else:
        for indeks in range(len(buku)):
            print "[%d] %s" % (indeks, buku[indeks])