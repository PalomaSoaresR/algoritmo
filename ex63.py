ht = float(input('horas trabalhadas: ')) 

ha = float(input('valor da hora-aula: ')) 

pd = float(input('percentual de desconto: ')) 

sb = ht * ha 

td = (pd/100)*sb 

sl = sb-td 

print('salário liquido: ' , sl) 

print(' ') 