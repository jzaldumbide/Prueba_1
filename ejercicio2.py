s= int(1)
contador= int(0)
suma= int(0)
resultado= int(0)
while(s==1):
	r=int(input("Ingrese un numero\n"))
	suma=suma+r
	contador=contador+1
	if (r==0):
		s=0
resultado= suma/contador
print (" EL promedio es: "+str(resultado))

