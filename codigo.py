'''
author: Iuri Freire
e-mail: iuricostafreire at gmail dot com
local date : 2021-01-06
local time : 10:25
'''

print('''
Selecione uma opção do menu:

Menu:
1. Somar
2. Cálcular IMC
''')

opcao = int(input('Opção: '))

if opcao == 1:
	num1 = int(input('Primeiro número: '))
	num2 = int(input('Segundo número: '))
	print(f'O resultado da soma de {num1} e {num2} é {num1 + num2}.')
elif opcao == 2:
	peso = int(input('Peso em kg: '))
	altura = float(input('Altura em metros: '))
	print(f'O IMC é {round(peso / altura ** 2, 2)}.')
else:
	print('Opção inválida')

print('')