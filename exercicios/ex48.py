sm = float(input('entre com o salário mínimo: '))
qtdade = float(input('entre com a quantidade em quilowatt: '))
preço = sm / 700
vp = preço + qtdade
vd = vp * 9/10
print ('preço do quilowarr: ' , preço , 'valor a ser pago: ' , vp , 'valor com desconto: ' , vd)
print (' ')