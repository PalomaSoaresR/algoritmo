ang = float(input('digite um ângulo em graus: '))
import math as m
rang = ang*m.pi / 180
print ('seno: ' , m.sin (rang))
print ('co-seno:' , m.cos(rang))
print ('tangente: ' , m.tan(rang))
print ('co-secante: ' , 1/ m.sin(rang))
print ('secante: ' , 1/ m.cos(rang))
print ('cotangente: ',  1/ m.tan(rang))
print (" ")