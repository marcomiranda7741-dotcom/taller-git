
def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True




def obtener_numero_entrada(msj):
    while True:
        try:
            return int(input(msj))
        except ValueError:
            print("Error: ingrese un numero")

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Primos")
        print("4. N números perfectos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función de Fibonacci (Estudiante 2)")
        elif opcion == "2":
            print("Función de Factorial (Estudiante 3)")
       
        elif opcion == "3":
            print("Función de Primos (Estudiante 4)")
            n = obtener_numero_entrada("Ingrese el numero para verificar si es primo: ")
            resultado = es_primo(n)
            if resultado:
                print(f"{n} es primo")
            else:
                print(f"{n} NO es primo")

        elif opcion == "4":
            print("Función de N números perfectos (Estudiante 5)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
