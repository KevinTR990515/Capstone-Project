from tabulate import tabulate
data = [{'Nomor':'','Nama':'Adrian Hermansyah','Kelas':'5A','Jenis Kelamin':'Laki-laki','Umur':10,'Kelurahan':'Kampung Bali','Nilai':80,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Febrian Astra','Kelas':'5B','Jenis Kelamin':'Laki-laki','Umur':11,'Kelurahan':'Petamburan','Nilai':76,'Keterangan':'Remedial'},
        {'Nomor':'','Nama':'Medina Oktaviani','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Karet Tengsin','Nilai':92,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Beni Lukman','Kelas':'5A','Jenis Kelamin':'Laki-Laki','Umur':10,'Kelurahan':'Karet Tengsin','Nilai':84,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Naufal Ramadhan','Kelas':'5A','Jenis Kelamin':'Laki-laki','Umur':10,'Kelurahan':'Petamburan','Nilai':88,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Erina Hermawati','Kelas':'5B','Jenis Kelamin':'Perempuan','Umur':12,'Kelurahan':'Bendungan Hilir','Nilai':80,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Vina Puspita Sari','Kelas':'5B','Jenis Kelamin':'Perempuan','Umur':11,'Kelurahan':'Bendungan Hilir','Nilai':100,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Leni Mustika ','Kelas':'5B','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Karet Tengsin','Nilai':84,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Danu Rahman','Kelas':'5B','Jenis Kelamin':'Laki-Laki','Umur':10,'Kelurahan':'Bendungan Hilir','Nilai':72,'Keterangan':'Remedial'},
        {'Nomor':'','Nama':'Chandra Putra','Kelas':'5A','Jenis Kelamin':'Laki-laki','Umur':10,'Kelurahan':'Petamburan','Nilai':88,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Yanti Rahayu','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Kampung Bali','Nilai':72,'Keterangan':'Remedial'},
        {'Nomor':'','Nama':'Qonita Putri','Kelas':'5B','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Kampung Bali','Nilai':76,'Keterangan':'Remedial'},
        {'Nomor':'','Nama':'Halimah Ayudia','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Karet Tengsin','Nilai':92,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Sabrina Citra Melissa','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Kampung Bali','Nilai':80,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Kiki Pratama','Kelas':'5B','Jenis Kelamin':'Laki-laki','Umur':11,'Kelurahan':'Petamburan','Nilai':96,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Gio Rahmat Putra','Kelas':'5B','Jenis Kelamin':'Laki-laki','Umur':10,'Kelurahan':'Kampung Bali','Nilai':88,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Yahya Mulia','Kelas':'5B','Jenis Kelamin':'Laki-laki','Umur':12,'Kelurahan':'Karet Tengsin','Nilai':80,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Olivia Maharani','Kelas':'5B','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Karet Tengsin','Nilai':76,'Keterangan':'Remedial'},
        {'Nomor':'','Nama':'Indah Ayu Mutia','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Bendungan Hilir','Nilai':100,'Keterangan':'Lulus'},
        {'Nomor':'','Nama':'Julia Elinawati','Kelas':'5A','Jenis Kelamin':'Perempuan','Umur':10,'Kelurahan':'Bendungan Hilir','Nilai':84,'Keterangan':'Lulus'},
        ]
bin_data = []

def read_data(data):
    for index, setiap_data in enumerate(data):
        setiap_data['Nomor'] = index + 1
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

def input_alfabet(prompt):
    while True:
        Huruf = input(prompt)
        if Huruf.replace(" ","").isalpha():
            return Huruf.title()
        else:
            print("Yang diinput bukan alfabet!")

def input_kelas(prompt):
    while True:
        Kelas = input(prompt)
        if Kelas in ['5A', '5B']:
            return Kelas
        else:
            print("Harus kelas 5A atau 5B!")

def input_umur(prompt):
    while True:
        Umur = input(prompt)
        if Umur.isdigit():
            Umur = int(Umur)
            if Umur <= 12 and Umur >= 10:
                return int(Umur)
            else:
                print("Harus di angka 10 sampai dengan 12 tahun!")
        else:
            print("Input yang anda masukkan bukan angka!")

def input_jenis_kelamin(prompt):
    while True:
        Jenis_Kelamin = input(prompt)
        if Jenis_Kelamin in ['Laki-laki','Perempuan']:
            return Jenis_Kelamin
        else:
            print("Harus antara 'Laki-laki' atau 'Perempuan'!")

def input_numerik(prompt):
    while True:
        Numerik = input(prompt)
        if Numerik.isdigit():
            return int(Numerik)
        else:
            print("Input harus berupa nilai angka!")

def input_keterangan(prompt): #Dipakai untuk filter keterangan
    while True:
        Keterangan = input(prompt)
        if Keterangan == 'Lulus' or Keterangan == 'Remedial':
            return Keterangan
        else:
            print("Harus antara 'Lulus' atau 'Remedial'!")

def input_nilai(prompt): # Dipakai untuk filter nilai
    while True:
        Nilai = input(prompt)
        if Nilai.isdigit():
            Nilai = int(Nilai)
            if Nilai <= 100 and Nilai % 4 == 0:
                return Nilai
            if Nilai % 4 != 0:
                print("Karena soal UTS berjumlah 25, maka nilai haruslah kelipatan 4. Nilai yang anda input bukanlah kelipatan 4!")
            elif Nilai > 100:
                print("Nilai tidak bisa melebihi 100!")
        else:
            print("Input nilai yang anda masukkan tidak valid!")

def input_index(prompt):
    while True:
        Index = input(prompt)
        if Index.isdigit():
            Index = int(Index)
            if Index <= (len(data) - 1):
                return int(Index)
            elif Index > (len(data) - 1):
                print("Index tidak boleh melebihi jumlah data!")
            else:
                print("Masukkan nilai index yang benar!")
        else:
            print("Index harus berupa angka!")

def create_data():
    nama = input_alfabet("Masukkan nama anda: ")
    kelas = input_kelas("Masukkan kelas anda: ")
    jenis_kelamin = input_jenis_kelamin("Masukkan jenis kelamin anda: ")
    umur = input_umur("Masukkan umur anda yang sesuai: ")
    kelurahan = input_alfabet("Masukkan kelurahan anda tinggal: ")
    while True:
        nilai = input_numerik("Masukkan nilai anda: ")
        if nilai >= 80 and nilai <= 100 and nilai % 4 == 0:
            keterangan = "Lulus"
            break
        elif nilai < 80 and nilai % 4 == 0:
            keterangan = "Remedial"
            break
        elif nilai > 100:
            print("Nilai tidak bisa melebihi dari 100!")
        else:
            print("Yang anda input tidak valid!")
    data.append({'Nama': nama,'Kelas':kelas,'Jenis Kelamin':jenis_kelamin,'Umur':umur,'Kelurahan':kelurahan,'Nilai':nilai,'Keterangan':keterangan})
    read_data(data)
    print("Data berhasil bertambah!")
    while True:
        Tambah_Data_Lagi = input("Apakah anda ingin menambah data lagi ? (y/n)")
        if Tambah_Data_Lagi == 'y':
            create_data()
            break
        elif Tambah_Data_Lagi == 'n':
            break
        else:
            print("Harus input 'y' atau 'n'!")

def filter_data():
    read_data(data)
    while True:
        kolom_filter = input("Mau di kolom mana yang ingin difilter ?")
        if kolom_filter in ['Kelas']:
            while True:
                cari_filter_kelas = input_kelas("Mau filter kelas yang mana ?")
                list_filter_kelas = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_kelas, data))
                if len(list_filter_kelas) != 0:
                    read_data(list_filter_kelas)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Jenis Kelamin']:
            while True:
                cari_filter_jenis_kelamin = input_jenis_kelamin("Mau filter jenis kelamin yang mana ?")
                list_filter_jenis_kelamin = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_jenis_kelamin, data))
                if len(list_filter_jenis_kelamin) != 0:
                    read_data(list_filter_jenis_kelamin)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Keterangan']:
            while True:
                cari_filter_keterangan = input_keterangan("Mau filter keterangan yang mana ?")
                list_filter_keterangan = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_keterangan, data))
                if len(list_filter_keterangan) != 0:
                    read_data(list_filter_keterangan)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Umur']:
            while True:
                cari_filter_umur = input_umur("Mau filter umur berapa ?")
                list_filter_umur = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_umur, data))
                if len(list_filter_umur) != 0:
                    read_data(list_filter_umur)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Nilai']:
            while True:
                cari_filter_nilai = input_nilai("Mau filter nilai berapa ?")
                list_filter_nilai = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_nilai, data))
                if len(list_filter_nilai) != 0:
                    read_data(list_filter_nilai)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Nama']:
            while True:
                cari_filter_nama = input_alfabet("Mau filter data yang mana ?")
                list_filter_nama = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_nama, data))
                if len(list_filter_nama) != 0:
                    read_data(list_filter_nama)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        elif kolom_filter in ['Kelurahan']:
            while True:
                cari_filter_kelurahan = input_alfabet("Mau filter data yang mana ?")
                list_filter_kelurahan = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter_kelurahan, data))
                if len(list_filter_kelurahan) != 0:
                    read_data(list_filter_kelurahan)
                    print("Data berhasil difilter!")
                    break
                else:
                    print("Filter tidak ditemukan di data")
            break
        else:
            print("Kolom yang anda cari tidak ada di dalam data")

