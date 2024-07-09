def divisible_enteros (n, d):
    if n % (2 * d) == 0:
        return 2
    elif n % d == 0:
        return 1
    else:
        return 0 
    n = int (input("ingrese valor de n: "))
    d = int (input("ingrese valor de d: "))
    
    resultado = divisible_enteros (n, d)
    print ("resultado:", resultado)