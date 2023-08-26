import os
os.system('cls')
print('------------------------------------')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if (idade >= 18):
    print('Pode entrar na Festa dos Enxutos')
    print(f'Parabéns {nome}')
else:
    print('Pode ir para a festa da Xuxa')

print('-------------------------------------')