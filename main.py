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
        elif opcion == "4":
            print("Función de N números perfectos (Estudiante 5)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
