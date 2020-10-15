#Exercicio 22

nome=input('Digite seu nome : ')
print(f'''
Seu nome com as letras maiusculas é :
 {nome.upper()} e minusculas é : 
 {nome.lower()}''')
print(f"Esse nome tem {(len(nome.replace(' ', '')))} caracteres ")