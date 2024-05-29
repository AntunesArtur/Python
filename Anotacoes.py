# Estruturas de decisão

# if else
if condicao:
    
else:


# else if
if condicao: 
    
elif condicao:
    
else:


# match
match variavel:
    case 1:       
    
    case _:


# Estruturas de repetição

# For
# range(3) 0 a <3 = 2
# range(1,4) começa em 1 e termina em menor que 4 = 3
# range(1,10,2) começa em 1 e anda 2 em 2 até < 10

for i in range(1, 4):


# while
while condicao:


# do while/ciclo repeat
while True: # ciclo infinito
    
    if condicao: # condição paragem
        break # sai do ciclo mais próximo

# fazer o cast do input

idade = int(input("Idade: ")) # input devolve texto
temp1 = eval(input("temperatura de segunda: ")) # converte para int ou double consuante o caso

# fazer o print com a função fString

print(f"Nome: {nome} Idade: {idade}") # fString

# print(f"""
#       Soma: {num1+num2}
#       Subtração: {num1-num2}
#       Multiplicação: {num1*num2}
#       Divisão: {num1/num2 :.2f}
#       """)

# Funções

# implementação
def soma(num1, num2):
    return num1 + num2

def ePar(num1):
    return num1%2 == 0 # retornar um valor lógico
 
# utilização - chamadas
print(soma(2,3))
val = soma(2,3)
if val>5:
    print("Maior")
else:
    print("Menor")

# função que retorna vários valores

def lerDados():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    return nome, idade
 
nome, idade = lerDados()
print(nome, idade)

# função com vários argumentos

def lerValor(msg, min, max):
    while True:
        nota = int(input(msg))
        if min <= nota <= max:
            return nota
        print(f"\nErro: nota inválida, por favor insira valores entre {min} e {max}!\n")

