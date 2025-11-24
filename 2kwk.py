import math

def hitung_nilai():
    print("\n=== PERHITUNGAN NILAI AKHIR ===")
    tugas = float(input("Nilai Tugas (30%): "))
    uts = float(input("Nilai UTS (30%): "))
    uas = float(input("Nilai UAS (40%): "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    print("Nilai Akhir =", round(nilai_akhir, 2))


def hitung_gaji():
    print("\n=== PERHITUNGAN GAJI KARYAWAN ===")
    gaji_pokok = float(input("Gaji Pokok: "))
    tunjangan = float(input("Tunjangan: "))
    potongan = float(input("Potongan: "))

    total_gaji = gaji_pokok + tunjangan - potongan
    print("Total Gaji =", total_gaji)


def hitung_luas():
    print("\n=== PERHITUNGAN LUAS BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Lingkaran")

    pilih = input("Pilih bangun(1/2/3): ")

    if pilih == "1":
        sisi = float(input("Sisi: "))
        luas = sisi * sisi
        print("Luas Persegi =", luas)

    elif pilih == "2":
        alas = float(input("Alas : "))
        tinggi = float(input("Tinggi : "))
        luas = 0.5 * alas * tinggi
        print("Luas Segitiga =", luas)

    elif pilih == "3":
        r = float(input("Jari-jari: "))
        luas = math.pi * r * r
        print("Luas Lingkaran =", round(luas, 2))

    else:
        print("Pilihan tidak valid")

while True:
    print("\n=== APLIKASI PERHITUNGAN SERBAGUNA ===")
    print("1. Hitung Nilai Akhir")
    print("2. Hitung Gaji Karyawan")
    print("3. Hitung Luas Bangun Datar")
    print("4. Keluar")

    pilih = input("Pilih menu (1/2/3/4): ")
