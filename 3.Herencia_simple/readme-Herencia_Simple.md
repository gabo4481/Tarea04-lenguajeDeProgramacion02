# Herencia Simple (ejecute archivo main.py)

## Descripción del Ejercicio

Este proyecto implementa dos clases en Python utilizando herencia simple: `Vehiculo` y `Carro`. La clase `Carro` hereda de la clase base `Vehiculo` e implementa los métodos `arrancar()` y `parar()` de manera específica.

## Clases

### Clase Vehiculo

La clase `Vehiculo` sirve como clase base y define los métodos `arrancar()` y `parar()`. Estas funciones son genéricas y pueden ser sobrescritas por clases derivadas.

#### Métodos

- `arrancar()`: 
  - **Descripción**: Indica que el vehículo está arrancando.
  - **Parámetros**: Ninguno.
  - **Retorna**: Una cadena de texto indicando que el vehículo está arrancando.

- `parar()`:
  - **Descripción**: Indica que el vehículo se ha detenido.
  - **Parámetros**: Ninguno.
  - **Retorna**: Una cadena de texto indicando que el vehículo se ha detenido.

#### Ejemplo de uso

```python
from Vehiculo import Vehiculo

# Uso de la clase Vehiculo
mi_vehiculo = Vehiculo()
print(mi_vehiculo.arrancar())  # El vehiculo está arrancando
print(mi_vehiculo.parar())     # El vehiculo se ha detenido
