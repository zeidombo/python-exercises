def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)
n=int(input("Entrer un nombre entier :"))
m="{:,}".format(factoriel(n))
print(m)