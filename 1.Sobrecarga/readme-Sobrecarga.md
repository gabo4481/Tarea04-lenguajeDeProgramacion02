# SobreCarga (ejecute archivo main.py)

## Descripción del Ejercicio

Este proyecto implementa dos clases en Python: `Vector` y `Transformador`. La clase `Vector` se utiliza para calcular la norma de vectores en 2D y 3D, mientras que la clase `Transformador` permite transformar listas de números mediante la suma de sus elementos o multiplicándolos por un factor.

## Clases

### Clase Vector

La clase `Vector` permite calcular la norma de un vector en función de sus componentes.

#### Métodos

- `calcular_norma(x, y)`: 
  - **Descripción**: Calcula la norma de un vector en 2D.
  - **Parámetros**: 
    - `x`: Componente x del vector.
    - `y`: Componente y del vector.
  - **Retorna**: Norma del vector en 2D.

- `calcular_norma(x, y, z)`:
  - **Descripción**: Calcula la norma de un vector en 3D.
  - **Parámetros**:
    - `x`: Componente x del vector.
    - `y`: Componente y del vector.
    - `z`: Componente z del vector.
  - **Retorna**: Norma del vector en 3D.

#### Ejemplo de uso

```python
from Vector import Vector

# Uso de la clase Vector
norma_2d = Vector(3, 4).calcular_norma()  # Norma en 2D
norma_3d = Vector(1, 2, 2).calcular_norma()  # Norma en 3D

print(f"Norma del vector 2D (3, 4): {norma_2d}")
print(f"Norma del vector 3D (1, 2, 2): {norma_3d}")
```

### Clase Vector

La clase `Transformador` permite transformar listas de números mediante la suma de sus elementos o multiplicándolos por un factor.

#### Métodos

- `transformar(datos)`: 
  - **Descripción**: Calcula la suma de los elementos de una lista.
  - **Parámetros**: 
    - `datos`: lista con elementos a sumar.
  - **Retorna**: la suma de los elementos.

- `transformar(datos,factor)`:
  - **Descripción**: calcula la multiplicacion de cada uno de los elementos de la lista por un factor
  - **Parámetros**:
    - `datos`: lista con elementos.
    - `factor`: factor de multiplicacion para cada elemento.
  - **Retorna**: Una lista con cada uno de sus elementos multiplicados por el factor.
    
```python
from Transformador import Transformador
# Uso de clase Transformador
numeros = [1, 2, 3, 4]
factor = 3
transformador_lista = Transformador(numeros)
transformador_factor = Transformador(numeros,factor)

# Ejemplo de transformación con suma
suma = transformador_lista.transformar()
print(f"Suma de los elementos: {suma}")

# Ejemplo de transformación con factor
transformada = transformador_factor.transformar()
print(f"Lista transformada (multiplicada por {factor}): {transformada}")

```
