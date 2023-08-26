#importar um pacote SO
import os
#limpar a tela
os.system('cls')
print('---------------------------------')
nome = input('Digite o seu nome: ')
print('Você digitou ' + nome)
idade = input('Digite sua idade: ')
print(f'Sua idade é {idade}')
print('O ' + nome + ' tem a idade de ' + idade)
print(f'O {nome} tem a idade de {idade}')
dias = 365 * int(idade)
print(f'O {nome} viveu {dias} dias')
