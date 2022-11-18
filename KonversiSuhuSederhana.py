# Program Pengkonversi Suhu Sederhana

# Kamus
'''
X           : bool
B           : int
T           : int
k           : bool
N           : int
n           : int
temp        : int
Temp_jmlh   : int
Temp_maks   : int
Temp_min    : int
Temp_avg    : float
'''

# Algoritma
X = False
while X == False:
    B = int(input("Bulan: "))
    if B > 12:
        print("Data yang anda masukkan tidak valid!")
        print("Harap masukkan ulang data bulan.")
        print ("")
    else:
        X = True

T = int(input("Tahun: "))
if T % 400 == 0:
    k = True
elif T % 400 != 0:
    if T % 100 == 0:
        k = False
    elif T % 100 != 0:
        if T % 4 == 0:
            k = True
        else:
            k = False

if B == 1 or B == 3 or B == 5 or B == 7 or B == 8 or B == 10 or B == 12:
    N = 31
elif B == 4 or B == 6 or B == 9 or B == 11:
    N = 30
elif B == 2:
    if k:
        N = 29
    else:
        N = 28

Temp_jmlh = 0
print("")
print("Suhu(°C) pada: ")
for n in range (1, N+1):
    temp = int(input("tanggal " + str(n) + ": "))
    Temp_jmlh += temp

    if n == 1:
        Temp_maks = temp
        Temp_min = temp
    elif temp > Temp_maks:
        Temp_maks = temp
    elif temp < Temp_min:
        Temp_min = temp

Temp_avg = Temp_jmlh/N

print ("Suhu rata-rata: " + str(Temp_avg) + "°C" + ", Suhu tertinggi: " + str(Temp_maks) + "°C" + ", Suhu terendah " + str(Temp_min) + "°C")