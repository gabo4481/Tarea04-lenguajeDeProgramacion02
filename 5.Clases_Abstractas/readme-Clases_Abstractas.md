# Clases Abstractas

## Descripción del Ejercicio

Este proyecto implementa una jerarquía de clases utilizando clases abstractas en Python para modelar empleados de tiempo completo y medio tiempo. La clase abstracta `Empleado` define los métodos abstractos `calcular_salario()` y `mostrar_info()`, los cuales son implementados por sus subclases `EmpleadoTiempoCompleto` y `EmpleadoMedioTiempo`.

## Clases

### Clase Empleado (Abstracta)

La clase abstracta `Empleado` es la clase base de la jerarquía, y define los métodos que deben ser implementados por las subclases.

#### Métodos

- `calcular_salario()`: 
  - **Descripción**: Método abstracto que calcula el salario del empleado.
  - **Retorna**: Salario del empleado.

- `mostrar_info()`: 
  - **Descripción**: Método abstracto que muestra la información del empleado.
  - **Retorna**: Información del empleado.

### Clase EmpleadoMedioTiempo

La clase `EmpleadoMedioTiempo` hereda de `Empleado` e implementa los métodos abstractos para un empleado de medio tiempo.

#### Atributos

- `nombre`: Nombre del empleado.
- `horas_trabajadas`: Cantidad de horas trabajadas por el empleado.
- `pago_por_hora`: Monto que recibe el empleado por hora trabajada.

#### Métodos

- `calcular_salario()`:
  - **Descripción**: Calcula el salario del empleado en base a las horas trabajadas y el pago por hora.
  - **Retorna**: Salario del empleado calculado como `horas_trabajadas * pago_por_hora`.

- `mostrar_info()`:
  - **Descripción**: Muestra la información del empleado de medio tiempo.
  - **Retorna**: Detalles del empleado en formato string.

### Clase EmpleadoTiempoCompleto

La clase `EmpleadoTiempoCompleto` hereda de `Empleado` e implementa los métodos abstractos para un empleado de medio tiempo.

#### Atributos

- `nombre`: Nombre del empleado.
- `salario_mensual`: Cantidad de salario mensual del empleado.


#### Métodos

- `calcular_salario()`:
  - **Descripción**: Muestra el salario mensual del empleado.
  - **Retorna**: Salario mensual del empleado en string.

- `mostrar_info()`:
  - **Descripción**: Muestra la información del empleado de tiempo completo.
  - **Retorna**: Detalles del empleado en formato string.

#### Ejemplo de uso

```python
from EmpleadoMedioTiempo import EmpleadoMedioTiempo
from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto

empleadoTiempoCompleto = EmpleadoTiempoCompleto("Gabriel Mendoza",120)
empleadoMedioTiempo = EmpleadoMedioTiempo("Jesus Mendoza",34,5)

#ejemplo con empleado de medio tiempo
print(empleadoMedioTiempo.mostrar_info())
print(empleadoMedioTiempo.calcular_salario())

print(empleadoTiempoCompleto.mostrar_info())
print(empleadoTiempoCompleto.calcular_salario())
