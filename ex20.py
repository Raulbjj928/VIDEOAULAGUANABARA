#Exercicio 20

import random
n1=input('Digite um nome : ')
n2=input('Digite outro nome : ')
n3=input('Digite outro : ')
n4=input('Digite o ultimo nome : ')
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print(lista)