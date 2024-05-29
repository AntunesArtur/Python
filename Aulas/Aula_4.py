# # exercicio 23 #########################

# Pop_A = 80000
# Pop_B = 200000
# contador = 0

# while Pop_A <= Pop_B:

#     Pop_A *= 1.03
#     Pop_B *= 1.015
#     contador += 1

# print(f"São necessários {contador} anos para a popupalção do país A ultrapassar a do país B.")

# resolução formador
# popPaisA = 80000
# popPaisB = 200000
 
# txCresPaisA = 1.03
# txCresPaisB = 1.015
 
# anos = 0
 
# while popPaisA<popPaisB:
#     popPaisA *= txCresPaisA # popPaisA = popPaisA + popPaisA*txCresPaisA
#     popPaisB *= txCresPaisB
#     anos += 1
 
# print(f"Após {anos} anos a população do país A é de {popPaisA :.0f} pessoas e do país B {popPaisB :.0f} pessoas!")

# exercicio 24 #########################

# # com clico while
# num_gerados = 0
# num = 0

# while num_gerados < 50:
#     num += 1
#     if num % 2 == 0:
#         print(f"{num}")
#         num_gerados +=1

# # com ciclo for
# num = 2
# for i in range(50):
#     print(f"{num}")
#     num += 2

# # resolução formador

# # for i in range(0, 101, 2):
# #     print(i)
 
# # for i in range(0, 51):
# #     print(i*2)
 
# count = 0
# while count < 51:
#     print(count*2)
#     count+=1

# # exercício 25

# valor = int(input("Introduza um valor entre 1 e 10: "))

# for i in range(10):
#     print(f"{valor} * {i+1} = {valor * (i+1)}")

# # correção formador

# while True:
#     val = int(input("Introduza um valor entre 1 e 10: "))
#     if 1 <= val <= 10:
#         break
#     print("\nAlooooooooo: entre 1 e 10!\n")
 
# for i in range(1, 11):
#     print(f"{val} * {i} = {val*i}")

# # exercício 13 segunda versão

# nota1 = None
# nota2 = None
# nota3 = None
 
# while True:

#     print("Prima 1 para ler a nota de 3 alunos (0 a 20)")
#     if nota1 and nota2 and nota3:
#         print("Prima 2 para devolver a média dos 3 alunos")
#         print("Prima 3 para devolver a soma das notas dos 3 alunos")
#     print("Prima 4 para sair")
    
#     op = int(input("Indique a opção desejada: "))
    
#     match op:
#         case 1:
#             while True:

#                 # while True:
#                 #     if input("Nota do 1º aluno: "):
#                 #         nota1 = eval(input("Nota do 1º aluno: "))
#                 #         break
#                 #     else:
#                 #         print("não inseriu nenhum valor!")
                
#                 # if input("Nota do 2º aluno: "):
#                 #     nota2 = eval(input("Nota do 2º aluno: "))

#                 # if input("Nota do 3º aluno: "):
#                 #     nota3 = eval(input("Nota do 3º aluno: "))

#                 nota1, nota2, nota3 = eval(input("Nota do 1º aluno: ")), eval(input("Nota do 2º aluno: ")), eval(input("Nota do 3º aluno: "))
#                 if 0<=nota1<=20 and 0<=nota1<=20 and 0<=nota1<=20:
#                     break
#                 else:
#                     print("As notas têm de estar no intervalo [0:20]")
#         case 2:
#             if nota1 and nota2 and nota3:
#                 print(f"Média: {(nota1+nota2+nota3)/3 :.2f}")
#             else:
#                 print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#         case 3:
#             if nota1 and nota2 and nota3:
#                 print(f"Soma: {nota1+nota2+nota3}")
#             else:
#                 print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#         case 4:
#             print("bye bye")
#         case _:
#             print("\nErro: opção inválida\n")
    
#     if op == 4: 
#         break # podia ficar dentro do case 4

# # resolução formador

# nota1 = None
# nota2 = None
# nota3 = None
 
# while True:
#     print("Prima 1 para ler a nota de 3 alunos (0 a 20)")
#     if nota1 and nota2 and nota3:
#         print("Prima 2 para devolver a média dos 3 alunos")
#         print("Prima 3 para devolver a soma das notas dos 3 alunos")
#     print("Prima 4 para sair")
 
#     op = int(input("Indique a opção desejada: "))
#     match op:
#         case 1:
#             while True:
#                 val = int(input("Nota1: "))
#                 if 0 <= val <= 20:
#                     nota1 = val
#                     break
#                 print("\nErro: valor inválido!\n")
#             while True:
#                 val = int(input("Nota2: "))
#                 if 0 <= val <= 20:
#                     nota2 = val
#                     break
#                 print("\nErro: valor inválido!\n")
#             while True:
#                 val = int(input("Nota3: "))
#                 if 0 <= val <= 20:
#                     nota3 = val
#                     break
#                 print("\nErro: valor inválido!\n")                
#         case 2:
#             if nota1 and nota2 and nota3:
#                 print(f"Média: {(nota1+nota2+nota3)/3 :.2f}")
#             else:
#                 print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#         case 3:
#             if nota1 and nota2 and nota3:
#                 print(f"Soma: {nota1+nota2+nota3}")
#             else:
#                 print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#         case 4:
#             print("bye bye")
#             break
#         case _:
#             print("\nErro: opção inválida\n")

# # função que retorne o produto de 3 números

# def produto(num1, num2, num3):
#     return num1*num2*num3

# # função que retorne o máximo de 2 números

# def maximo(num1, num2):

#     max = num1

#     if num2 > max:
#         max = num2
    
#     return max

# # função que imprime 10 num pares

# def print_pares():    
#     for i in range(10):
#         print((i+1)*2)

# print_pares()

# def print_pares_2(inicial):

#     for i in range(inicial, inicial+10):
#         if i == 1 and inicial%2 == 0:
#             print(inicial)
#         print((i+1)*2)

# print_pares_2(2)

# # correção formador
# def soma(num1, num2):
#     return num1 + num2
 
# # crie uma função que retorne o produto de 3 números
# def produto(n1, n2, n3):
#     return n1*n2*n3
 
# # crie uma função que retorne o máximo de 2 números
# def maximo(n1, n2):
#     if n1>n2:
#         return n1
#     return n2
 
# # crie uma função que imprima 10 números pares
# def pares():
#     for i in range(10):
#         print(i*2, end=' ')
#     print()
 
# #print(soma(2,3))
# #print(produto(2,3,8))
# #print(maximo(8,3))
# pares()
# print("Eu sou qq coisa")

