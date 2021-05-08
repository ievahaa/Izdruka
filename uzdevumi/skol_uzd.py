#Izveido funkciju, kura salīdzina saraksta pirmo un pēdējo skaitli: Ja pirmais skaitlis ir lielāks, nekā pēdējais, sarakstu izprintē atmuguriski, ja pēdējais skaitlis ir lielāks par pirmo, sarakstu izprintē normāli.

def salidzini(saraksts):
    pirmais = saraksts[0]
    pedejais = saraksts[-1]
    if pirmais < pedejais:
        print(saraksts)
    else:
        saraksts.reverse()
        print(saraksts)


salidzini([7, 3, 8, 4])

#Uzrakstīt funkciju, kas sadala lietotāja ievadīto tekstu pēc atstarpēm un atgriež vārdu, kura kārtas numuru teikumā ievada lietotājs. (izmanto split())

def sadali(teikums,numurs):
    pa_vardiem = teikums.split()
    return pa_vardiem[numurs-1]

teksts = input("Ievadi teikumu: ")
nr = int(input("Ievadi kārtas numuru, kuru vārdu vēlies izdrukāt: "))
print(sadali(teksts,nr))
