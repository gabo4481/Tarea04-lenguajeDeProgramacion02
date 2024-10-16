from EmpleadoMedioTiempo import EmpleadoMedioTiempo
from EmpleadoTiempoCompleto import EmpleadoTiempoCompleto

empleadoTiempoCompleto = EmpleadoTiempoCompleto("Gabriel Mendoza",120)
empleadoMedioTiempo = EmpleadoMedioTiempo("Jesus Mendoza",34,5)

#ejemplo con empleado de medio tiempo
print(empleadoMedioTiempo.mostrar_info())
print(empleadoMedioTiempo.calcular_salario())

print(empleadoTiempoCompleto.mostrar_info())
print(empleadoTiempoCompleto.calcular_salario())