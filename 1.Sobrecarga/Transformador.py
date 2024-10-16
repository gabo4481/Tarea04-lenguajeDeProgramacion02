class Transformador():
    def __init__(self,*args):
        self.datos = args
        
    def transformar(self):
        if len(self.datos) == 1:
            lista = self.datos[0]
            acumulador = 0
            for valor in lista:
                acumulador = acumulador + valor
            return acumulador
        elif len(self.datos) == 2:
            lista,factor = self.datos
            transformado = []
            for dato in lista:
                numero = dato * factor
                transformado.append(numero)
            return transformado
        else:
            raise ValueError("el numero de componentes debe ser 1 o 2")
        
            
        