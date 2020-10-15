#Exercicio 17

import math
co=float(input(('Qual a medida do Cateto oposto ? : ')))
ca=float(input('Qual a medida do cateto adjascente ? : '))
hi= math.hypot(co,ca)
print(f'A hipotenuza vai medir {hi:.2f}')