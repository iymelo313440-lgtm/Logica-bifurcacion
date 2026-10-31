# Proyecto Final – Módulo 2
## Fundamentos de Python

### Descripción del proyecto

Este proyecto integra dos ejercicios desarrollados durante el módulo, utilizando estructuras de control, conversión de tipos de datos y manejo de excepciones.

El programa cuenta con un menú interactivo que permite seleccionar entre dos funcionalidades:

1. **Validación de longitud:** solicita una palabra y determina si tiene menos de 4 caracteres, más de 8 o una longitud entre 4 y 8 caracteres.
2. **Identificación de cuadrantes:** solicita las coordenadas X e Y de un punto y determina en cuál de los cuatro cuadrantes del plano cartesiano se encuentra.

También incluye una opción para salir del programa.

### Conceptos y herramientas aplicados

Durante el desarrollo se utilizaron los siguientes elementos de Python:

- **Variables:** almacenamiento de datos ingresados por el usuario.
- **Conversión de tipos:** uso de `int()` para convertir la opción del menú a entero y `float()` para trabajar con coordenadas decimales.
- **Estructuras condicionales:** `if`, `elif` y `else` para evaluar condiciones y tomar decisiones.
- **Ciclos:** `while` para mantener activo el menú y repetir las solicitudes cuando los datos ingresados no son válidos.
- **Manejo de excepciones:** `try` y `except ValueError` para controlar entradas no numéricas y evitar que el programa se interrumpa.
- **Control de ciclos:** `break` y `continue` para gestionar la repetición y salida de los procesos.

### Cómo ejecutar el programa

1. Tener Python instalado.
2. Descargar o clonar este repositorio.
3. Abrir el proyecto desde Visual Studio Code o una terminal.
4. Ejecutar el archivo:

```bash
python IVONEE_MELO_proyectoM2.py
```

### Reflexión sobre el aprendizaje

La integración de estos ejercicios me permitió comprender mejor cómo las estructuras de control ayudan a organizar la lógica de programación.

Al principio, los ejercicios funcionaban de manera independiente, pero al integrarlos en un menú fue necesario establecer condiciones para dirigir el flujo del programa y utilizar ciclos para mantenerlo activo.

También comprendí la importancia de validar los datos ingresados por el usuario y manejar posibles errores mediante excepciones. La conversión de tipos de datos me permitió trabajar correctamente con entradas numéricas, mientras que las estructuras condicionales facilitaron la toma de decisiones según cada situación.

Este ejercicio fortaleció mi capacidad para analizar problemas, dividirlos en procesos más pequeños y construir una solución organizada, funcional y comprensible.

---

**Proyecto desarrollado como parte del Bootcamp de Python – Módulo 2.**
