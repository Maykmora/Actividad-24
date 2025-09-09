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

while True:
    print("--MENÚ--")
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
            print()
        case "5":
            print()
        case "6":
            print()
        case "7":
            print("Gracias por usar el programa.")
            break