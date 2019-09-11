#merupakan sebuah class dengan metode untuk mencari jumlah huruf vokal
class pencariHuruf() :
    def __init__(self, teks):
        self.kata = teks
        self.a = 0
        self.i = 0
        self.u = 0
        self.e = 0
        self.o = 0
    def A (self) :
        for i in range(len(self.kata)):
            if self.kata[i] == 'a' or self.kata[i] == 'A' :
                self.a = self.a + 1
        return self.a
    def I (self) :
        for i in range(len(self.kata)):
            if self.kata[i] == 'i' or self.kata[i] == 'i' :
                self.i = self.i + 1
        return self.i
    def U (self) :
        for i in range(len(self.kata)):
            if self.kata[i] == 'u' or self.kata[i] == 'u' :
                self.u = self.u + 1
        return self.u
    def E (self) :
        for i in range(len(self.kata)):
            if self.kata[i] == 'e' or self.kata[i] == 'e' :
                self.e = self.e + 1
        return self.e
    def O (self) :
        for i in range(len(self.kata)):
            if self.kata[i] == 'o' or self.kata[i] == 'o' :
                self.o = self.o + 1
        return self.o

#proses pemanggilan dan penampungan class "pencariHuruf"
teks = 'ma mi mu me mo'
penampung = pencariHuruf(teks)

#pemanggilan metode yang ada di class "pencariHuruf"
jumlahA = penampung.A()
jumlahI = penampung.I()
jumlahU = penampung.U()
jumlahE = penampung.E()
jumlahO = penampung.O()

#mencetak hasil proses yang di tampung di dalam variabel di atas.
print(jumlahA)
print(jumlahI)
print(jumlahU)
print(jumlahE)
print(jumlahO)