#lists jeb saraksti
#['Sveika,', 100, 'tu', 3.59, 'skaista!', [1,26]]
myList = [1, 2, 3, 100, 'tu', 3.59, 'skaista!']
print(len(myList))  #saraksta garums

my_list = ["viens", "divi", "trīs", 'četri']
print(my_list[0])  #izdrukā elementu ar norādīto indeksu
print(my_list[1:])  #izdrukā no norādītā indeksa līdz beigām

#sarakstu apvienošana jeb konkatinācija
cits_list = ["pieci", "seši"]
print(my_list + cits_list)  #izdrujā sarakstu ar abu mainīgo elementiem
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
new_list = ['b', 'a', 'z', 'e']
print(new_list)
num_list = [4, 1, 8, 3]
print(num_list)
new_list.sort()
print(new_list)
num_list.sort()
print(num_list) 
num_list.reverse()
print(num_list)