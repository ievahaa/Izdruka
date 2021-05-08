#1 
str = input("Ievadiet teikumu ") 
print(f"Jusu teikumā ir {len(str)} simboli") 
#2 
str = input("Ievadiet savu vārdu ") 
print(str[0]) 
#3 
str = "Sveika, pasaule!" 
print(str[10:15])  
#4 
str = input("Ievadiet teikumu ") 
print(str.upper()) 
#5 
str = input("Ievadiet teikumu ") 
print(str.lower()) 
#6 
str = "samērcēt" 
print(str.replace("s", "p")) 
#7 
str = " Sveika, pasaule! " 
print(str.strip( " " )) 
#8 
b = "Ievadiet teikumu" 
print(b) 
c = "*".join(b) 
print(c) 
 
#9 
a = input("Ievadiet savu vārdu ") 
print(a[::-1] + ". Pamatīgs jūceklis, vai nē, "+ a[0]) 