def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def sum_nat(n):
    if n<0:
        return 0
    else:
        return n+sum_nat(n-1)
def fibonacci(n):
    if n==1 or n==0:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
def contar_letra(palabra, letra):
    if palabra=="" or letra=="":
        return 0
    else:
        if palabra[0]==letra:
            return 1+contar_letra(palabra[1:], letra)
        else:
            return contar_letra(palabra[1:], letra)

while True:
    print("\n--MENÚ--")
    print("1.Calcular factorial")
    print("2.Suma de primeros N números naturales")
    print("3.Calcular el n-ésimo numero de Fibonacci")
    print("4.Contar cuantas veces aparece una letra en una palabra")
    print("5.Invertir una cadena de texto")
    print("6.Calcular la potencia de un numero")
    print("7.Salir")
    option=input("\nSeleccione una opción del menú (1-7): ")

    match option:
        case "1":
            print("\n--FACTORIAL--")
            n=int(input("Ingrese el numero que desea para encontrar su factorial: "))
            print(factorial(n))
        case "2":
            print("\n--SUMA--")
            n=int(input("Ingrese el numero que desea:"))
            print(sum_nat(n))
        case "3":
            print("\n--FIBONACCI--")
            n=int(input("Ingrese el numero de posicion que desea encontrar: "))
            print(fibonacci(n))
        case "4":
            print("\n--CONTADOR DE LETRAS--")
            palabra=input("Ingrese la palabra que desea:").lower()
            letra=input("Ingrese la letra que desea buscar en la palabra: ").lower()
            print(f"La letra '{letra}' aparece {contar_letra(palabra, letra)} veces")
        case "5":
            print()
        case "6":
            print()
        case "7":
            print("Gracias por usar el programa.")
            break