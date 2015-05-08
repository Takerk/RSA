

def esprimo(numero):
    contador=0
    verificar= False
    for i in range(1,numero+1):
        if (numero%i)==0:
            contador=contador+1
        if contador >= 3:
            verificar=True
            break
    if contador==2 or verificar==False:
        return 1
    else:
        return 0

limite=50000000
inicio=1000000

print('Generacion de p y q, ambos primos')
p=0
q=0
print(esprimo(999769))
encontrado=0
n=inicio
while(n<=limite):
    if esprimo(n):
        encontrado=n
        print(encontrado)
    n=n+1




