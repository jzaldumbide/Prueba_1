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
        frase=linea.splitline()
        #frase= frase.split()
        print(frase)
        archi.close()
        print (linea)
    archi.close()
leertxt()

