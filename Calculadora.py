import math
cores = {'Limpa': '\033[m',
         'Vermelho': '\033[1;31m',
         'Verde': '\033[1;32m'}

operacao = input('Insira qual operação deseja realizar (+; -; *; /; r; %; ^; **): ')
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

# Adição
if operacao == '+':
    print('{} + {} = {}{}{}'.format(num1, num2, cores['Verde'], num1 + num2, cores['Limpa']))
# Subtração
elif operacao == '-':
    print('{} - {} = {}{}{}'.format(num1, num2, cores['Verde'], num1 - num2, cores['Limpa']))
# Multiplicação
elif operacao == '*':
    print('{} * {} = {}{}{}'.format(num1, num2, cores['Verde'], num1 * num2, cores['Limpa']))
# Divisão
elif operacao == '/':
    if num2 == 0:
        print('{}Não é possível dividir por zero!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('{} / {} = {}{}{}'.format(num1, num2, cores['Verde'], num1 / num2, cores['Limpa']))
# Potência
elif operacao == '^' or operacao == '**':
    if num1 == 0 and num2 < 0:
        print('{}O número zero não pode ser elevado a um número negativo!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('{} ^ {} = {}{}{}'.format(num1, num2, cores['Verde'], math.pow(num1, num2), cores['Limpa']))
# Resto da Divisão
elif operacao == '%':
    if num2 == 0:
        print('{}Não é possível dividir por zero!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('{} % {} = {}{}{}'.format(num1, num2, cores['Verde'], num1 % num2, cores['Limpa']))
# Raiz Quadrada
elif operacao == 'r':
    if num1 < 0:
        print('{}Não existe raiz quadrada de número negativo!{}'.format(cores['Vermelho'], cores['Limpa']))
    else:
        print('Raiz de: {} = {}{}{}'.format(num1, cores['Verde'], math.sqrt(num1), cores['Limpa']))
else:
    print('{}Esta operação não é compatível!{}'.format(cores['Vermelho'], cores['Limpa']))
