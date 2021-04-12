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

#Dots pozitīvs veselais skaitlis n. Uzraksti funkciju, kas atgriež starpības moduli starp n un 21, izņemot, ja modulis ir vairāk nekā 21, tad atgriež dubultu tā vērtību.


def starpiba(n):
    if n <= 21:
        st = 21 - n
    else:
        st = n - 21
    if st > 21:
        return st * 2
    return st


print(starpiba(3)) #atgriež 18, jo 21-3 = 18
print(starpiba(121)) #atgriež 200, jo 121-21 =100, bet jāreizina ar 2

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


def papagaila_problema(laiks, runa):
    if (laiks < 7 or laiks > 20) and runa:
        return True
    return False


print(papagaila_problema(5, True))  #atgriež True, jo trokšņo naktī
print(papagaila_problema(15, True))  #atgriež False, jo trokšņo dienā
print(papagaila_problema(5, False))  #atgriež False, jo naktī netrokšņo
