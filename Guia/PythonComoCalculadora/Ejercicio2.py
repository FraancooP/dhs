#Realizar un programa que calcule el desglose mínimo en billetes y monedas
#de una cantidad exacta de pesos. Hay billetes de $1000, $500, $200, $100 y
#$50 y monedas de $10, $5 y $2 y $1. El desglose se realiza del más grande
#al más pequeño. . El desglose se realiza del más grande al más pequeño


# Solicita al usuario que ingrese el monto total en pesos y lo convierte a entero
montoTotal = int(input("Ingresa el monto total en pesos: "))


# Listas con las denominaciones de billetes y monedas disponibles
billetes = [1000, 500, 200, 100, 50]
monedas = [10, 5, 2, 1]


# Recorre cada billete de mayor a menor
for billete in billetes:
    # Calcula cuántos billetes de este valor entran en el monto actual
    #1789: 1era 1789/1000 resto = 789 billete de 1000 1
    #1789: segunda 789/500 resto = 289 billetes de 500 1
    #1789: tercera 289/200 resto = 89 billete de 200 1
    #1789: cuarta 89/100 resto = 89 billete de 100 0
    #...y asi sucesivamente
    cantidad = montoTotal // billete  # División entera: cuántas veces cabe el billete en el monto
    if cantidad > 0:
        print(f"Billetes de ${billete}: {cantidad}")
    # Actualiza el monto, quitando el valor de los billetes usados
    montoTotal %= billete  # Operador módulo: lo que sobra después de usar esos billetes
    #El operador modulo devuelve el resto de una divicion entera
    #Ejemplo
    # 17 % 5 = 2, porque 17 dividido 5 es 3 (5×3=15) y sobran 2.
    #789 % 500 = 289, porque 789 dividido 500 es 1 (500×1=500) y sobran 289
    print(f"Monto total luego de usar el operador modulo: /n",montoTotal)


# Repite el proceso para las monedas
for moneda in monedas:
    # Calcula cuántas monedas de este valor entran en el monto actual
    cantidad = montoTotal // moneda  # División entera
    if cantidad > 0:
        print(f"Monedas de ${moneda}: {cantidad}")
    # Actualiza el monto, quitando el valor de las monedas usadas
    montoTotal %= moneda  # Operador módulo
    print(f"Monto total luego de usar el operador modulo: /n",montoTotal)
