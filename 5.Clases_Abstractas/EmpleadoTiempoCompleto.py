from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self,nombre,salario_mensual,):
        self.nombre = nombre
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        return f"Salario: {self.salario_mensual}$"
    
    def mostrar_info(self):
        return f"Empleado Tiempo Completo: {self.nombre}, Salario: {self.salario_mensual}$"