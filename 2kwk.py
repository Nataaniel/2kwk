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
