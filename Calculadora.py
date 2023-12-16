print("=========CALCULADORA==========")
while True:
    num1 = float(input('Digite o primeiro numero: '))
    operacao = input('Qual operação deseja realizar? (*, /, +, -)')
    num2 = float(input('Digite o segundo numero: '))
    if operacao == '*':
        print(num1 * num2)
    elif operacao == '/':
        print(num1 / num2)
    elif operacao == '-':
        print(num1 - num2)
    elif operacao == '+':
        print(num1 + num2)
    else:
        print('Entrada inválida. Por favor digite uma das opções acima.')
    break
