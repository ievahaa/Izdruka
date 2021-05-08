"""
#uzd1
#Lietotājs ievada divus veselos skaitļus – intervāla galapunktus. Izdrukāt visus norādītā intervāla skaitļus, ieskaitot abus galapunktus.[a;b]
#Papilduzdevums - ja norādīts nekorekts intervāls, tad izdrukā attiecīgu paziņojumu un liek ievadīt datus no jauna

a = int(input("Ievadi sākuma skaitli: "))
b = int(input("Ievadi beigu skaitli: "))
for skaitlis in range(a, b + 1):
    print(skaitlis, end=" ")

#uzd2
#Lietotājs ievada veselu skaitli. Aprēķini šī skaitļa faktoriālu, izmantojot ciklu. faktoriāls = 1*2*3*....*n
print()

a = int(input("Ievadi veselu skaitli: "))
faktorials = 1
for i in range(1, a + 1):
    faktorials = faktorials * i

print(f"Skaitļa {a} faktoriāls ir {faktorials}.")

#uzd3
#No lietotāja ievadīta intervāla, izvadi visus veselos skaitļus, kas dalās ar konkrētu skaitli (arī to norāda lietotājs).

a = int(input("Ievadi sākuma skaitli: "))
b = int(input("Ievadi beigu skaitli: "))
dalitajs = int(input("Ievadi dalītāju: "))
for skaitlis in range(a, b + 1):
    if skaitlis % dalitajs == 0:
        print(skaitlis, end=" ")



#2-1 Lietotājs ievada veselu skaitli N. Izdrukā visus nepāra skaitļus no 1 līdz N augošā secībā. Piemēram, ja N = 9, tad izdrukā 1, 3, 5, 7, 9

n = int(input("Ievadi veselu skaitli: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

#2-2 Lietotājs ievada divus veselos skaitļus A un B. Izdrukā visus skaitļus no A līdz B augošā secībā, ja A<B, bet dilstošā secībā, ja A>=B.

a = int(input("Ievadi veselu skaitli a: "))
b = int(input("Ievadi veselu skaitli b: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):  #skaita atpakaļ
        print(i)

#2-3 Lietotājs ievada veselu skaitli N. Izdrukā visus pāra skaitļus no 0 līdz N dilstošā secībā. Piemēram, ja N = 7, tad izdrukā 6, 4, 2, 0

n = int(input("Ievadi veselu skaitli: "))
for i in range(n, -1, -1):
    if i % 2 == 0:
        print(i)

#versija 2-3
n = int(input("Ievadi veselu skaitli: "))

for k in reversed(range(0, n + 1)):
    if k % 2 == 0:
        print(k)

#2-4 Pajautā, lai lietotājs ievada 10 skaitļus (var būt daļskaitļi). Programma visus ievadītos skaitļus ievieto sarakstā (list). Kad saraksts gatavs, to izdrukā.

mylist = []
for i in range(10):
    n = float(input(f"Ievadi {i+1}. skaitli: "))
    mylist.append(n)

#mylist.sort()
print(mylist)

#2-5 Lietotājs ievada veselu skaitli N. Izdrukā visus veselo skaitļu kvadrātus, kas ir mazāki vai vienādi ar N, augošā secībā. Piemēram, ja N = 10, tad izdrukā 1, 4, 9

sk = 1
n = int(input("Ievadi veselu skaitli: "))
while sk * sk <= n:
    print(sk**2)
    sk += 1

#2-6 Lietotājs ievada veselu skaitli N >=  2. Izdrukā mazāko veselo skaitli (izņemot 1), ar kuru N dalās bez atlikuma.

n = 0
while n < 2:
    n = int(input("Ievadi veselu skaitli, kas ir vismaz 2: "))

dalitajs = 2
while True:
    if n % dalitajs == 0:
        print(
            f"Mazākais skaitlis, ar ko {n} dalās bez atlikuma, ir {dalitajs}.")
        break
    else:
        dalitajs += 1
"""
#uzd 2-7 Izvadi ar cikla palīdzību:
# 1
# 12
# 123
# 1234

#str(5) = "5"
#print("5"+"6")

#sk = 1
a = ""
for sk in range(1, 5):
    a = a + str(sk)
    print(a)

sk = 1
a = ""
while sk < 5:
    a = a + str(sk)
    print(a)
    sk += 1
"""
#uzd 2-8
# Fibonači virknē, katrs nākamais skaitlis ir divu iepriekšējo skaitļu summa: 0 1 1 2 3 5... Izvadi visus Fibonači virknes skaitļus no 1 līdz 100

pirmais = 0
otrais = 1
pagaidu = 0

print("Fibonači skaitļi ir",end=" ")

while pirmais<=100:
    print(pirmais, end=" ")
    temp = pirmais+otrais
    pirmais = otrais
    otrais = temp

"""
