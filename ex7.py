import os
os.system('cls')
print('------------------------------')
def calcular(valor, parcelas):
    parcela = valor / parcelas
    print('Valor da parcela sem juros: {0:.2f}' . format(parcela))
    total = 0
    for p in range (1, parcelas + 1):
        if (p > 1):
            parcela = parcela + parcela * 1.99/100
        print('Parcela {0} de R$ {1:.2f}' . format(p, parcela))
        total = total + parcela
    print('O valor total é de R$ {0:.2f}'.format(total))
    totalcomjuros = total - valor
    print('O juros é de R$ {0:.2f}'.format(totalcomjuros))
    print('--------------------------------')

valor = float(input('Digite o valor: '))
parcelas = int(input('Digite o número de parcelas: '))
calcular(valor, parcelas)