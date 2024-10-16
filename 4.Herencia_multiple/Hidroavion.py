from Volador import Volador
from Navegable import Navegable

class Hidroavion(Volador,Navegable):
    def navegar(self):
        return "El hidroavión está navegando."
    
    def volar(self):
        return "El hidroavión está volando."