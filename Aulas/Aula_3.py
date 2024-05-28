# #exercicio 1

# opcao = None
# nota1 = None
# nota2 = None
# nota3 = None

# print("Prima 1 para ler a nota de 3 alunos")
# print("Prima 2 para imprimir a média das notas")
# print("Prima 3 para imprimir a soma das notas")
# print("Prima 4 para sair.")

# opcao = eval(input("Escolha uma opção: "))

# match opcao:
#     case 1:
#         nota1 = eval(input("Nota do 1º aluno: "))
#         nota2 = eval(input("Nota do 2º aluno: "))
#         nota3 = eval(input("Nota do 3º aluno: "))
#         opcao = eval(input("Escolha uma opção: "))
#     case 2:
#         if nota1 != None and nota1 != None and nota3 != None:
#             print(f"A média das notas é: {(nota1+nota2+nota3)/3}")
#         else:
#             print("As notas inseridas não são válidas")    
#     case 3:
#         print(f"A soma das notas é: {nota1+nota2+nota3}")
#     case 4:
#         exit
#     case _:
#         print("Opção inválida")

# #Exercicio 1 RESOLUÇÂO FORMADOR

# nota1 = None
# nota2 = None
# nota3 = None
 
# print("Prima 1 para ler a nota de 3 alunos (0 a 20)")
# if nota1 and nota2 and nota3:
#     print("Prima 2 para devolver a média dos 3 alunos")
#     print("Prima 3 para devolver a soma das notas dos 3 alunos")
# print("Prima 4 para sair")
 
# op = int(input("Indique a opção desejada: "))
# match op:
#     case 1:
#         nota1, nota2, nota3 = int(input("Nota de 3 alunos: ")), int(input("Nota: ")), int(input("Nota: "))
#     case 2:
#         if nota1 and nota2 and nota3:
#             print(f"Média: {(nota1+nota2+nota3)/3}")
#         else:
#             print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#     case 3:
#         if nota1 and nota2 and nota3:
#             print(f"Soma: {nota1+nota2+nota3}")
#         else:
#             print("\nErro: por favor introduza primeiro a nota dos 3 alunos\n")
#     case 4:
#         print("bye bye")
#     case _:
#         print("\nErro: opção inválida\n")

# Ciclo for

# # ler 3 notas
# # range(3) 0 a <3 = 2
# # range(1,4) começa em 1 e termina em menor que 4 = 3
# # range(1,10,2) começa em 1 e anda 2 em 2 até < 10
# for i in range(1, 4):
#     nota = int(input(f"Nota {i}: "))
 
# for i in range(1,10,2):
#     print(i)

#exercicio 2
# num = None
# soma = 0

# for i in range(1,11):
#     num = eval(input(f"Insira o {i}º número: "))
#     soma += num

# print(f"A soma dos números é {soma}.")

# # correção exercicio 2 formador
# # leia 10 números e no final apresente a sua soma
# # soma = 0
# # for i in range(10):
# #     val = int(input(f"Valor {i+1}: ")) # 3 4
# #     soma += val #soma = val + soma
# # print(f"Soma: {soma}")

# exercicio 3

# temp = None
# soma = 0

# for i in range(7):
#     temp = eval(input(f"Insira a temperadura do {i+1}º dia: "))
#     soma += temp

# print(f"A média das temperaturas é {soma/(i+1):.2f}.")

#exercicio 16

# num_alunos = None
# nota = None

# for i in range(num_alunos):
#     nota = eval(input(f"Nota do {i+1}º aluno:"))
    
#     match nota:
#         case _ if nota >= 0 and nota < 10:


# #resolução formador

# nStudents = int(input("Quantos alunos tem a turma? "))
# sum = 0
# max = None
# min = None
 
# for i in range(nStudents):
#     grade = eval(input("Nota: "))
#     sum += grade
#     if grade >= 10:
#         print("Aprovado")
#     else:
#         print("Reprovado")
#     if i == 0:
#         max = grade
#         min = grade
#     else:
#         if grade > max:
#             max = grade
#         if grade < min:
#             min = grade
 
# print(f"Média das notas: {sum/nStudents :.2f}\nNota mínima: {min}\nNota máxima: {max}")

# #exercico 18

# valor = None

# while valor != 0:
#     valor = int(input(f"Insere um valor: "))

# #ciclo repeat
# # ler valores inteiros até inserir o valor 0
# while True: # ciclo infinito
#     val = int(input("Valor: "))
#     if val == 0: # condição paragem
#         break # sai do ciclo mais próximo
#     print(val)

## exercicio 21
# contador = 0
# valor = None

# while True:
#     valor = eval(input(f"Insira um valor entre 0 e 20: "))
    
#     while not 0<=valor<=20:
#         valor = eval(input(f"O valor não é válido.\nInsira um valor entre 0 e 20: "))
#         if valor == -1:
#             break

#     if valor != None:
#         contador += 1

#     print(f"Foram introduzidos {contador} valores.")

#     if valor == -1:
#         break

# # correção formador

# count = 1
 
# while True:
#     val = int(input(f"{count} - Introduza um valor entre 0 e 20: "))
#     if val == -1:
#         print("Obrigado pela sua contribuição")
#         break
#     if 0 <= val <= 20:
#         count += 1
#     else:
#         print("Valor inválido! Por favor introduza novamente!")

# # exercicio 22

# num = None
# contador = 0

# num = int(input("\nInsira uma valor inteiro: "))

# while num >= 2:
#     num = num - 2
#     contador += 1

# print(f"\nO número {num + 2*contador} é divisível por 2, {contador} vezes.\n")


# # resolução formador
# num = int(input("Indique um número: "))
# numOriginal = num
# count = 0
 
# while(num%2 == 0):
#     num /= 2 # num = num / 2
#     count += 1
 
# print(f"O número {numOriginal} é divisivel {count} vezes por 2")