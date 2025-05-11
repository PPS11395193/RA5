from operaciones import sumar, restar, multiplicar, dividir

def ejecutar_calculadora():
    print("Bienvenido a la Calculadora en Python")
    print("Elige una de las siguientes operaciones:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

    continuar = True
    while continuar:
        try:
            seleccion = int(input("\nSelecciona una opción (1-5): "))
            if seleccion == 5:
                print("Programa finalizado. ¡Gracias por usar la calculadora!")
                continuar = False
                continue

            valor1 = float(input("Introduce el primer número: "))
            valor2 = float(input("Introduce el segundo número: "))

            if seleccion == 1:
                resultado = suma(valor1, valor2)
                print(f"Resultado: {valor1} + {valor2} = {resultado}")
            elif seleccion == 2:
                resultado = resta(valor1, valor2)
                print(f"Resultado: {valor1} - {valor2} = {resultado}")
            elif seleccion == 3:
                resultado = multiplicacion(valor1, valor2)
                print(f"Resultado: {valor1} * {valor2} = {resultado}")
            elif seleccion == 4:
                try:
                    resultado = division(valor1, valor2)
                    print(f"Resultado: {valor1} / {valor2} = {resultado}")
                except ZeroDivisionError as error:
                    print(f"Error: {error}")
            else:
                print("Opción inválida. Elige un número del 1 al 5.")
        except ValueError:
            print("Entrada incorrecta. Asegúrate de ingresar números válidos.")

if __name__ == "__main__":
    ejecutar_calculadora()
