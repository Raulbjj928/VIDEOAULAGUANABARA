#Exercicio 18

import math
an=float(input('Digite o angulo que vc deseja : '))
seno=math.sin(math.radians(an))
print(f'O angulo de {an}º tem o seno {seno:.2f}')
cos=math.cos(math.radians(an))
print(f'O angulo de {an}º tem o cosseno {cos:.2f}')
tan=math.tan(math.radians(an))
print(f'O angulo de {an}º tem  a tangente {tan:.2f}')