numero=input("ingrese el numero del factorial: ")
resultado=1
for i in xrange(2,numero+1):
    resultado = resultado * i
print "%s!=%s"%(numero, resultado)
