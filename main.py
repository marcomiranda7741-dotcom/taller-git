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


def fibonacci(n: int) -> list:
menu
    if n <= 0:
        return []
    if n == 1:
        return [0]

    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial no definido para números negativos")
    

    if not isinstance(n, int):
        return "Error: debe ingresar un número entero."

    if n <= 0:
        return "Error: el número debe ser mayor que 0."

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])

    return serie


def factorial(n: int) -> int:
master
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def es_perfecto(n: int) -> bool:
    if n < 2:
        return False
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n


menu
def primeros_n_perfectos(cantidad: int) -> list:
    encontrados = []
    num = 1

    while len(encontrados) < cantidad:
        if es_perfecto(num):
            encontrados.append(num)
        num += 1

    return encontrados


def obtener_numero_entrada(msj):
    """Solicita una entrada entera y maneja errores de valor. 
       Devuelve un entero o lanza un ValueError si la entrada está vacía."""
    entrada = input(msj).strip()
    if not entrada:
        raise ValueError("Entrada vacía, volviendo al menú.")
    try:
        return int(entrada)
    except ValueError:
        print("❌ Error: ingrese un número entero válido.")
        raise


def manejar_opcion_fibonacci():
    print("\n--- Función de Fibonacci ---")
    while True:
        try:
            n = obtener_numero_entrada("¿Cuántos números desea generar? (o presione Enter para volver): ")
            print("Secuencia:", fibonacci(n))
        except ValueError:
            break
        
        continuar = input("\nPresione **Enter** para otra operación o ingrese **M** para volver al Menú Principal: ").strip().upper()
        if continuar == 'M':
            break

def manejar_opcion_factorial_individual():
    print("\n--- Cálculo del Factorial de un número ---")
    while True:
        try:
            n = obtener_numero_entrada("Ingrese un número para calcular su factorial (o presione Enter para volver): ")
            print(f"El factorial de {n} es: {factorial(n)}")
        except ValueError as e:
            if "Factorial no definido" in str(e):
                print(f"❌ Error: {e}")
                continue 
            break 
        except Exception: # Captura si el usuario solo presiona Enter
            break

        continuar = input("\nPresione **Enter** para otra operación o ingrese **M** para volver al Menú Principal: ").strip().upper()
        if continuar == 'M':
            break
            
def manejar_opcion_factorial_estudiante():
    print("\n--- Función de Factorial (Lista completa - Estudiante 3) ---")
    while True:
        try:
            n = obtener_numero_entrada("Ingrese un número para calcular su factorial (o presione Enter para volver): ")
            print(f"Factorial de {n} = {factorial(n)}")
        except ValueError:
            break

        continuar = input("\nPresione **Enter** para otra operación o ingrese **M** para volver al Menú Principal: ").strip().upper()
        if continuar == 'M':
            break

def manejar_opcion_primos():
    print("\n--- Función de Primos ---")
    while True:
        try:
            n = obtener_numero_entrada("Ingrese un número para verificar si es primo (o presione Enter para volver): ")
            print(f"⭐ {n} es primo" if es_primo(n) else f"❌ {n} NO es primo")
        except ValueError:
            break

        continuar = input("\nPresione **Enter** para otra operación o ingrese **M** para volver al Menú Principal: ").strip().upper()
        if continuar == 'M':
            break

def manejar_opcion_perfectos():
    print("\n--- N primeros números perfectos ---")
    while True:
        try:
            n = obtener_numero_entrada("¿Cuántos números perfectos desea obtener? (o presione Enter para volver): ")
            print(f"Primeros {n} números perfectos:", primeros_n_perfectos(n))
        except ValueError:
            break

        continuar = input("\nPresione **Enter** para otra operación o ingrese **M** para volver al Menú Principal: ").strip().upper()
        if continuar == 'M':
            break

def generar_numeros_perfectos(limite: int) -> list:
    perfectos = []

    for num in range(2, limite + 1):
        suma_divisores = 0

        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                suma_divisores += i
                otro = num // i
                if otro != i and otro != num:
                    suma_divisores += otro

        if suma_divisores == num:
            perfectos.append(num)

    return perfectos


def calcular_factorial_individual():
    n = obtener_numero_entrada("Ingrese un número para calcular su factorial: ")
    print(f"El factorial de {n} es: {factorial(n)}")


def obtener_numero_entrada(msj):
    while True:
        try:
            return int(input(msj))
        except ValueError:
            print("Error: ingrese un número válido.")
master


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
menu
        print("1. Secuencia de Fibonacci")
        print("2. Función de Factorial (Lista completa - Estudiante 3)")
        print("3. Verificar si un número es Primo")
        print("4. N primeros números Perfectos")
        print("5. Cálculo del Factorial de un número") 
        print("6. Salir")

        print("1. Fibonacci")
        print("2. Factorial (lista completa)")
        print("3. Primos")
        print("4. N números perfectos")
        print("5. Salir")
        print("6. Cálculo del factorial de un número")  # ⭐ Nueva opción agregada ⭐
master

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
menu
            manejar_opcion_fibonacci()
        
        elif opcion == "2":
            manejar_opcion_factorial_estudiante()
        
        elif opcion == "3":
            manejar_opcion_primos()
        
        elif opcion == "4":
            manejar_opcion_perfectos()
            

            print("\n--- Función de Fibonacci ---")
            try:
                n = obtener_numero_entrada("Ingrese cuántos números Fibonacci desea generar: ")
                print(fibonacci(n))
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "2":
            print("\n--- Función de Factorial (Estudiante 3) ---")
            n = obtener_numero_entrada("Ingrese un número para calcular su factorial: ")
            print(f"Factorial de {n} = {factorial(n)}")

        elif opcion == "3":
            print("\n--- Función de Primos ---")
            n = obtener_numero_entrada("Ingrese un número para verificar si es primo: ")
            print(f"{n} es primo" if es_primo(n) else f"{n} NO es primo")

        elif opcion == "4":
            print("\n--- N primeros números perfectos ---")
            n = obtener_numero_entrada("¿Cuántos números perfectos desea obtener?: ")
            print(f"Primeros {n} números perfectos:", generar_numeros_perfectos(n))

master
        elif opcion == "5":
            manejar_opcion_factorial_individual()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

menu
        else:
            print("🚫 Opción inválida, intente de nuevo.")

        elif opcion == "6":  # ⭐ Nueva opción implementada ⭐
            print("\n--- Cálculo del factorial de un número ---")
            calcular_factorial_individual()

        else:
            print("Opción inválida, intente de nuevoo.")
master


if __name__ == "__main__":
    main() 