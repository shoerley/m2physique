def pgcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

"""
Le processus implémenté est celui du PGCD
"""