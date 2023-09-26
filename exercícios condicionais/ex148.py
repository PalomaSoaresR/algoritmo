regiao = ['1 Região Norte', '2 Região Nordeste', '3 Região Centro-Oeste','4 Região Sul']
for Região in regiao:
    print(Região)
op = int(input('\nDigite o número da região: '))
ida = ['1 Ida', '2 Ida e volta']
for Ida in ida:
    print(Ida)
iv = int(input('\nDigite o número do tipo de passagem: '))
if op == 1:
   if iv == 1:
       print ('\nO valor da passagem ida é R$500,00')
   elif iv == 2:
    print ('\nO valor da passagem de ida e volta é R$950,00')
elif op == 2:
    if iv == 1:
        print('\nO valor da passagem de ida é R$350,00')
    elif iv == 2:
        print('\nO valor da passagem de ida e volta é R$650,00')
elif op == 3:
    if iv == 1:
        print('\nO valor da passagem de ida é R$350,00')
    elif iv == 2 :
        print('\nO valor da passagem de ida e volta é R$600,00')
elif op == 4:
    if iv == 1:
        print('\nO valor da passagem de ida é R$300,00')
    elif iv == 2:
        print('\nO valor da passagem de ida e volta é R$550,00')
else:
    print('\nOpção inexistente')
print('\n')
