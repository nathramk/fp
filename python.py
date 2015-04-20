#se requiere un programa que lea 3 lados de un triangulo cualquiera y calcule su area, considerar si A, B, C son los lados y S el semiperimetro.
#entrada
a=input("ingrese un lado: ")
b=input("ingrese un lado2: ")
c=input("ingrese un lado3: ")
s=input("ingrese el semiperimetro: ")
#proceso
area=(s*(a-s)*(b-s)*(c-s))**0.5
#salida
print "el area es: %s"% area


