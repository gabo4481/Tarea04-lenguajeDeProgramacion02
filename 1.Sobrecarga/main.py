from Transformador import Transformador
from Vector import Vector



# Uso de clase Vector
norma_2d = Vector(3, 4).calcular_norma()  # Norma en 2D
norma_3d = Vector(1, 2, 2).calcular_norma()  # Norma en 3D

# Ejemplo de calculo de norma
print(f"Norma del vector 2D (3, 4): {norma_2d}")
print(f"Norma del vector 3D (1, 2, 2): {norma_3d}")

# Uso de clase Transformador
numeros = [1, 2, 3, 4]
factor = 3
transformador_lista = Transformador(numeros)
transformador_factor = Transformador(numeros,factor)

# Ejemplo de transformación con suma
suma = transformador_lista.transformar()
print(f"Suma de los elementos: {suma}")

# Ejemplo de transformación con factor
transformada = transformador_factor.transformar()
print(f"Lista transformada (multiplicada por {factor}): {transformada}")

