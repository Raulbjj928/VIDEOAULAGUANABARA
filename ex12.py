#Exercicio 12

valor=float(input('Qual o preço do produto?R$'))
desconto= (5*valor)/100
total=valor-desconto
print('Esse produto com 5% de desconto fica {:.2f}R$'.format(total))