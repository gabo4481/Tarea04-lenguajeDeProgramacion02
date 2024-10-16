from Empleado import Empleado

class EmpleadoMedioTiempo(Empleado):
    def __init__(self,nombre, horas_trabajadas,pago_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
        
    def calcular_salario(self):
        return f"salario: {self.horas_trabajadas * self.pago_por_hora}$"    
    
    def mostrar_info(self):
        return  f"Empleado Medio Tiempo: {self.nombre}, Horas Trabajadas: {self.horas_trabajadas}, Pago por hora: {self.pago_por_hora}$"