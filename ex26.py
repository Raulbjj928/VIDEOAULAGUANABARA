#Exercicio 26

frase=input('Escreva algo : ').upper().strip()
print(f'''
A letra "A" aparece {frase.count("A")} vezes nessa frase
A primeira vez na posição {frase.find("A") + 1}
e a ultima na posição {frase.rfind("A") + 1}''')