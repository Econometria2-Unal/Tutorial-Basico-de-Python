# # Tutorial 1: Python Básico
# Este módulo cubre los fundamentos de Python.
# Usar `# %%` para ejecutar cada celda de forma independiente en VSCode.

# %% 1. Variables y tipos de datos``
# Python es un lenguaje interpretado (permite correr línea por línea) 
# y además es de tipado dinámico (No necesitas declarar el tipo de una variable).

diez_entero = 10
numero_pi_flotante = 3.14
texto = "Hola, Econometría"
booleano = True

# Dos formas de imprimir en python

# 1. Impresión normal: print()

print("Impresión normal usando la función print()")

print("entero", diez_entero)
print("flotante", numero_pi_flotante)
print("texto", texto)
print("booleano", booleano)


print("\n")

# 2. Impresión con formato especial print(f)

print("Impresión con formato especial usando la función print(f"")")

print(f"entero: {diez_entero} (tipo: {type(diez_entero).__name__})")
print(f"flotante: {numero_pi_flotante} (tipo: {type(numero_pi_flotante).__name__})")
print(f"texto: {texto} (tipo: {type(texto).__name__})")
print(f"booleano: {booleano} (tipo: {type(booleano).__name__})")


# %% 2. Operaciones aritméticas

a = 15
b = 4

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo: {a % b}")
print(f"Potencia: {a ** b}")
# %% 3. Operaciones lógicas
x = True
y = False

print(f"AND: {x and y}")
print(f"OR: {x or y}")
print(f"NOT x: {not x}")
print(f"NOT y: {not y}")
print(f"x AND (NOT y): {x and not y}")
print(f"(NOT x) OR y: {not x or y}")

# %% 4. Strings (cadenas de texto)

nombre = "Econometría"
version = "II"

# Concatenación
curso = nombre + " " + version
print(curso)

# f-strings (formato recomendado)
print(f"Bienvenido al curso de {nombre} {version}")

# Métodos útiles de strings
print(f"Mayúsculas: {curso.upper()}")
print(f"Minúsculas: {curso.lower()}")
print(f"Longitud: {len(curso)}")
print(f"Reemplazar: {curso.replace('II', 'III')}")

# Slicing
print(f"Primeros 5 caracteres: {curso[:5]}")
print(f"Últimos 2 caracteres: {curso[-2:]}")
# %% 5. Listas

# Las listas son colecciones ordenadas y mutables
notas = [3.5, 4.0, 2.8, 4.5, 3.9]
print(f"Notas: {notas}")
print(f"Primera nota: {notas[0]}")
print(f"Última nota: {notas[-1]}")

# Agregar elementos
notas.append(4.2)
print(f"Después de append: {notas}")

# Insertar en posición específica
notas.insert(0, 5.0)
print(f"Después de insert: {notas}")

# Eliminar elementos
notas.remove(5.0)
print(f"Después de remove: {notas}")

# Slicing de listas
print(f"Primeras 3 notas: {notas[:3]}")

# List comprehension
notas_altas = [n for n in notas if n >= 4.0]
print(f"Notas >= 4.0: {notas_altas}")
# %% 6. Tuplas

# Las tuplas son colecciones ordenadas e inmutables
coordenadas = (4.6097, -74.0817)  # Bogotá
print(f"Latitud: {coordenadas[0]}")
print(f"Longitud: {coordenadas[1]}")

# Desempaquetado
lat, lon = coordenadas
print(f"Lat: {lat}, Lon: {lon}")
# %% 7. Diccionarios

# Los diccionarios almacenan pares clave-valor
estudiante = {
    "nombre": "Ana García",
    "código": 1234567,
    "semestre": 7,
    "notas": [4.0, 3.5, 4.5]
}

print(f"Nombre: {estudiante['nombre']}")
print(f"Semestre: {estudiante['semestre']}")

# Agregar o modificar
estudiante["carrera"] = "Economía"
print(f"Estudiante completo: {estudiante}")

# Imprimir las keys del diccionario
print(f"Las 'keys' del estudiante son: {estudiante.keys()}")

# Imprimir las values del diccionario
print(f"Las 'values' del estudiante son: {estudiante.values()}")

# Iterar sobre un diccionario
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")
# %% 8. Condicionales (Estructuras de control de flujo)

nota_final = 3.2

if nota_final >= 4.0:
    print("Le sabe")
elif nota_final >= 3.0:
    print("Paso raspando, papu")
else:
    print("Vago 😸")

# Operador ternario
resultado = "Aprobó" if nota_final >= 3.0 else "Reprobó"
print(f"Resultado: {resultado}")

# %% 9. Ciclos (loops)

# For loop
print("--- For loop ---")
materias = ["Econometría con germancho", "Microeconomía con pachito god", "polmacro con IsiGod??"]
for materia in materias:
    print(f"  Materia: {materia}")

# For con enumerate (obtener índice y valor)
print("--- Enumerate ---")
for i, materia in enumerate(materias):
    print(f"  {i}: {materia}")

# For con range
print("--- Range ---")
for contador in range(5):
    print(f"  Iteración {contador}")

# While loop
print("--- While loop ---")
acumulador = 0
while acumulador < 3:
    print(f"  Contador: {acumulador}")
    acumulador += 1

# %% 10. Funciones

# Ejemplo de función en python: 
def encontrar_maximo(lst): 
    """Encontrar el máximo de una lista de elementos

    Args:
        lst (list): Lista que contiene los enteros de números del cuál se quiere encontrar el máximo
    """
    if len(lst) > 0:    
        maximo = 0
        for numero in lst:
            if numero > maximo:
                maximo = numero
        print("El número máximo es", maximo)
        
        return(maximo)
    else: 
        print("La lista está vacía")
        return(None)
    
lst1 = [8, 9, 10, 2, 4, 5]
lst2 = []

encontrar_maximo(lst1)
encontrar_maximo(lst2)

# Ejemplo de función recursiva en python: 
def exponenciacion_version_recursiva(base, exponente): 
    """_summary_

    Args:
        base (_type_): _description_
        exponente (_type_): _description_
    """
    if exponente == 0: 
        return(1)
    
    # Caso Recursivo
    if exponente > 1:
        return(base * exponenciacion_version_recursiva(base, exponente - 1))
   # Caso Base
    elif exponente == 1: 
        return(base)
    
print(exponenciacion_version_recursiva(2, 0))
print(exponenciacion_version_recursiva(2, 4))

# %% 11. Clases

# Importar librerias (módulos) del python standard library
import sys
from pathlib import Path

# Path(__file__) apunta a este script; .parent es la carpeta donde vive.
# Agregamos la subcarpeta 'ejemplo_bancario' al path de búsqueda de módulos.
sys.path.insert(0, str(Path(__file__).resolve().parent / "ejemplo_bancario"))

import clases_ejemplo_bancario as banco

# --- Demo ---
cuenta1 = banco.CuentaBancaria("Ana", 100)
ahorro1 = banco.CuentaAhorros("Luis", 200, tasa_interes=0.05)
estudiante1 = banco.CuentaEstudiante("Mila", 80)

print(banco.CuentaBancaria.info_banco())   # información general del banco
print(cuenta1)
print(ahorro1)
print(estudiante1)
print(ahorro1.aplicar_interes())     # método propio de CuentaAhorros
print(estudiante1.retirar(60))       # rechazado: excede el límite
print(estudiante1.retirar(40))       # permitido: pasa al retirar del padre
print(banco.CuentaBancaria.info_banco())   # el contador refleja las 3 cuentas creadas

# %% 12. Tarea
#def funcion_tarea1