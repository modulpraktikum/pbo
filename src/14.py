# membuat variabel global
nama = "Petanikode"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print "Nama: %s" % nama
    print "Versi: %s" % versi


# mengakses variabel global
print "Nama: %s" % nama
print "Versi: %s" % versi

# memanggil fungsi help()
help()