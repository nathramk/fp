print "inicio del programa: "
numero=input("ingrese numero: ")
frase=raw_input("ingrese apodo: ")
for i in range(numero):
    
     print "%s, %s"% (i+1,frase)


print "fin del programa"

print "tabla de multiplicar"
for i in range(10):
    for j in range(12):
        print "%s*%s=%s"%(j+1,i+1,(j+1)*(i+1))
    print "tabla de: %s "%(i+1)
    print "--------------"
print "fin del programa"

