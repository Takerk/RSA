import sys
import random

def generarLlave():
    p = 47
    q = 71
    n = p * q
    phi = (p-1)*(q-1)
    e = aleatorioE(phi)
    d = eea(phi,e)
    print 'Llave pública: (',e,',',n,')'
    print 'Llave privada: (',d,',',n,')'

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

def encriptar():
    generarLlave()
    print 'AQUI SE VA A ENCRIPTAR'

def desencriptar():
    print 'AQUI SE VA A DESENCRITAR'

def main():
    print 'Bienvenido al sistema de encriptación RSA \n    Por favor seleccione una opción'
    print '\n1.Encriptar \n2.Desencripar \n3.Salir'
    menu = {'1': 'Encriptar', '2': 'Desencriptar', '3': 'Salir'}
    T= sys.stdin.readline()
    if (T == '1'):
        encriptar()
    elif (T== '2'):
        desencriptar()
    elif (T== '3'):
        print 'Hasta pronto :D'
    else:
        print 'Opcion inválida\nIntente de nuevo \n\n'
        main()

def test():   
    a = 79
    b = 3220
    w = gcd(a,b)
    print 'Primos relativos ' , w
    z = eea(b,a)
    print 'Algoritomo extendido de Euclides', z

main()

