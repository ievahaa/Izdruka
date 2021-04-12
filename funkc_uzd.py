#Funkcija atgriež 10% no a un 20% no skaitļa b
def procenti(a, b):
    return a * 10 / 100, b * 0.20


print(procenti(100, 1000))


def var_pagulet(diena):
    if diena == "brīvdiena":
        return True
    else:
        return False


print(var_pagulet("darbdiena"))
print(var_pagulet("brīvdiena"))

#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. Funkcija ir_problema


def ir_problema(a_smile, b_smile):
    return a_smile == b_smile


print(ir_problema(True, False))
print(ir_problema(False, False))
print(ir_problema(True, True))
print(ir_problema(False, True))

#Dots veselais skaitlis n. Uzraksti funkciju, kas atgriež starpības moduli starp n un 21, izņemot, ja modulis ir vairāk nekā 21, tad atgriež dubultu tā vērtību. Ja n>21, tad starpība n-21 ir pozitīva, ja n<21, tad starpība 21-n ir pozitīva
