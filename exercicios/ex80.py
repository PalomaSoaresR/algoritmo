quant = float(input('digite a quantidade de fitas: '))
valAluguel = float(input('digite o valor do aluguel: '))
fatAnual = quant/3 * valAluguel * 12 
print ('faturamento anual: ' ,fatAnual) 
multas = valAluguel * 0.1 * (quant/3)/10
print ('multas mensais: ' , multas)
quantFinal = quant - quant * 0.02 + quant/10; quant*1.08
print ('quantidade de fitas no final do ano: ' , quantFinal)
print (' ')
