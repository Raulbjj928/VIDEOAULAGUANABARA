
#Exercicio 13

salario=float(input('Quanto o funcionário recebe? R$'))
acrescimo=15 * salario / 100
total= salario + acrescimo
print('''
O funcionário que ganha {:.2f}R$ 
com o reajuste de 15% passará a receber {:.2f}R$'''.format(salario,total))