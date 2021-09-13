# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.
import time
valor_emprestimo = float(input('Qual o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = int(input('Irá pagar em quantos anos? '))
juros = float(input('Qual o valor dos juros por ano? '))
prestacao = valor_emprestimo / (anos * 12)
juros_mes = juros/12
print('\nAguarde...')
time.sleep(2)
print('\nCalculando taxas...')
time.sleep(1)
print('\nAnalisando proposta...')
time.sleep(5)
if prestacao + (prestacao * juros_mes) <= (salario * 0.3):
    print('Empréstimo de R${:.2f} foi APROVADO!. \n\nOs juros aplicados em cada parcela é de {:.2f}% \n\nO valor de cada parcela é de R${:.2f}.'.format(
        valor_emprestimo, juros_mes, (prestacao + (prestacao * juros_mes))))
else:
    print('Empréstimo NEGADO!')
print('')
