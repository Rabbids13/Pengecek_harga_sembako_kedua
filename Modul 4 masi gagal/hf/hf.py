
print ("Program pengecekan harga barang di toko") 
def ayam (jumlahayam='30.000/Kg'):
    print ("Berapa Kilo ayam yang anda mau cek harganya : ")
    jumlahayam = float(input())
    totalayam = 30000 * jumlahayam
    print ("Harga ayam ", jumlahayam,"Kg adalah", totalayam, "Rupiah")
    return totalayam

def beras (jumlahberas='12.000/Kg'):
    print ("Berapa Kilo beras yang anda mau cek harganya : ")
    jumlahberas = float(input())
    totalberas = 12000  * jumlahberas
    print ("Harga beras ", jumlahberas,"Kg adalah", totalberas, "Rupiah")
    return totalberas

def minyak (jumlahminyak='11.000/Liter') :
    print ("Berapa liter minyak yang anda mau cek harganya : ")
    jumlahminyak = float(input())
    totalminyak = 11000 * jumlahminyak
    print ("Harga minyak ", jumlahminyak,"Liter adalah", totalminyak, "Rupiah")
    return totalminyak

def telur (jumlahtelur='25.000/Kg') :
    print ("Berapa kilo telur yang anda mau cek harganya : ")
    jumlahtelur = float(input())
    totaltelur = 25000 * jumlahtelur
    print ("Harga telur ", jumlahtelur,"Kg adalah", totaltelur, "Rupiah")
    return totaltelur

def tepung (jumlahtepung='9.000/Kg') :
    print ("Berapa kilo tepung yang anda mau cek harganya : ")
    jumlahtepung = float(input())
    totaltepung = 9000 * jumlahtepung
    print ("Harga tepung ", jumlahtepung,"Kg adalah", totaltepung, "Rupiah")
    return totaltepung

def gula (jumlahgula='15.000/Kg') :
    print ("Berapa kilo gula yang anda mau cek harganya : ")
    jumlahgula = float(input())
    totalgula = 15000 * jumlahgula
    print ("Harga gula ", jumlahgula,"Kg adalah", totalgula, "Rupiah")
    return totalgula

def thanks () :
   print ("Terima kasih sudah mengecek harga dengan aplikasi kami")
pilihan = 'y'
while (pilihan != 'n'):
    print ("Pilih Barang yang ingin di cek : ")
    print ("1. Ayam")
    print ("2. Beras")
    print ("3. Minyak")
    print ("4. Telur")
    print ("5. Tepung")
    print ("6. Gula")
    print ("7. Beli")

    a = float (input("Masukan barang yang ingin di cek harganya : "))
    if (a == 1) :
        ayam()
    elif (a==2) :
       beras()
    elif (a==3) :
        minyak()
    elif (a==4) :
        telur()
    elif (a==5) :
        tepung()
    elif (a==6) :
        gula ()
    elif (a==7) :
        from class1 import domino

    else :
        print ("Masukan yang anda masukan salah")    
    pilihan = input("Apakah Anda ingin mengulangi lagi (y/n)?")
thanks() 