def update_data():
    read_data(data)
    print('''
          Apakah anda ingin mengupdate satu-satu atau update secara keseluruhan ?
          1. Update secara satu-satu
          2. Update secara keseluruhan
          3. Tidak jadi update data
          ''')
    while True:
        menu_update = input_numerik("Apakah anda ingin mengupdate ? Tekan 1 untuk update secara satu-satu, tekan 2 untuk update secara keseluruhan, tekan 3 untuk cancel.")
        if menu_update == 1:
            update_data_satu_satu()
            break
        elif menu_update == 2:
            update_data_keseluruhan()
            break
        elif menu_update == 3:
            break
        else:
            print("Harus input '1', '2', atau '3'!")

def update_data_satu_satu():
    index_update = input_index("Mau update baris data yang mana ?")
    read_data([data[index_update]])
    data_benar = False
    while True:
        benar_atau_tidak = input("Apakah data yang ditampilkan sudah benar ? (y/n)")
        if benar_atau_tidak == 'y':
            while True:
                kolom_update = input("Mau update kolom yang mana ?")
                if kolom_update == 'Nama':
                    nama_baru = input_alfabet("Masukkan nama yang baru: ")
                    data[index_update]['Nama'] = nama_baru
                    read_data(data)
                    print("Data berhasil diupdate!")
                    break
                elif kolom_update == 'Kelas':
                    kelas_baru = input_kelas("Masukkan kelas yang mau diupdate: ")
                    data[index_update]['Kelas'] = kelas_baru
                    read_data(data)
                    print("Data berhasil diupdate!")
                    break
                elif kolom_update == 'Jenis Kelamin':
                    jenis_kelamin_baru = input_jenis_kelamin("Masukkan jenis kelamin yang mau diupdate: ")
                    data[index_update]['Jenis Kelamin'] = jenis_kelamin_baru
                    read_data(data)
                    print("Data berhasil diupdate")
                    break
                elif kolom_update == 'Umur':
                    umur_baru = input_umur("Masukkan umur yang mau diupdate: ")
                    data[index_update]['Umur'] = umur_baru
                    read_data(data)
                    print("Data berhasil diupdate!")
                    break
                elif kolom_update == 'Kelurahan':
                    kelurahan_baru = input_alfabet("Masukkan kelurahan yang mau diupdate: ")
                    data[index_update]['Kelurahan'] = kelurahan_baru
                    read_data(data)
                    print("Data berhasil diupdate!")
                    break
                elif kolom_update == 'Nilai':
                    while True:
                        nilai_baru = input_numerik("Masukkan nilai yang mau diupdate: ")
                        if nilai_baru >= 80 and nilai_baru <= 100 and nilai_baru % 4 == 0:
                            keterangan = "Lulus"
                            data[index_update]['Nilai'] = nilai_baru
                            data[index_update]['Keterangan'] = keterangan
                            read_data(data)
                            print("Data berhasil diupdate!")
                            break
                        elif nilai_baru < 80 and nilai_baru % 4 == 0:
                            keterangan = "Remedial"
                            data[index_update]['Nilai'] = nilai_baru
                            data[index_update]['Keterangan'] = keterangan
                            read_data(data)
                            print("Data berhasil diupdate!")
                            break
                        elif nilai_baru > 100:
                            print("Nilai tidak bisa melebihi dari 100!")
                        else:
                            print("Yang anda input tidak valid!")
                    break
                else:
                    print("Kolom yang diminta tidak ada!")
            data_benar = True
            break
        elif benar_atau_tidak == 'n':
            print("Pilih kembali baris data yang mau diupdate.")
            update_data_satu_satu()
            break
        else:
            print("Input harus 'y' atau 'n'!")
    if data_benar == True:
        while True:
            update_lagi = input("Apakah anda ingin mengupdate data lagi ? Tekan 'y' untuk lanjut update. Tekan 'n' untuk kembali ke menu utama. (y/n)")
            if update_lagi == 'y':
                update_data()
                break
            elif update_lagi == 'n':
                break
            else:
                print("Harus input 'y' atau 'n'!")

