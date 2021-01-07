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

def soma(x, y):
    return x + y

def quadrado(x):
    return x ** 2

def somar():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    print(f'O resultado da soma de {num1} e {num2} é {soma(num1, num2)}.')

def imc():
    peso = int(input('Peso em kg: '))
    altura = float(input('Altura em metros: '))
    print(f'O IMC é {round(peso / quadrado(altura), 2)}.')

if opcao == 1:
    somar()
elif opcao == 2:
    imc()
else:
    print('Opção inválida')

print('')
