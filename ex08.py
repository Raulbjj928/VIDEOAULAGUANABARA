#Exercicio 8

medida=float(input('digite uma medida em metros :'))
cm=medida * 100
mm=medida * 1000
dm=medida*10
dam=medida*0.1
hm=medida*0.01
km=medida*0.001
print('''
a medida de {} corresponde a {}cm , {}mm,dm{},dam{},hm{} e km{}
'''.format(medida,cm,mm,dm,dam,hm,km))