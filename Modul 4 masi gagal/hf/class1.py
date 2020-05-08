class Domino(object):
    
    def pembeliansembako():
        print ("Program pengecekan harga barang di toko") 
        def ayam (jumlahayam='30.000/Kg'):
            print ("Berapa Kilo ayam yang anda mau cek harganya : ")
            jumlahayam = float(input())
            totalayam = 30000 * jumlahayam
            print ("Harga ayam ", jumlahayam,"Kg adalah", totalayam, "Rupiah")
            a =input("apakah anda ingin membeli", jumlahayam, "kg dengan seharga",totalayam,"? (y/n")
        if (a == y) :
            totalayam()
        else :
            return totalayam
                    

        def beras (jumlahberas='12.000/Kg'):
            print ("Berapa Kilo beras yang anda mau cek harganya : ")
            jumlahberas = float(input())
            totalberas = 12000  * jumlahberas
            print ("Harga beras ", jumlahberas,"Kg adalah", totalberas, "Rupiah")
            b =input("apakah anda ingin membeli", jumlahberas, "kg dengan seharga",totalberas,"?(y/n)")
        if (b == y) :
            totalberas()
        else :
            return totalberas

        def minyak (jumlahminyak='11.000/Liter') :
            print ("Berapa liter minyak yang anda mau cek harganya : ")
            jumlahminyak = float(input())
            totalminyak = 11000 * jumlahminyak
            print ("Harga minyak ", jumlahminyak,"Liter adalah", totalminyak, "Rupiah")
            c =input("apakah anda ingin membeli", jumlahminyak, "Liter dengan seharga",totalminyak,"?(y/n)")
        if (c == y) :
            totalminyak()
        else :
            return totalminyak

        def telur (jumlahtelur='25.000/Kg') :
            print ("Berapa kilo telur yang anda mau cek harganya : ")
            jumlahtelur = float(input())
            totaltelur = 25000 * jumlahtelur
            print ("Harga telur ", jumlahtelur,"Kg adalah", totaltelur, "Rupiah")
            d =input("apakah anda ingin membeli", jumlahtelur, "kg dengan seharga",totaltelur,"?")
        if (d == y) :
            totaltelur()
        else :
            return totaltelur

        def tepung (jumlahtepung='9.000/Kg') :
            print ("Berapa kilo tepung yang anda mau cek harganya : ")
            jumlahtepung = float(input())
            totaltepung = 9000 * jumlahtepung
            print ("Harga tepung ", jumlahtepung,"Kg adalah", totaltepung, "Rupiah")
            e =input("apakah anda ingin membeli", jumlahtepung, "kg dengan seharga",totaltepung,"?")
        if (e == y) :
            totaltepung()
        else :
            return totaltepung

        def gula (jumlahgula='15.000/Kg') :
            print ("Berapa kilo gula yang anda mau cek harganya : ")
            jumlahgula = float(input())
            totalgula = 15000 * jumlahgula
            print ("Harga gula ", jumlahgula,"Kg adalah", totalgula, "Rupiah")
            f =input("apakah anda ingin membeli", jumlahgula, "kg dengan seharga",totalgula,"?")
        if (f == y) :
            totalgula()
        else :
            return totalgula

        def thanks () :
            print ("Terima kasih sudah membeli produk kami")
            pilihan = 'y'
        while (pilihan != 'n'):
            print ("Pilih Barang yang ingin anda beli  ")
            print ("1. Ayam")
            print ("2. Beras")
            print ("3. Minyak")
            print ("4. Telur")
            print ("5. Tepung")
            print ("6. Gula")
            print ("7. Total pembelian")

            a = float (input("Masukan barang yang ingin anda beli : "))
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
            elif (a==7):
                totalharga = totalgula()+totalayam()+totalberas()+totalminyak()+totaltepung()+totaltelur()
                print ("total harga pembelian : Rp",totalharga )

            else :
                print ("Masukan yang anda masukan salah")    
            pilihan = input("Apakah Anda ingin mengulangi lagi (y/n)?")
            thanks()





