# Herencia Múltiple (ejecute archivo main.py)

## Descripción del Ejercicio

Este proyecto implementa el concepto de herencia múltiple en Python a través de las clases `Volador`, `Navegable` y `Hidroavion`. La clase `Hidroavion` hereda de las clases `Volador` y `Navegable`, permitiendo que el hidroavión pueda tanto navegar en el agua como volar en el aire.

## Clases

### Clase Volador

La clase `Volador` permite simular un comportamiento de vuelo.

#### Métodos

- `volar()`: 
  - **Descripción**: Devuelve un mensaje indicando que el objeto está volando.
  - **Retorna**: "Volando en el aire."

### Clase Navegable

La clase `Navegable` permite simular un comportamiento de navegar.

#### Métodos

- `navegar()`: 
  - **Descripción**: Devuelve un mensaje indicando que el objeto está navegando.
  - **Retorna**: "Navegando en el agua."
 
### Clase Hidroavion

La clase `Hidroavion` permite simular un comportamiento de un hidroavion.

#### Métodos

- `navegar()`: 
  - **Descripción**: Devuelve un mensaje indicando que el hidroavion está navegando.
  - **Retorna**: "El hidroavión está navegando."
 
#### Métodos

- `volar()`: 
  - **Descripción**: Devuelve un mensaje indicando que el hidroavion está volando.
  - **Retorna**: "El hidroavión está volando."


#### Ejemplo de uso

```python
from Hidroavion import Hidroavion

mi_hidroavion = Hidroavion()
print(mi_hidroavion.navegar())
print(mi_hidroavion.volar())
