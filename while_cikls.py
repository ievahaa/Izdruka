print("sveiki")
print("sveiki")
print("sveiki")

#while True:
#    print("sveiki")

i = 1  #tipisks cikla mainīgais
while i <= 5:
    print("labi")
    i += 1  #i=i+1
print("i tagad ir", i)

j = 0
while j < 5:
    print("Nr.", j)
    j += 1

while i > 0:
    print("Skaitām atpakaļ", i)
    i -= 1

#ar soli 2
i = 20
while True:
    if i > 26:
        break
    print("i ir",i)
    i += 2

#uzdevums
#Ievadiet eglītes augstumu. Izdrukājiet eglīti:
#Piem. augstums == 3
#Izdruka būtu:
#  *
# ***
#*****

augstums = int(input("Norādi stāvu skaitu: "))
i = 0
while i < augstums:
    print("*"*augstums)
    i += 1


