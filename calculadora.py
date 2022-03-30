def calcular(num1, operacao, num2 ):
    if operacao == '+':
       print(num1 + num2)

    if operacao == '-':
       print(num1 - num2)

    if operacao == '*':
       print(num1 * num2)

    if operacao == '/':
       print(num1 / num2)

num1 = int(input('Digite o primeiro número'))

operacao = input('Digite a operação')

num2 = int(input('Digite o segundo número'))

calcular(num1, operacao, num2)
