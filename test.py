def je_prastevilo(n):
    if n == 2 or n == 3:
        return True 
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3,n):
        if n % i == 0:
            return False
    return True

for i in range(200):
    if je_prastevilo(i):
        print(i)