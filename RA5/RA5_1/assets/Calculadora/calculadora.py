import sys

class Calculadora:
    def multiplicar(self, a, b):
        return a * b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py num1 num2")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        calc = Calculadora()
        resultado = calc.multiplicar(num1, num2)
        print("Resultado:", resultado)
    except ValueError:
        print("Introduce dos números válidos.")
        sys.exit(1)