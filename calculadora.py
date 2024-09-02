while True:
  operacao = input('Digite a operação que você quer fazer (+,-,*,/) ou digite \'s\' para sair')
  if operacao == 's' or operacao == 'S':
    break
  elif operacao == '+' or operacao =='-' or operacao =='*' or operacao =='/':
    num1 = int(input('Digite o primeiro número:'))
    num2 = int(input('Digite o segundo número:'))
  else:
    print('Operação inválida')
  if operacao == '+':
    total = num1 + num2
    print('Resultado:',total)
  elif operacao == '-':
    total = num1 - num2
    print('Resultado:',total)
  elif operacao == '*':
    total = num1 * num2
    print('Resultado:',total)
  elif operacao =='/':
    total = num1 / num2
    print('Resultado:',total)