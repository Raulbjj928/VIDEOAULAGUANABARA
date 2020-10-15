#Exercicio 11

lap= float(input('Largura da parede: '))
alp= float(input('Altura da parede: '))
quant=(lap*alp)/2
print('''
Sua parede tem a dimensão de {}m x {}m,
e sua área é de {:.3f}m²'''.format(lap,alp,lap*alp))
print('E precisará de {:.3f}L de tinta para pinta-la.'.format(quant))