def tempat() :
    print("Halo selamat datang di bioskop!")
    print("Dimanakah kamu ingin menonton?")
    print("1) XXI Empire")
    print("2) XXI Amplaz")
    print("3) XXI JCM")
    tempat=int(input("Masukkan pilihanmu :"))
    if(tempat>3) :
        print("Pilihan tidak tersedia.")
        exit()
    print("Mau nonton film apa nih? Ada film:")
    print("1. Frozen")
    print("2. Keramat")
    print("3. KKN di Desa Penari")
    film=int(input("Pilih nomor film:"))
    if(film>3) :
        print("Pilihan tidak tersedia.")
        exit()
    print("Mau nonton layar bioskop apa:")
    print("1. Reguler")
    print("2. Dolby atmos")
    print("3. Premiere")
    layar=int(input("Pilih nomor tipe layar:"))
    if(layar>3) :
        print("Pilihan tidak tersedia.")
        exit()
    jumlahtiket=input("Berapa banyak tiket?")
    print("Mau nonton layar bioskop apa")
    jam1=("12.35")
    jam2=("14.45")
    jam3=("16.55")
    jam4=("19.05")
    print("1. ", jam1)
    print("2. ", jam2)
    print("3. ", jam3)
    print("4. ", jam4)
    jam=int(input("Masukkan angka pilihan Anda :"))
    if(jam==1) :
        print("Oke berhasil!, Silahkan dinikmati di jam", jam1)
    elif(jam==2) :
        print("Oke berhasil!, Silahkan dinikmati di jam", jam2)
    elif(jam==3) :
        print("Oke berhasil!, Silahkan dinikmati di jam", jam3)
    elif(jam==4) :
        print("Oke berhasil!, Silahkan dinikmati di jam", jam4)
    else :
        print("Pilihan tidak tersedia.")

tempat()
