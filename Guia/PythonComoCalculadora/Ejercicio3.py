#Diseñar un programa que, dados cinco puntos en el plano, determine cuál
#de los cuatro últimos es más cercano al primero
import math

ejeX = []
ejeY = []
for i in range(5):
    print("Ingrese las coordenadas de los puntos en el plano: \n")
    ejeX.append(float(input("Ingrese la coordenada X del punto: \n")))
    ejeY.append(float(input("Ingrese la coordenada Y del punto: \n")))
    print(f"Coordenadas del punto {i+1}: ({ejeX[i]}, {ejeY[i]})\n")
    print("Ingrese otro punto. \n")
print("Coordenadas ingresadas: \n")
for i in range(5):
    print(f"Punto {i+1}: ({ejeX[i]}, {ejeY[i]})\n")
# Calcula la distancia entre el primer punto y los otros cuatro
distancia = []
for i in range(1, 5):

    #raizcuadrada((Xi - X1)^2 + (Yi - Y1)^2)
    d = ((ejeX[i] - ejeX[0]) ** 2 +(ejeY[i] - ejeY[0]) ** 2 ) ** 0.5
    #Alternativa con math:
    # d = math.dist([ejeX[i], ejeY[i]], [ejeX[0], ejeY[0]])
    distancia.append(d)
    
min_distancia = min(distancia)
indice = distancia.index(min_distancia) + 2  # Sumar 2 para que coincida con el número de punto real
print(f"El punto más cercano al primero es el punto {indice} con una distancia de {min_distancia}")