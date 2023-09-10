p = float(input('digite o valor da aplicação: '))
i = float(input('digite a taxa (0-1): '))
n = float(input('digite o número de meses: '))
va = p*(((1+i)**n)-1)/i
print ('o valor acumulado: ' , va)
print (' ')
