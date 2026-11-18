operacao = input('Insira qual operação deseja realizar (+; -; *; /; **; %): ')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
if operacao == '+':
    print('A soma é: {}'.format(num1 + num2))
elif operacao == '-':
    print('A subtração é: {}'.format(num1 - num2))
elif operacao == '*':
    print('A multiplicação é: {}'.format(num1 * num2)) 
elif operacao == '/':
    if num2 == 0:
        print('Não é possível dividir por zero!')
    else:
        print('A divisão é: {}'.format(num1 / num2))
elif operacao == '**':
    print('A potência é: {}'.format(num1 ** num2))
elif operacao == '%':
    print('O resto da divisão é: {}'.format(num1 % num2))
else:
    print('Esta operação não é compatível!')
