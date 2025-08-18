#Dado dos números enteros imprimir por pantalla el producto de los mismos. 
# Si el producto es más grande que 10000, imprimir su suma
num1 = 0
num2 = 0
producto = 0

num1 = int(input("Ingrese el primer numero: \n"))
num2 = int(input("Ingrese el segundo numero: \n"))
producto = num1 * num2
if producto > 10000:
    print("La suma de los numeros es: ", num1 + num2)
else:
    print("El producto de los numeros es: ", producto)
