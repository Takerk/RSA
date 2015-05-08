def keyGenerator():
    p = 47
    q = 71
    n = p * q
    phi = (p-1)*(q-1)
    
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


a = 79
b = 3220

w = gcd(a,b)
print 'Primos relativos ' , w

z = eea(b,a)
print 'Algoritomo extendido de Euclides', z
