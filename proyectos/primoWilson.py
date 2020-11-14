def es_primo(n):
    factorial = 1
    if n < 0:
        return 0
    elif n == 0:
        return 1
    while (n > 1):
        factorial *= n
        n -= 1
    
    # print(factorial)
    return factorial

def main():
    numero = int(input("Escribe un numero: "))
    wilson = es_primo(numero - 1) + 1
    
    #print(wilson)
    if wilson % numero == 0:
        # print(wilson/numero)
        print("El numero es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    main()