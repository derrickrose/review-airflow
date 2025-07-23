# module 3

## 🔹 **Prioridades de los operadores**

| Precedencia | Operadores                                       | Descripción                                       |
|:-----------:|:-------------------------------------------------|:--------------------------------------------------|
|  1 (Mayor)  | `~`, `+`, `-`                                    | Unarios                                           |
|      2      | `**`                                             | Exponenciación                                    |
|      3      | `*`, `/`, `//`, `%`                              | Multiplicación, división, división entera, módulo |
|      4      | `+`, `-`                                         | Binarios (suma, resta)                            |
|      5      | `<<`, `>>`                                       | Desplazamiento de bits                            |
|      6      | `<`, `<=`, `>`, `>=`                             | Comparación                                       |
|      7      | `==`, `!=`                                       | Igualdad                                          |
|      8      | `&`                                              | AND bit a bit                                     |
|      9      | `                                                | `                                                 | OR bit a bit |
| 10 (Menor)  | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, ` | =`, `>>=`, `<<=`                                  | Asignación |

| Precedencia | Operadores                                       | Descripción                                       |
|:-----------:|:-------------------------------------------------|:--------------------------------------------------|
|  1 (Mayor)  | `~`, `+`, `-`                                    | Unarios                                           |
|      2      | `**`                                             | Exponenciación                                    |
|      3      | `*`, `/`, `//`, `%`                              | Multiplicación, división, división entera, módulo |
|      4      | `+`, `-`                                         | Binarios (suma, resta)                            |
|      5      | `<<`, `>>`                                       | Desplazamiento de bits                            |
|      6      | `<`, `<=`, `>`, `>=`                             | Comparación                                       |
|      7      | `==`, `!=`                                       | Igualdad                                          |
|      8      | `&`                                              | AND bit a bit                                     |
|      9      | `                                                | `                                                 | OR bit a bit |
|     10      | `^`                                              | XOR bit a bit                                     |
|     11      | `and`                                            | AND lógico                                        |
|     12      | `or`                                             | OR lógico                                         |
| 13 (Menor)  | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, ` | =`, `>>=`, `<<=`                                  | Asignación |

### Asociatividad

- **Izquierda a derecha**: La mayoría de operadores
- **Derecha a izquierda**: Exponenciación (`**`) y asignación

## 🔹 **Operadores de Comparación**

- Operador de igualdad `==` vs. operador de asignación `=`
- Operador de desigualdad `!=`
- Operadores relacionales: `>`, `>=`, `<`, `<=`
- Comparaciones y valores de retorno (True/False)

## 🔹 **Estructuras de Control Condicional**

- Sentencia `if` básica
- Sentencia `if-else`
- Sentencia `elif` (cascada)
- Anidamiento de condicionales (nested)
- Indentación y bloques de código

## 🔹 **Evaluación de Valores Booleanos**

- Valores que se evalúan como `False` (cero, cadenas vacías)
- Valores que se evalúan como `True` (cualquier valor no cero)
- Conversión implícita a booleanos

## 🔹 **Bucles (Ciclos)**

- **Bucle `while`**: ejecución condicional repetitiva
- **Bucle `for`**: iteración con contador automático
- Función `range()` y sus parámetros
- Cuerpo del bucle y control de iteraciones

## 🔹 **Control de Flujo en Bucles**

- Instrucción `break`: salir del bucle inmediatamente
- Instrucción `continue`: saltar al siguiente ciclo
- Cláusula `else` en bucles `while` y `for`
- Bucles infinitos y su manejo

## 🔹 **Operadores Lógicos**

- **Conjunción** (`and`): ambas condiciones verdaderas
- **Disyunción** (`or`): al menos una condición verdadera
- **Negación** (`not`): inversión lógica
- Leyes de De Morgan
- Precedencia de operadores lógicos

## 🔹 **Operadores de Bit (Bitwise)**

- **AND bit a bit** (`&`): conjunción por bits
- **OR bit a bit** (`|`): disyunción por bits
- **XOR bit a bit** (`^`): exclusiva por bits
- **NOT bit a bit** (`~`): negación por bits
- Operadores de asignación aumentada (`&=`, `|=`, `^=`)

## 🔹 **Desplazamiento de Bits**

- Desplazamiento a la izquierda (`<<`): multiplicación por potencias de 2
- Desplazamiento a la derecha (`>>`): división por potencias de 2
- Manipulación de bits individuales con máscaras

## 🔹 **Manipulación de Bits Individuales**

- Creación de máscaras de bits
- Verificar el valor de un bit específico
- Poner un bit a cero (reset)
- Poner un bit a uno (set)
- Alternar un bit (toggle)

## 🔹 **Listas - Conceptos Básicos**

- Declaración de listas con corchetes `[]`
- Indexación (acceso por índices)
- Índices negativos
- Función `len()` para obtener longitud
- Listas heterogéneas (diferentes tipos de datos)

## 🔹 **Operaciones con Listas**

- **Agregar elementos**: `append()`, `insert()`
- **Eliminar elementos**: `del`
- **Modificar elementos**: asignación por índice
- Iteración a través de listas

## 🔹 **Métodos de Listas**

- `sort()`: ordenamiento de elementos
- `reverse()`: inversión del orden
- Diferencia entre funciones y métodos

## 🔹 **Algoritmos con Listas**

- **Ordenamiento burbuja**: implementación manual
- Intercambio de elementos
- Búsqueda del elemento mayor
- Eliminación de elementos duplicados
- Reversión manual de listas

## 🔹 **Rebanadas (Slicing)**

- Sintaxis de rebanadas `[start:end]`
- Índices negativos en rebanadas
- Omisión de parámetros (valores por defecto)
- Copia de listas con rebanadas `[:]`
- Eliminación de rebanadas con `del`

## 🔹 **Referencias vs. Copias**

- Diferencia entre asignación de referencia y copia
- Comportamiento de listas como referencias
- Creación de copias independientes

## 🔹 **Operadores de Pertenencia**

- Operador `in`: verificar si elemento existe en lista
- Operador `not in`: verificar si elemento no existe
- Búsqueda de elementos en listas

## 🔹 **Listas Avanzadas**

- **Comprensión de listas**: creación dinámica `[x for x in range()]`
- **Listas bidimensionales**: matrices y tableros
- **Listas tridimensionales**: estructuras complejas
- Anidamiento y acceso a elementos multidimensionales

## 🔹 **Tabla de Precedencia de Operadores**

- Orden de evaluación desde operadores unarios hasta asignación
- Precedencia entre operadores lógicos, de comparación y de bits



