"""
vards = input("Kā tevi sauc? ")
print(f"Tavs vārds ir {vards}.")

gadi = int(input("Cik tev gadu? "))
print(f"Tev ir {gadi} gadi.")
dzimsGads = 2021 - gadi
print(f"Tavs dzimšanas gads ir {dzimsGads}.")


#Uzraksti programmu, kas lietotājam lūdz ievadīt temperatūru pēc Celsija un izdrukā šo temperatūru pēc Farenheita skalas. (T(°F) = T(°C) × 9/5 + 32)celsijs = int(input("Kāda ir temperatūra pēc Celsija?"))

farenheiti = celsijs * 9 / 5 + 32

print(
    f"Temperatūra {celsijs} grādi pēc Celsija skalas ir {farenheiti} grādi pēc Farenheita skalas."
)
#Uzraksti programmu, kas uzdod 3 jautājums par telpas izmēriem –  platumu, garumu, augstumu. Aprēķini un izdrukā telpas tilpumu.

platums = float(input("Platums: "))
garums = float(input("Garums: "))
augstums = float(input("Augstums: "))
print(f"Tilpums ir {platums*garums*augstums}.")

#Strings (rakstzīmju virknes)
print("sveiki")
print('sveiki')
print("I'm going on a run")
print('Arī šis ir "risinājums"')
print("Sveika, \npasaule!")  #izdrukā divās rindās
print("Sveika, \tpasaule!")  #izdrukā ar tabulācijas atkāpi

#String garums - len()
print(len("sveiki"))
print(len("Ko tu domā?"))
"""

# [sākums:beigas:solis]
myString = "Sveika, pasaule!"
print(myString)
print(myString[0])  #izdrukā pirmo rakstzīmi (ar indeksu 0)
print(myString[8])  #izdrukā rakstzīmi ar 8. indeksu
print(myString[-1])  #izdrukā pēdējo simbolu
print(myString[13])  #izdrukā 14. rakstzīmi
print(myString[-3])  #izdrukā 14. rakstzīmi

myString = "abcdefghijklmnoprstuvz"
print(myString)
print(myString[2]) #izdrukā c
print(myString[2:]) #izdrukā visu, sākot no c
print(myString[:3]) #izdrukā visu līdz 3. indeksam (neieskaitot)
print(myString[3:6]) #izdrukā visu no 3. līdz 5. indeksam
print(myString[::]) #izdrukā visu
print(myString[::2]) #izdrukā katru otro rakstzīmi
print(myString[2:7:2]) #izdrukā katru otro rakstzīmi no 2. līdz 6. indeksam
print(myString[::-1]) #izdrukā visu no otra gala
