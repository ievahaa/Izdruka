#if, else, elif
"""
if nosacījums:
    izpildāmās darbības
elif cits nosacījums:
    izpildāmās dabības
else:
    izpildāmās darbības visos citos gadījumos
"""
#ja skaitlis ir lielāks par 5, izdrukā, ka lielāks par 5, citādi, ja skaitlis lielāks par 0, izdrukā, ka lielāks par 0. Citādi izdrukā, ka tas nav pozitīvs skaitlis
a = -1
if a > 5:
    print("Šis skaitlis ir lielāks par 5.")
elif a > 0:
    print(f"Skaitlis {a} ir lielāks par 0.")
else:
    print(f"Skaitlis {a} nav pozitīvs.")

if True:
    print("patiesi")

suns_grib_est = False

if suns_grib_est:
    print("Pabaro suni!")
else:
    print("Suns ir paēdis.")