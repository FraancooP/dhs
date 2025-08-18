# Realizar un programa que permita determinar las raíces de un polinomio
# de segundo grado. Se deben contemplar los tres casos posibles


def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c  # Calcula el discriminante

    if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2*a)
        raiz2 = (-b - discriminante**0.5) / (2*a)
        print(f"Las raíces son: {raiz1} y {raiz2}")
    elif discriminante == 0:
        raiz = -b / (2*a)
        print(f"La raíz doble es: {raiz}")
    else:
        print("No hay raíces reales.")
    return

print("Resolviendo la ecuación cuadrática: ax^2 + bx + c = 0\n")
print("Por ejemplo para la funcion 3x^2 + 2x - 1 \n")
print("los valores son: a = 3, b = 2, c = -1\n")
resolver_ecuacion_cuadratica(3, 2, -1)
