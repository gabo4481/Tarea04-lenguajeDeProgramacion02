# Polimorfismo

## Descripción del Ejercicio

Este proyecto implementa una jerarquía de clases en Python que utiliza el concepto de polimorfismo. La clase base `Empleado` tiene un método `trabajar()` que es sobreescrito por las clases derivadas `Desarrollador`, `Diseñador` y `Gerente`, cada una de las cuales proporciona una implementación específica del método.

## Clases

### Clase Empleado

La clase `Empleado` es la clase base que define un método `trabajar()` que devuelve una cadena vacía.

#### Métodos

- `trabajar()`: 
  - **Descripción**: Método que se espera que sea sobreescrito por las clases derivadas.
  - **Retorna**: Una cadena vacía.

### Clase Desarrollador

La clase `Desarrollador` hereda de `Empleado` y sobreescribe el método `trabajar()`.

#### Métodos

- `trabajar()`:
  - **Descripción**: Devuelve la cadena que representa la actividad de un desarrollador.
  - **Retorna**: `"Escribiendo código."`

### Clase Diseñador

La clase `Diseñador` hereda de `Empleado` y sobreescribe el método `trabajar()`.

#### Métodos

- `trabajar()`:
  - **Descripción**: Devuelve la cadena que representa la actividad de un diseñador.
  - **Retorna**: `"Creando diseño gráfico."`

### Clase Gerente

La clase `Gerente` hereda de `Empleado` y sobreescribe el método `trabajar()`.

#### Métodos

- `trabajar()`:
  - **Descripción**: Devuelve la cadena que representa la actividad de un gerente.
  - **Retorna**: `"Gestionando el equipo."`

#### Ejemplo de uso

```python
from Empleado import Empleado
from Desarrollador import Desarrollador
from Diseñador import Diseñador
from Gerente import Gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())
        
empleados = [Diseñador(), Desarrollador(), Gerente()]
mostrar_trabajo(empleados)
