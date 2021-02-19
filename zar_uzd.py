a = 18
b = 3.45
c = 4.78
"""
if a>b and a>c and b<c:
    print("Skaitlis a ir lielākais un skaitlis b ir mazākais")
if b>a and b>c and a<c:
    print("Skaitlis b ir lielākais un skaitlis a ir mazākais")
"""

if a > b and a > c: 
    print("a ir lielākais skaitlis")
elif b > a and b > c:
    print("b ir lielākais skaitlis")
else:
    print("c ir lielākais skaitlis.")

if a < b and a < c:
    print("a ir mazākais skaitlis")
elif b < a and b < c:
    print("b ir mazākais skaitlis")
else:
    print("c ir mazākais skaitlis.")

#risinājums ar list
myList = [a, b, c]
myList.sort()
print(
    f"Lielākais skaitlis ir {myList[-1]}, bet mazākais skaitlis ir {myList[0]}."
)

#2.uzdevums
temp = float(input("Ievadi temperatūru: "))
if temp < 35:
    print("Vai nav par aukstu?")
elif temp >= 35 and temp <= 37: # 35<=temp<=37
    print("Viss kārtībā.")
else:
    print("Iespējams drudzis.")


#stundas uzdevums
#banka (te ir daudz naudas), veikals (Jānopērk āboli), aptieka (man ir iesnas), visur citur - ābolu nav
atr = input("Ievadi atrašanās vietu: ")
if atr == "banka":
    print("Te ir daudz naudas")
elif atr == "veikals":
    print("Jānopērk āboli")
elif atr == "aptieka":
    print("Man ir iesnas")
else:
    print("Ābolu nav")
