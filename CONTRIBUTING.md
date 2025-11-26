# Guía para Contribuir al Proyecto

Gracias por colaborar. Sigue estas reglas para mantener el repositorio ordenado y facilitar la integración.

## Reglas básicas
1. Cada integrante trabaja en **su propia rama**. No trabajes en `master`/`main`.
2. No modificar el menú (archivo `main.py`) salvo indicación del Estudiante 1.
3. Hacer commits pequeños y descriptivos.
4. Probar localmente antes de subir.
5. Todo cambio va mediante **Pull Request** hacia `master`/`main`.
6. Etiquetar al Estudiante 1 y al QA en el PR para revisión.

## Nomenclatura de ramas
- `feature-<funcion>` → para nuevas funcionalidades (ej: `feature-fibonacci`)
- `bugfix/<breve-descripcion>` → para correcciones
- `docs/<tema>` → para documentación

## Flujo recomendado
1. Actualiza tu rama local:
   ```bash
   git checkout master
   git pull origin master
