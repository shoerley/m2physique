

def magic_function(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * magic_function(n-1)


"""
Cet exo était à rendre sur feuille. 

Il s'agit de la fonction factorielle.
    magic_function(2) = 2
    magic_function(4) = 24
    
La justification était nécessaire pour avoir les points.
"""

def factorielle(n):
    f = 1

    for i in range(1, n+1):
        f = f * i
    return f

