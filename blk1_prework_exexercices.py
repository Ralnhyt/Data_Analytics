# -*- coding: utf-8 -*-
"""blk1_ejercicios(1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dxGDYvkEOsy2-Ry9Tsjjoz-r_AeJjbb9

<!DOCTYPE html>
<html>
<head>
</head>
<body>

<div style="display: flex; justify-content: center; align-items: center; font-family: Arial, sans-serif; margin-top: 20px; margin-bottom: 20px;">
  <div style="text-align: right;">
    <div style="font-size: 24px; font-weight: bold; color: white; margin-left:20px;">PREWORK BOOTCAMP DATA ANALYTICS</div>
    <div style="font-size: 18px; font-weight: bold; margin-left: 20px;">PRIMER BLOQUE: EJERCICIOS</div>
  </div>
  <div style="text-align: right;">
    <img src="https://d1fdloi71mui9q.cloudfront.net/S8HhvUnnRgmjyhySHtWl_ZQMaRWd21TfV5AsU" width="100" height="100">
  </div>
  <div style="text-align: left;">
    <div style="font-size: 24px; font-weight: bold; color: white; margin-left:20px;">UPGRADE-HUB</div>
    <div style="font-size: 18px; font-weight: bold; margin-left: 20px;">coordinacion.data@bootcamp-upgrade.com</div>
  </div>
</div>

</body>
</html>

### Ejercicio 1: Crear variables de diferentes tipos de datos

Crea variables de los siguientes tipos de datos y asígnales valores:

1. Número entero (int)
2. Número decimal (float)
3. Cadena de caracteres (str)
4. Valor booleano (bool)
"""

# 1.
numero_entero = 1
# 2.
numero_decimal = 0,21
# 3.
cafe = "leche azucar"
# 4
te = "azucar" == False
print(te)

"""### Ejercicio 2: Operaciones aritméticas básicas

Dadas las variables `a = 10` y `b = 3`, realiza las siguientes operaciones y guarda los resultados en nuevas variables:

1. Suma
2. Resta
3. Multiplicación
4. División

"""

#1.
a = 10
b = 3
suma= a+b
print(suma)
#2.
resta= a-b
print(resta)
#3.
multiplicacion= a*b
print(multiplicacion)
#4
division= a/b
print(division)

"""### Ejercicio 3: Listas

Crea una lista de números enteros y realiza las siguientes operaciones:

1. Añade un nuevo elemento al final de la lista.
2. Inserta un elemento en una posición específica de la lista.
3. Elimina un elemento de la lista.
4. Obtiene la longitud de la lista.
5. Accede a un elemento específico de la lista utilizando su índice.
"""

lista= [1,2,3,4,5]
#1.
lista.append(6)
print(lista)
#2.
lista.insert(2,17)
print(lista)
#3.
lista.remove(17)
print(lista)
#4.
lend=lista
print(lista)
#5.
lista= [5]
print(lista)

"""### Ejercicio 4: Tuplas

Crea una tupla con diferentes tipos de datos (int, float, str, bool) y accede a sus elementos utilizando índices.
"""

#Ingredientes arroz con leche
ingredientes =(1,"kg arroz,",0.3,"kg de azucar","1l de leche","canela","limon", "naranja",True)
print(ingredientes)
citricos = ingredientes[6:8]
print(citricos)

"""### Ejercicio 5: Diccionarios

Crea un diccionario con al menos tres pares clave-valor y realiza las siguientes operaciones:

1. Accede al valor de una clave específica.
2. Cambia el valor de una clave específica.
3. Agrega un nuevo par clave-valor al diccionario.
4. Elimina un par clave-valor del diccionario.
"""

#Lugares
lugares = {"ciudad":"londres", "playas":"playa del ingles","caminos":"camino de santiago"}
print(lugares)
#1
vacaciones = lugares["ciudad"]
print(vacaciones)
#2
lugares["playas"]= "playa de sitges"
print(lugares)
#3
lugares["heladeria"] = "jijonenca"
print(lugares)
#4
del lugares["caminos"]
print(lugares)

"""### Ejercicio 6: Operadores de comparación

Dadas las variables `x = 5` e `y = 8`, utiliza operadores de comparación (==, !=, >, <, >=, <=) para comparar sus valores y guarda los resultados en variables booleanas.
"""

x = 5
y= 8
#¿Son iguales?
iguales= x == y
print(iguales)
#¿Son diferentes?
diferentes= x != y
print(diferentes)
#¿Es mayor que?
mayor = x > y
print(mayor)
#¿Es menor que?
menor = x < y
print(menor)
#¿Es mayor o igual que?
igual_o_mayor = x >= y
print(igual_o_mayor)
#¿Es menor o igual que?
igual_o_menor = x <= y
print(igual_o_menor)

"""### Ejercicio 7: Conversión de tipos de datos

Practica la conversión de tipos de datos con las siguientes operaciones:

1. Convierte un número entero a float.
2. Convierte un número float a entero.
3. Convierte un número a cadena.
4. Convierte una cadena a número (si la cadena contiene un valor numérico válido).
"""

#1
entero = 3
conversion = float(entero)
print(conversion)
#2
flotante = 3.1416
conversion = int(flotante)
print(conversion)
#3
numeros = 1234567
conversion = str(numeros)
print(numeros)
#4
cadenas = "1"
conversion = int(cadenas)
print(conversion)