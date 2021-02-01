#vārdnīcas jeb dictionaries
tel = {
    "direktors": "67947253",
    "vietnieks": "65674720",
    "sekretāre": "65826974"
}
print(tel["direktors"])  #norādot atslēgu, izdrukā vērtību

cenas = {'piens': 1.12, 'āboli': 0.95, 'apelsīni': 1.89}
print(cenas["piens"])

d = {
    "k1": 123,
    "k2": [10, 11, 12],
    "k3": {
        "atsl1": 100,
        "atsl2": 200
    }
}  #vārdnīcās var uzglabāt dažādus datu tipus
print(d["k1"])
print(d["k3"]["atsl1"])  #izdrukā iekšējās vārdnīcas elementu
#kā izdrukāt 12 no "k2"?
print(d["k2"][2])  #vispirms norāda atslēgu, pēc tam saraksta indeksu

my_dict = {'key1': ['a', 'b', 'c']}
print(my_dict)
my_list = my_dict['key1']
print(my_list)
burts = my_list[2]
print(burts)
print(burts.upper())
#vienā rindā
print(my_dict['key1'][1].upper())  #izdrukā lielo b

#pievieno jaunus objektus
new_dict = {'k1': 100, 'k2': 200}
print(new_dict)
new_dict['k3'] = 300 #definē jaunu elementu
print(new_dict)
new_dict['k1'] = "simts"
print(new_dict)

#vārdnīcu metodes
print(new_dict.keys()) #izdrukā atslēgas
print(new_dict.values()) #izdrukā vērtības
print(new_dict.items()) #izdrukā pārus