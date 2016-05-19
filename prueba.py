def menu():
    print("Prueba Programacion Avanzada")

def suma():
    x1 = int(input("Ingrese el valor de x1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    y1 = int(input("Ingrese el valor de y1: "))
    y2 = int(input("Ingrese el valor de y2: "))
    z1 = int(input("Ingrese el valor de z1: "))
    z2 = int(input("Ingrese el valor de z2: "))
    coor1 = x1 + x2
    coor2 = y1 + y2
    coor3 = z1 + z2
    print ("las coordenadas del punto son: ")
    print("x: " + str(coor1))
    print("y: " + str(coor2))
    print("z: " + str(coor3))

def ejercicio2()
	s= int(1)
	contador= int(0)
	suma= int(0)
	resultado= int(0)
		while(s==1):
			r=int(input("Ingrese un numero\n"))
			suma+=r
			contador+=1
			if (r==0):
				s=0
			resultado= suma/contador
		print (" EL promedio es: "+str(resultado))



menu()

suma()