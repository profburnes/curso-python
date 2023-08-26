import os
os.system('cls')
print('----------------------------------')
nr = int(input('Digite um valor maior que 0: '))
nr += 1
for numero in range(1, nr):
    print(f'Número: {numero}')