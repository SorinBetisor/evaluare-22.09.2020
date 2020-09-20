
# INTRODUCETI NUMAR DIN 5 cifre"""
n= int(input("Introduceti numarul n : "))
ult= n % 10
print (f'Ultima cifra a numarului {n} = {ult}')
penult= n // 10
penult2= penult % 10
print (f'Penultima cifra a numarului {n} = {penult2}')
rest9= n % 9
cat9= n // 9
print (f'Restul impartirii numarului {n} la 9 = {rest9}')
print (f'Catul impartirii numarului {n} la 9 = {cat9}')
urma3 = n // 100 % 10
urma4 = n // 1000 % 10
primul = n // 10000
sumacifrelor= primul+urma4+urma3+penult2+ult
print ("Suma cifrelor = ")
print (f'{primul} + {urma4} + {urma3} + {penult2} + {ult} = {sumacifrelor}')
print (f'Rasturnatul = {ult}{penult2}{urma3}{urma4}{primul}')