def update_data_keseluruhan():
    index_update = input_index("Mau update baris data yang mana ?")
    read_data([data[index_update]])
    data_sudah_benar = False
    while True:
        benar_atau_salah = input("Apakah data yang ditampilkan sudah benar ? (y/n)")
        if benar_atau_salah == 'y':
            data[index_update]['Nama'] = input_alfabet("Masukkan nama terbaru: ")
            data[index_update]['Kelas'] = input_kelas("Masukkan kelas terbaru: ")
            data[index_update]['Jenis Kelamin'] = input_jenis_kelamin("Masukkan jenis kelamin terbaru: ")
            data[index_update]['Umur'] = input_umur("Masukkan umur terbaru: ")
            data[index_update]['Kelurahan'] = input_alfabet("Masukkan kelurahan terbaru: ")
            while True:
                nilai_update = input_numerik("Masukkan nilai terbaru: ")
                if nilai_update >= 80 and nilai_update <= 100 and nilai_update % 4 == 0:
                    keterangan_update = "Lulus"
                    data[index_update]['Nilai'] = nilai_update
                    data[index_update]['Keterangan'] = keterangan_update
                    break
                elif nilai_update < 80 and nilai_update % 4 == 0:
                    keterangan_update = "Remedial"
                    data[index_update]['Nilai'] = nilai_update
                    data[index_update]['Keterangan'] = keterangan_update
                    break
                elif nilai_update > 100:
                    print("Nilai tidak bisa melebihi 100!")
                else:
                    print("Input nilai yang anda masukkan tidak valid!")
            data_sudah_benar = True
            break
        elif benar_atau_salah == 'n':
            print("Pilih kembali baris data yang mau diupdate.")
            update_data_keseluruhan()
            break
        else:
            print("Input harus 'y' atau 'n'!")
    if data_sudah_benar == True:
        read_data(data)
        print("Data berhasil diupdate!")
        while True:
            update_lagi = input("Apakah anda ingin mengupdate data lagi ? Tekan 'y' untuk lanjut update. Tekan 'n' untuk kembali ke menu utama. (y/n)")
            if update_lagi == 'y':
                update_data()
                break
            elif update_lagi == 'n':
                break
            else:
                print("Harus input 'y' atau 'n'!")

