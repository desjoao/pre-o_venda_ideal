#Lista 3 - Exercício 3
valor = float(input('Informe o valor de compra do produto: '))
while valor <0:
    print('Valor inválido.')
    valor = float(input('Informe o valor de compra do produto: '))
if valor<20:
    print(f'O valor de venda apropriado para esse produto é de {valor*1.7:.2f} reais')
elif valor<50:
    print(f'O valor de venda apropriado para esse produto é de {valor*1.5:.2f} reais')
elif valor<100:
    print(f'O valor de venda apropriado para esse produto é de {valor*1.4:.2f} reais')
else:
    print(f'O valor de venda apropriado para esse produto é de {valor*1.3:.2f} reais')
