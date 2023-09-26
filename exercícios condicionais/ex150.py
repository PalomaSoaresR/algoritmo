import math as m
ang = float(input('\nDigite o ângulo em graus: '))
rang = ang * m.pi / 180
if ((rang > m.pi/2) == (rang <= m.pi)) == ((rang > 3* m.pi/2) == (rang < 2 * m.pi )):
   print ('\nSeno: ' , m.sin(rang))
else:
   print('\nCo-seno: ' , m.cos(rang))