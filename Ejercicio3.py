def reverse(list):
    if len(list)==1:
        return list
    else:
        return list[-1]+reverse(list[:-1])

def leertxt():
    archi=open('texto.txt','r')
    linea=archi.readline()
    while linea!="":
        print (linea)
        linea=archi.readline()
        frase=list(str(linea))
        print(reverse (str(frase)))
        archi.close()
        print (linea)
    archi.close()
leertxt()

