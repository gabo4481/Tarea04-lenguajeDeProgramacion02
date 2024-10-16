from Diseñador import Diseñador
from Desarrollador import Desarrollador
from Gerente import Gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())
        
empleados = [Diseñador(),Desarrollador(),Gerente()]
mostrar_trabajo(empleados)