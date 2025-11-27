# 🧪 Plan de Pruebas – Taller Git

Este documento describe las pruebas que debe ejecutar cada estudiante antes de enviar su Pull Request.

---

## ✔️ 1. Pruebas funcionales

### 🔹 Menú Principal
- [ ] El menú muestra todas las opciones.
- [ ] Cada opción llama correctamente a su función.

### 🔹 Funciones matemáticas
Para cada función implementada por estudiantes:

- **Fibonacci**
  - [ ] Devuelve la secuencia correcta.
  - [ ] Maneja correctamente entradas pequeñas (0, 1, 2).
  - [ ] Maneja números grandes sin fallar.

- **Números perfectos**
  - [ ] Identifica correctamente números perfectos como 6, 28.
  - [ ] Retorna lista vacía si no hay números perfectos en el rango.

- **Factorial**
  - [ ] Devuelve factorial correcto.
  - [ ] Maneja el caso 0 correctamente → resultado = 1.

- **Primos**
  - [ ] Identifica correctamente números primos.
  - [ ] No marca como primo números compuestos.

---

## ✔️ 2. Pruebas de integración
- [ ] Todas las funciones están integradas en el menú.
- [ ] No hay importaciones duplicadas o rutas incorrectas.
- [ ] Las funciones no se bloquean entre sí.

---

## ✔️ 3. Pruebas de errores
- [ ] Si el usuario ingresa letras, se maneja el error (no se rompe el programa).
- [ ] Si el usuario ingresa números negativos, el programa responde adecuadamente.
- [ ] No se produce ningún crash inesperado.

---

## ✔️ 4. Resultado esperado
Si todas las pruebas pasan, el PR está listo para ser enviado.