def delete_data():
    read_data(data)
    data_terhapus_disini = []
    for i in data:
        data_terhapus_disini.append(i['Nomor'])
    while True:
        number_delete = input_numerik("Masukkan nomor/baris data yang mau didelete: ")
        if number_delete in data_terhapus_disini:
            for i in data:
                if number_delete == i['Nomor']:
                    read_data([data[number_delete - 1]])
                    while True:
                        hapus_atau_tidak = input(f"Apakah anda yakin ingin menghapus data nomor ke-{number_delete} ? Tekan 'y' untuk menghapus. Tekan 'n' untuk tidak jadi menghapus data. (y/n)")
                        if hapus_atau_tidak == 'y':
                            bin_data.append(i)
                            data.remove(i)
                            read_data(data)
                            print("Data berhasil terhapus!")
                            print("Data yang telah terhapus sudah masuk ke dalam data bin.")
                            read_data(bin_data)
                            break
                        elif hapus_atau_tidak == 'n':
                            break
                        else:
                            print("Harus 'y' atau 'n'!")
            break
        else:
            print("Nomor yang anda masukkan tidak ada di dalam data.")

def restore_data():
    read_data(bin_data)
    print('''
          Apakah anda ingin menrestore satu data saja atau restore semua data ?
          1. Restore satu data yang ada di dalam bin saja
          2. Restore semua data yang ada di dalam bin
          3. Tidak jadi restore data
          ''')
    while True:
        menu_restore = input_numerik("Apakah anda ingin merestore data ? Tekan 1 untuk restore satu data saja, tekan 2 untuk restore semua data., tekan 3 untuk cancel.")
        if menu_restore == 1:
            restore_satu_bin_data()
            break
        elif menu_restore == 2:
            restore_semua_bin_data()
            break
        elif menu_restore == 3:
            break
        else:
            print("Harus input '1' atau '2'!")

def restore_satu_bin_data():
    data_terestore_disini = []
    for i in bin_data:
        data_terestore_disini.append(i['Nomor'])
    while True:
        number_restore = input_index("Masukkan nomor/baris bin data yang mau direstore: ")
        if number_restore in data_terestore_disini:
            for i in bin_data:
                if number_restore == i['Nomor']:
                    read_data([bin_data[number_restore]])
                    while True:
                        restore_atau_tidak = input(f"Apakah anda yakin ingin merestore bin data nomor ke-{number_restore} ? Tekan 'y' untuk restore, tekan 'n' untuk cancel. (y/n)")
                        if restore_atau_tidak == 'y':
                            data.append(i)
                            bin_data.remove(i)
                            read_data(data)
                            print("Data berhasil direstore!")
                            read_data(bin_data)
                            break
                        elif restore_atau_tidak == 'n':
                            break
                        else:
                            print("Harus 'y' atau 'n'!")
            break
        else:
            print("Nomor yang anda masukkan tidak valid!")

