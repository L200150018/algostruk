####def cariLurus( wadah, target ):
####    n = len( wadah )
####    for i in range( n ):
####        if wadah[i] == target:
####            return True
####    return False
##
##class MhsTIF(object):
##    def __init__(self, nama, nim, kota, us):
##        self.nama = nama
##        self.nim = nim
##        self.kota = kota
##        self.uangSaku = us
##
##    def __str__(self):
##        s = self.nama + ', nim ' + str(self.nim)\
##            + '. Tinggal di ' + self.kota\
##            + '. Uang saku Rp ' + str(self.uangSalu)\
##            + '. tiap bulannya.'
##        return s
##    
##c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
##c1 = MhsTIF("Budi", 51, "Sragen", 230000)
##c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
##c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
##c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
##c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
##c6 = MhsTIF("Deni", 13, "Klaten", 245000)
##c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
##c8 = MhsTIF("Janto", 23, "Klaten", 245000)
##c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
##c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)
##
##Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
##
##def cariAsal():
##    target = 'Klaten'
##    for i in Daftar:
##        if i.kota == target:
##            print(i.nama + ' tinggal di ' + target)
##
##
##
##def cariTerkecil(kumpulan):
##    n = len(kumpulan)
##    terkecil = kumpulan[0]
##    for i in range(1, n):
##        if kumpulan[i] < terkecil:
##            terkecil = kumpulan[i]
##    return terkecil
##
##kumpulan = [2, 5, 753, 24, 25, 3, 5, 7, 12]
##cariTerkecil(kumpulan)


def binSe(kumpulan, target):
    # Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    # Secara berulang belah runtutan itu menjadi separuhnya
    # sampai targetnya ditemukan
    while low <= high:
        # Temukan pertengahan runtut itu
        mid = (high + low) // 2
        # Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            return True
        # ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        # ataukah targetnya di sebelah kanannya?
        else:
            low = mid + 1
        # Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False
