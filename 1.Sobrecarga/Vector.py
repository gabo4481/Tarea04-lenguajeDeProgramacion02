class Vector():
    def __init__(self,*args):
        self.valores = args
        
    def calcular_norma(self):
        if len(self.valores) == 2:
            x,y = self.valores
            return (x**2 + y**2)**0.5
        elif len(self.valores) == 3:
            x,y,z = self.valores
            return (x**2 + y**2 + z**2)**0.5
        else:
            raise ValueError("el numero de componentes debe ser 3 o 2...")
        
    