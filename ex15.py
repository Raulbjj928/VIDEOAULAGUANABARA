#Exercicio 15

d = int(input('Quantos dias alugados? :' ))
km = float(input('Quantos Km rodados? : '))
paga = float(d * 60) + (km * 0.15)
print('O total a pagar é {:.2f}R$'.format(paga))