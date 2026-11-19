cores = {'Limpa': '\033[m',
         'Negrito': '\033[1m',
         'Vermelho': '\033[1;31m'}

operacao = input('Insira qual operação deseja realizar (+; -; *; /; **; %): ')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

if operacao == '+':
    print('Resultado da soma é: {}{}{}'.format(cores['Negrito'], num1 + num2, cores['Limpa']))
elif operacao == '-':
    print('Resultado da subtração é: {}{}{}'.format(cores['Negrito'], num1 - num2, cores['Limpa']))
elif operacao == '*':
    print('Resultado da multiplicação é: {}{}{}'.format(cores['Negrito'], num1 * num2, cores['Limpa'])) 
elif operacao == '/':
    if num2 == 0:
        print('{}Não é possível dividir por zero!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('Resultado da divisão é: {}{}{}'.format(cores['Negrito'], num1 / num2, cores['Limpa']))
elif operacao == '**':
    if num1 == 0 and num2 < 0: 
        print('{}O número zero não pode ser elevado a um número negativo!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('Resultado da potência é: {}{}{}'.format(cores['Negrito'], num1 ** num2, cores['Limpa']))
elif operacao == '%':
    if num2 == 0:
        print('{}Não é possível dividir por zero!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('O resto da divisão é: {}{}{}'.format(cores['Negrito'], num1 % num2, cores['Limpa']))
else:
    print('{}Esta operação não é compatível!{}'.format(cores['Vermelho'], cores['Limpa']))
