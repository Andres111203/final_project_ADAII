# Proyecto 2 - Optimización

## Descripción

Este proyecto busca determinar una ubicación adecuada para un concierto dentro de una región representada por un cuadrado de tamaño `N x N`, considerando un conjunto de ciudades ubicadas en coordenadas enteras.

La solución genera automáticamente un modelo en MiniZinc a partir de una entrada proporcionada por el usuario. El modelo puede copiarse y ejecutarse directamente en MiniZinc para obtener la ubicación óptima del concierto.

## Requisitos

* Python 3.10 o superior
* Biblioteca Tkinter (incluida normalmente con Python)

## Estructura del Proyecto

```text
proyecto_optimizacion/
│
├── main.py
├── parser.py
├── minizinc_generator.py
└── README.md
```

## Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

## Funcionamiento

1. Ingresar los datos en el área de texto de entrada.
2. Presionar el botón **Generar Modelo MiniZinc**.
3. Copiar el código generado.
4. Abrir MiniZinc.
5. Pegar el modelo generado.
6. Ejecutar el modelo para obtener la solución.

## Formato de Entrada

La entrada debe seguir la siguiente estructura:

```text
N
M
NombreCiudad X Y
NombreCiudad X Y
...
```

Donde:

* `N` representa el tamaño del cuadrado.
* `M` representa el número de ciudades.
* Cada línea posterior contiene:

  * Nombre de la ciudad.
  * Coordenada X.
  * Coordenada Y.

## Ejemplo de Entrada

```text
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
Rio Frio 1 2
```

## Modelo Utilizado

La distancia entre el concierto y cada ciudad se calcula utilizando la distancia Manhattan:

```text
d = |x1 - x2| + |y1 - y2|
```

El modelo utiliza una estrategia de optimización de dos niveles:

1. Minimizar la distancia máxima entre el concierto y cualquier ciudad.
2. Minimizar la diferencia entre la ciudad más cercana y la más lejana.

Esto busca garantizar una distribución equitativa de las distancias y evitar favorecer una ciudad sobre las demás.

## Restricciones

* El concierto debe ubicarse dentro del cuadrado `N x N`.
* El concierto no puede ubicarse exactamente en una ciudad.
* Todas las coordenadas son enteras.
* Se utiliza distancia Manhattan para medir desplazamientos.

## Autor(es)
Andrés Eduarodo Narváez Cañas
David Mármol
Proyecto desarrollado para la asignatura Análisis y Diseño de Algoritmos.
