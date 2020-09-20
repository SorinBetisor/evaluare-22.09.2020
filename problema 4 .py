#Se dă numărul natural n.
#- Să se transforme n metri în centimetri;
#- Să se transforme n kilograme în miligrame;
#- Să se transforme n ani în luni, săptămâini, zile (1 an=365 zile)
n= int(input("Introduceti valoarea lui n : "))
print (f'Ati introdus valoarea {n}')
ncm= n * 100
nmg= n * 1000000
nluni= n * 12
nsaptamaini= n * 52 #un an complet are aprox 52 saptamani
nzile= n * 365
print (f'{n}','metri in centrimetri = ',ncm)
print (f'{n}','kilograme in miligrame = ',nmg)
print (f'{n}','ani in luni = ',nluni)
print (f'{n}','ani in saptamani = ',nsaptamaini)
print (f'{n}','ani in zile = ',nzile)




