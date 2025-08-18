# Dado un rango de 10 números enteros, iterar desde el primero al último y
# en cada iteración imprimir:
# Valor actual
# Valor anterior
# Valor siguiente
# Suma acumulada
# Nota: se debe usar range() para generar el rango de números

suma_acomulada = 0
for i in range(1,10):
    valor_actual = i
    valor_anterior = i-1
    valor_siguiente = i+1
    suma_acomulada += valor_actual
    print("Valor actual:", valor_actual)
    print("Valor anterior:", valor_anterior)
    print("Valor siguiente:", valor_siguiente)
    print("Suma acumulada:", suma_acomulada)