import os
os.system('cls')
print('--------------------------------------')
nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
print(f'O {nome} ganha de salário {salario}')
print('O {0} ganha de salário {1}' . format(nome, salario))
# calculos dos descontos do breno
# se o salario >= 5000 - desconto de 27%
# se o salario for menor - desconto será de 20%
if (salario >= 5000):
    desconto = salario * 27 / 100
    print('O desconto do salário do {0} é de {1}' . format(nome, desconto))
else:
    desconto = salario * 20 / 100
    print('O desconto do salário do {0} é de {1} ' . format(nome, desconto))