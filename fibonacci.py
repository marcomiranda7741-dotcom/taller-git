# Estudiante 2 - Función Fibonacci

def calcular_fibonacci(n):
    """
    Retorna una lista con los primeros n números de la serie Fibonacci.
    Validación incluida para evitar errores.
    """

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


# Bloque de prueba local (solo para ti, no afecta al menú)
if __name__ == "__main__":
    try:
        cantidad = int(input("Ingrese cuántos números Fibonacci desea generar: "))
        print(calcular_fibonacci(cantidad))
    except ValueError:
        print("Debe ingresar un número entero.")
