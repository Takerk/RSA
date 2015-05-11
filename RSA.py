import sys
import random

#Encriptación y desencriptación

def powerMod(mc,ed,n):
    base = mc
    lbinario = listaBinario(ed);
    del lbinario[0]
    if ed < 0:
         del lbinario[0]
    for i in lbinario:
        if i=='1':
            mc = (mc*mc*base)% n
        else:
            mc=(mc*mc)%n
    return mc

def listaBinario(ed):
    lista=[]
    binario=bin(ed)
    for i in binario:
        lista.append(i)
    del lista[0]
    del lista[0]
    return lista

def descomponer(n):
    

#...Encriptación y desencriptación


#Generar llave

def numPrimos():
    archivo=open("primos.txt")
    lineas=len(open("primos.txt").readlines())
    plinea=random.randrange(lineas)
    qlinea=random.randrange(lineas)
    while(plinea==qlinea):
     qlinea=random.randrange(lineas)
    for i in range(lineas):
        if i==plinea:
            p=int(archivo.next())
        else:
            if i==qlinea:
                q=int(archivo.next())
            else:
                archivo.next()
    archivo.close()
    return p,q

def aleatorioE(phi):
    e = random.randint(2,(phi-1))
    g = gcd(e,phi)
    if(g!= True):
        return aleatorioE(phi)
    else:
        return e
    
def gcd(e,phi):
    r = e % phi
    if (r == 0):
        return False
    if (r == 1):
        return True
    else:
        x  = e / phi
        y = int(x)
        return gcd(phi,r)

def eea(phi,e):
    listaPhi=[]
    listaE=[]
    listaR=[]
    listaPhi.append(phi)
    listaE.append(e)
    r=1
    
    while(r!=0):
        r = phi % e
        listaR.append(r)
        phi= e
        e = r
        listaPhi.append(phi)
        listaE.append(e)
    x = 0
    gh = -len(listaPhi)
    i=-2
    while(i>=gh):
        a = listaPhi[i]
        b = listaE[i]
        y =  (-(a*x)+1)/b
        x = y
        i = i -1
    return y

#...Generar llave

def generarLlave():
    p,q = numPrimos()
    n = p * q
    phi = (p-1)*(q-1)
    e = aleatorioE(phi)
    d = eea(phi,e)
    print '\nLlave pública: (',e,',',n,')'
    print 'Llave privada: (',d,',',n,')'
    return e,d,n 

def encriptar():
    ent=[]
    textoPlano = []
    c = []
    print '\nAQUI SE VA A ENCRIPTAR'
    print 'Ingrese el texto que desea cifrar \nInstrucciones: ingrese los números separados entre sí por un espacio \nal terminar de ingresar el mensaje presione enter y obtendrá un mensaje cifrado.'
    tp = sys.stdin.readline().strip().split()
    for i in range(len(ent)):
        textoPlano.append(int(ent[i]))
    e,d,n = generarLlave()
    for i in range(len(textoPlano)):
        m = textoPlano[i]
        c.append(powerMod (m,e,n))
    print '\nMensaje cifrado: \n'
    for i in range(len(c)):
        print c[i]
    
def desencriptar():
    ent=[]
    textoPlano = []
    c = []
    print '\nAQUI SE VA A DESENCRITAR'
    print'Ingrese la llave pública (cada término separado por un espacio (e,n))'
    llaveP = sys.stdin.readline().strip().split()
    e = int(llaveP[0])
    n = int(llaveP[1])
    print 'Ingrese el texto cifrado \nInstrucciones: ingrese los números separados entre sí por un espacio \nal terminar de ingresar el mensaje presione enter y obtendrá el mensaje original.'
    ent = sys.stdin.readline().strip().split()
    for i in range(len(ent)):
        c.append(int(ent[i]))
    

def main():
    try:
        print '\nBienvenido al sistema de encriptación RSA \n    Por favor seleccione una opción'
        print '\n1.Encriptar \n2.Desencripar \n3.Salir'
        menu = {'1': 'Encriptar', '2': 'Desencriptar', '3': 'Salir'}
        T= int(sys.stdin.readline())
        if (T==1):
            encriptar()
            main()
        elif (T==2):
            desencriptar()
            main()
        elif (T==3):
            print 'Hasta pronto :D'
        else:            
            print 'Opcion inválida\nIntente de nuevo \n\n'
            main()
    except ValueError:
        print'Opción inválida\nIntente denuevo \n\n'
        main()

def test():   
    a = 79
    b = 3220
    w = gcd(a,b)
    print 'Primos relativos ' , w
    z = eea(b,a)
    print 'Algoritomo extendido de Euclides', z

main()
