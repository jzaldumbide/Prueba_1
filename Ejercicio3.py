def leertxt():
    archi=open('e2.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
        frase=linea
        archi.close()
        print (linea)
    archi.close()
    linea = linea.split()
    nlinea = len(linea)
    print (nlinea)

leertxt()
print(len(frase))