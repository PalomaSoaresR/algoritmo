valor = float(input('digite o valor da prestação:  ')) 

taxa =  float(input('digite a taxa: ')) 

tempo = float(input('digite o tempo (n° de meses):  ')) 

prest = valor+(valor*(taxa/100)*tempo) 

print ('o valor da prestação em atraso é= ', prest) 

print (' ') 