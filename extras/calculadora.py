import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def exponenciacao(a, b):
    return a ** b

def raiz_quadrada(a):
    return math.sqrt(a)

print("Calculadora Científica")
print("----------------------")
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponenciação")
print("6 - Raiz Quadrada")

opcao = input("Digite o número da operação desejada: ")

if opcao in ['1', '2', '3', '4', '5']:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    resultado = soma(num1, num2)
    print("Resultado: ", resultado)
elif opcao == '2':
    resultado = subtracao(num1, num2)
    print("Resultado: ", resultado)
elif opcao == '3':
    resultado = multiplicacao(num1, num2)
    print("Resultado: ", resultado)
elif opcao == '4':
    resultado = divisao(num1, num2)
    print("Resultado: ", resultado)
elif opcao == '5':
    resultado = exponenciacao(num1, num2)
    print("Resultado: ", resultado)
elif opcao == '6':
    resultado = raiz_quadrada(num1)
    print("Resultado: ", resultado)
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")
