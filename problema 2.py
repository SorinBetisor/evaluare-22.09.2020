#Se dau două numere întregi a şi b. Să se determine suma, diferenţa, câtul împărţirii, restul
#împărţirii, produsul şi ridicarea la putere.(a – baza, b – exponentul)
a= int(input("Introduceti o valoare pentru a: "))
#print (f'Ati introdus valoarea {a}')
b= int(input("Introduceti o valoare pentru b: "))
#print (f'Ati introdus valoarea {b}')
suma = a + b
print ("Suma a+b")
print (a," + ",b," = ",suma)
dif = a - b
print ("Diferenta a-b")
print (a," - ",b," = ",dif)
catul = a // b
print ("Catul a:b")
print (a," : ",b," = ",catul)
restul = a % b
print ("Restul a:b")
print (a," : ",b," = ",restul)
produsul= a*b
print ("Produsul a*b")
print (a," * ",b," = ",produsul)
putere = a**b
print ("a la puterea b")
print (a," ** ",b," = ",putere)





