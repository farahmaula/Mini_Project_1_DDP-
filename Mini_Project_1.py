while True :
        print ("===== Menu Utama Catatan Kehadiran Mahasiswa =====")
        print ("1.Masukkan data")
        print ("2.Hapus data")
        print ("3.Keluar")
        print ("\n")
        menu = input("Pilih Menu Utama (1/2/3): ")
        if menu  == "1": 
                nama = str(input("Nama: ")) 
                nim = int(input("NIM: ")) 
                tanggal = int(input("Tanggal (1-30): "))   
                bulan = int(input("Bulan (1-12): ")) 
                tahun = int(input("Tahun: ")) 
                jam = float(input("Jam kehadiran (08.00-09.00): "))
                print ("\n")
                status = input("Apakah hadir? (ya/tidak): ")

                if status == "ya":
                        print ("hadir")

                elif status == "tidak":
                        alasan_tidak_hadir = ( "Sakit", "Izin", "Tidak valid" ) 
                        alasan = ("Pilih alasan tidak hadir? ")
                        print ("1. sakit")
                        print ("2. izin")
                        pilih_alasan = input("pilih alasan tidak hadir (1/2): ")
                        if pilih_alasan == "1":
                                alasan = alasan_tidak_hadir[0]
                                print ("sakit")
                        elif pilih_alasan == "2":
                                alasan = alasan_tidak_hadir[1]
                                print ("izin")
                        elif pilih_alasan == "3":
                                alasan = alasan_tidak_hadir[2]
                                print ("tidak valid")
                                
        
        elif menu == "2":
                status = input("Hadir? (ya): ")
                jam = float(input("Jam kehadiran (08.00-09.00): "))
                if jam > 09.00:
                        print("Data dihapus karena terlambat")
                else:
                        print("Tidak ada data yang dihapus")
        
        elif menu == "3":
                print ("keluar sistem")

        else:
                print ("Menu tidak valid, coba lagi")