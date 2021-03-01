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

#uzd4
#Izvadi ar cikla palīdzību:
# 1
# 12
# 123
# 1234

#uzd5
# Fibonači virknē, katrs nākamais skaitlis ir divu iepriekšējo skaitļu summa: 0 1 1 2 3 5... Izvadi visus Fibonači virknes skaitļus no 1 līdz 100
