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
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def es_perfecto(n: int) -> bool:
    if n < 2:
        return False
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n


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


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Secuencia de Fibonacci")
        print("2. Función de Factorial (Lista completa - Estudiante 3)")
        print("3. Verificar si un número es Primo")
        print("4. N primeros números Perfectos")
        print("5. Cálculo del Factorial de un número") 
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            manejar_opcion_fibonacci()
        
        elif opcion == "2":
            manejar_opcion_factorial_estudiante()
        
        elif opcion == "3":
            manejar_opcion_primos()
        
        elif opcion == "4":
            manejar_opcion_perfectos()
            
        elif opcion == "5":
            manejar_opcion_factorial_individual()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("🚫 Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
