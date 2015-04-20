#calcular la suma de los N primero termial
#entrada
r=0 
a=input("ingrese valor: ")
#proceso
for i in range(a):
    r=r+(i+1)
#salida
print r

#calcule la suma de la siguiente serie 
#entrada
x=input("ingrese valor: ")
n=input("ingrese valor: ")
s=0
#proceso
for i in range(n):
    s=s+(x**i)
#salida 
print s

print "ingrese faltorial de un numero"

#entrada
r=1

f=input("ingrese factorial: ")
#proceso
for i in xrange(1,f+1):
    r=r*i
#salida 
print r


