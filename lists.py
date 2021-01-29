#lists jeb saraksti
#['Sveika,', 100, 'tu', 3.59, 'skaista!', [1,26]]
myList = [1, 2, 3, 100, 'tu', 3.59, 'skaista!']
print(len(myList))  #saraksta garums

my_list = ["viens", "divi", "trīs", 'četri']
print(my_list[0])  #izdrukā elementu ar norādīto indeksu
print(my_list[1:])  #izdrukā no norādītā indeksa līdz beigām

#sarakstu apvienošana jeb konkatinācija
cits_list = ["pieci", "seši"]
print(my_list + cits_list)  #izdrukā sarakstu ar abu mainīgo elementiem
jauns_list = my_list + cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0] = 1
print(jauns_list)

jauns_list.append("septiņi")  #pievieno pēdējo elementu
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

pop_elem = jauns_list.pop(0)  #noņem elementu ar norādīto indeksu
print(jauns_list)
print(pop_elem)

#elementu kārtošana
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort()  #sakārto pēc alfabēta
print(new_list)
num_list.sort(
)  #sakārto, BET jāizmanto kā atsevišķa metode, to nevar izmantot kā darbību
print(num_list)
num_list.reverse()  #sakārto pretējā secībā
print(num_list)
myList = [1, 2, 3, 100, 3.59]
myList.sort()
print(myList)

#saraksts sarakstā (nested)
nested_list = [1, 5, [7, 2]]
print(nested_list[2][1])

augli = ["ābols", "banāns", "gurķis"]
print(augli[2])
#aizstāt elementu - gurķis -> apelsīns
augli[2] = "apelsīns"
print(augli)

#pievienot beigās "bumbieris"
augli.append("bumbieris")
print(augli)

#iespraust konkrētā vietā jaunu elementu "citrons"
augli.insert(2, "citrons")
print(augli)

#izņemt no saraksta "banāns"
augli.pop(1)
print(augli)

#izdrukāt pilnā teikumā, cik augļi ir sarakstā
print(f"Sarakstā ir {len(augli)} dažādi augļi.")