def restore_semua_bin_data():
    while True:
        restore_atau_tidak = input("Apakah anda yakin ingin merestore data yang sudah berada di dalam bin kembali ke data utama ? Tekan 'y' untuk restore, tekan 'n' untuk cancel. (y/n)")
        if restore_atau_tidak == 'y':   
            data.extend(bin_data)
            bin_data.clear()
            read_data(data)
            print("Data yang berada di bin berhasil masuk ke dalam data utama!")
            break
        elif restore_atau_tidak == 'n':
            break
        else:
            print("Input harus 'y' atau 'n'!")

def sort_data():
    read_data(data)
    while True:
        pilih_kolom = input("Mau di kolom mana yang ingin disorting ?")
        if pilih_kolom == 'Nama' or pilih_kolom == 'Kelas' or pilih_kolom == 'Jenis Kelamin' or pilih_kolom == 'Umur' or pilih_kolom == 'Kelurahan' or pilih_kolom == 'Nilai':
            print("Sorting berdasarkan apa ? Ketik 'a' untuk ascending (sorting berdasarkan dari bawah ke atas). Ketik 'd' untuk descending (sorting berdasarkan dari atas ke bawah).")
            while True:
                pilih_urutan = input("a = ascending atau d = descending ? (a/d)")
                if pilih_urutan == 'a':
                    data_sorting_a = list(sorted(data, key=lambda setiap_data: setiap_data[pilih_kolom]))
                    read_data(data_sorting_a)
                    print("Data berhasil disorting!")
                    break
                elif pilih_urutan == 'd':
                    data_sorting_d = list(sorted(data, key=lambda setiap_data: setiap_data[pilih_kolom], reverse=True))
                    read_data(data_sorting_d)
                    print("Data berhasil disorting!")
                    break
                else:
                    print("Harus input 'a' atau 'd'!")
            break
        elif pilih_kolom == 'Keterangan':
            print("Tidak perlu sorting kolom 'Keterangan' dikarenakan kalau sorting dari kolom 'Nilai', maka kolom 'Keterangan' sudah otomatis tersorting juga. Ketik 'Nilai' saja.")
        else:
            print("Kolom yang diminta tidak ada.")

def main_data():
    while True:
        print('''
        "DATA NILAI UTS MATEMATIKA SISWA KELAS 5 SD NEGERI 01 JAKARTA PUSAT"
        SELAMAT DATANG! SILAKAN PILIH MENU:
        1. Background
        2. Melihat Data Nilai Siswa yang Sekarang
        3. Tambah Data Siswa            
        4. Filter Data Siswa
        5. Update Data Siswa
        6. Delete Data Siswa
        7. Restore Data Siswa (Hanya bisa masuk jika ada data bin nya!)
        8. Sorting Data Siswa
        9. Keluar dari Menu
        ''')
        menu = input_numerik('masukkan pilihan menu : ')
        if menu == 1:
            print('''
            Guru matematika di SD Negeri 01 Jakarta Pusat melakukan UTS kepada semua siswa kelas 5.
            Soal matematika berisi 25 soal, dengan 1 soal benar berjumlah 4 poin.
            Semua siswa kelas 5 wajib mendapatkan nilai minimal 80 untuk lulus UTS Matematika,
            jika siswa mendapatkan nilai di bawah 80, maka siswa tersebut harus mengikuti remedial.
            ''')
        elif menu == 2:
            read_data(data)
        elif menu == 3:
            create_data()
        elif menu == 4:
            filter_data()
        elif menu == 5:
            update_data()
        elif menu == 6:
            delete_data()
        elif menu == 7:
            if len(bin_data) != 0:
                restore_data()
            else:
                print("Bin data tidak ada!")
        elif menu == 8:
            sort_data()
        elif menu == 9:
            exit = False
            while True:
                Keluar_Menu = input("Apakah anda yakin ingin keluar dari menu ? Jika iya, tekan 'y'. Jika tidak, tekan 'n'. (y/n)")
                if Keluar_Menu == 'n':
                    break
                elif Keluar_Menu == 'y':
                    print("Terima kasih dan sampai jumpa di kemudian waktu!")
                    exit = True
                    break
                else:
                    print("Input harus 'y' atau 'n'!")
            if exit == True:
                break
        else :
            print('masukkan menu yang valid')

main_data()