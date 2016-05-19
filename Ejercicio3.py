def leertxt():
    archi=open('texto.txt','r')
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
