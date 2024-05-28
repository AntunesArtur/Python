# comentário de 1 linha - documentar o nosso código
"""
sdfsd
sdf
sdf
"""
'''
sdafsdf
sdf
sdf
'''
 
#idade = 23.23 # atribuição
#print(idade)
# operação de input - entrada de dados
nome = input("Nome: ")
idade = int(input("Idade: ")) # input devolve texto
print(nome)
print(idade)
idade = idade + 1
print(idade)

nome = input("Nome: ")
idade = int(input("Idade: ")) # input devolve texto
print(f"Nome: {nome} Idade: {idade}") # fString

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))
 
num1, num2, num3 = int(input("Introduza 3 números: ")), int(input()), int(input())
 
print(f"Multiplicação: {num1*num2*num3}")