#ARİTMETİKSEL OPERATÖRLER

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#Karşılaştırma operatörleri

x = 5
y = 10

print(x > y)
print(x == y)
print(x != y)

#Mantıksal Operatörler

print( x > 3 and y < 15) #True
print( x > 3 or y < 9) #True 
print( not(x<6)) #True 

"""
if kosul:
    Şart sağlanınca yapılacaklar
elif kosul:
    Şart sağlanınca yapılacaklar
else:
    Şartlar sağlanmazsa
"""

yas = 19

if yas < 18:
    print("Reşit değilsiniz!")
elif yas == 18:
    print("Tam sınırdasınız")
else:
    print("Reşitsiniz")
