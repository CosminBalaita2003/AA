#cmmmc a b calcul cmmmc-ul dintre a si b
def cmmmc(a,b):
    if a==b:
        return a
    if a>b:
        a,b=b,a
    for i in range(b,a*b+1,b):
        if i%a==0:
            return i
    return a*b

for a in range(1,9):
    for b in range(1,9):
        x=cmmmc(a,b)
        if (a**2+b**2)%x==0 : #a la 2 + b la 2 trebuie sa fie divizibil cu cmmmc-ul si a sa fie diferit de b
            print (a,b)
