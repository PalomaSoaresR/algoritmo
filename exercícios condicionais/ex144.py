saldomedio = float(input('\nDigite o saldo médio: '))
if saldomedio < 501:
    credito = 0
else: 
    if saldomedio < 1001:
        credito = saldomedio * 0.3
    else: 
        if saldomedio < 3001:
            credito = saldomedio * 0.4
        else:
            credito = saldomedio * 0.5
if credito == 0:
     print ('\nComo seu saldo era de: ', saldomedio , '\nVocê não terá nenhum crédito')
else:
    print ('\nComo seu saldo era de: ', saldomedio ,'\nSeu crédito será de: ' , credito)
    print('')