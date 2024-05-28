# nome = input("Nome: ")
# salario = int(input("salário bruto: "))
# #salario = float(input("salário bruto: "))

# print(f"{nome} - salário líquido: {salario-salario*0.11-salario*0.18}€")

#exercico 2
# nome = input("Indique o seu nome: ")
# dias = float(input("Quantos dias trabalhou neste mês? "))
# valor_Subsidio = float(input("Qual o valor so Subsídio diário?"))

# print(f"O {nome} tem direito a {dias * valor_Subsidio} Euros de Subsídio.")

#exercicio 3

# temp1 = eval(input("temperatura de segunda: "))
# temp2 = eval(input("temperatura de terça: "))
# temp3 = eval(input("temperatura de quarta: "))
# temp4 = eval(input("temperatura de quinta: "))
# temp5 = eval(input("temperatura de sexta: "))
# temp6 = eval(input("temperatura de sábado: "))
# temp7 = eval(input("temperatura de domingo: "))

# print(f"Média de temperatura: {(temp1+temp2+temp3+temp4+temp5+temp6+temp7)/7:.2f}")

#exercicio 4
# nota = int(input("Nota: "))
# # nota < 10 Negativa nota >= 10 e <= 15 Positiva >=16 Bom
# if 0 <= nota < 10: # if nota >= 0 and nota < 10
#     print(f"{nota} -> Negativa")
# elif 10 <= nota < 16:
#     print(f"{nota} -> Positiva")
# elif 16 <= nota <= 20:
#     print(f"{nota} -> Bom")
# else:
#     print(f"\nErro: {nota} fora do intervalo\n")

#exercicio5
# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
 
# print(f"""
#       Soma: {num1+num2}
#       Subtração: {num1-num2}
#       Multiplicação: {num1*num2}
#       Divisão: {num1/num2 :.2f}
#       """)
 
# if num1 % 2 == 0:
#     print(f"{num1} é par!")
# else:
#     print(f"{num1} é impar!")
 
# if num2 % 2 == 0:
#     print(f"{num2} é par!")
# else:
#     print(f"{num2} é impar!")    
 
# if num1 % 2 == 0 and num2 % 2 == 0:
#     print("Ambos são pares")
# elif num1 % 2 != 0 and num2 % 2 != 0:
#     print("Ambos são impares")
# else:
#     print("Os números não são ambos pares/impares")

#exercicio 6
# print("Insira valores entre a e 20.")
# soma = 0
# min = None
# max = None

# num = int(input("Insira o 1º número:"))
# soma += num
# print(f"A soma é {soma}")
# min = num
# max = num

# num = eval(input("Insira o 2º número:"))
# soma += num
# print(f"A soma é {soma}")

# if min > num:
#     min = num
# if max < num:
#     max = num

# num = eval(input("Insira o 3º número:"))
# soma += num
# print(f"A soma é {soma}")

# if min > num:
#     min = num
# if max < num:
#     max = num

# num = eval(input("Insira o 4º número:"))
# soma += num
# print(f"A soma é {soma}")

# if min > num:
#     min = num
# if max < num:
#     max = num

# num = eval(input("Insira o 5º número:"))
# soma += num
# print(f"A soma é {soma}")

# if min > num:
#     min = num
# if max < num:
#     max = num

# print(f"O minímo é {min}")
# print(f"O máximo é {max}")

#resolução formador
# min = None
# max = None
# sum = 0
# count = 1
 
# inserir 1.ª nota
# value = int(input(f"Insira o valor n.º {count}: ")) # 2 3
# sum += value # 0 + 2 = 2 / 2 + 3 = 5
# print(f"Soma: {sum}")
# # calcular max e min
# if count == 1:
#     min = value # min = 2
#     max = value # max = 2
# else:
#     if value > max: # 3 > 2
#         max = value # max = 2
#     if value < min: # 3 < 2
#         min = value
# count += 1 # count = count + 1
 
# # inserir 2.ª nota
# value = int(input(f"Insira o valor n.º {count}: ")) # 2 3
# sum += value # 0 + 2 = 2 / 2 + 3 = 5
# print(f"Soma: {sum}")
# # calcular max e min
# if count == 1:
#     min = value # min = 2
#     max = value # max = 2
# else:
#     if value > max: # 3 > 2
#         max = value # max = 2
#     if value < min: # 3 < 2
#         min = value
# count += 1 # count = count + 1
 
# # inserir 3.ª nota
# value = int(input(f"Insira o valor n.º {count}: ")) # 2 3
# sum += value # 0 + 2 = 2 / 2 + 3 = 5
# print(f"Soma: {sum}")
# # calcular max e min
# if count == 1:
#     min = value # min = 2
#     max = value # max = 2
# else:
#     if value > max: # 3 > 2
#         max = value # max = 2
#     if value < min: # 3 < 2
#         min = value
# count += 1 # count = count + 1
 
# # inserir 4.ª nota
# value = int(input(f"Insira o valor n.º {count}: ")) # 2 3
# sum += value # 0 + 2 = 2 / 2 + 3 = 5
# print(f"Soma: {sum}")
# # calcular max e min
# if count == 1:
#     min = value # min = 2
#     max = value # max = 2
# else:
#     if value > max: # 3 > 2
#         max = value # max = 2
#     if value < min: # 3 < 2
#         min = value
# count += 1 # count = count + 1
 
# # inserir 5.ª nota
# value = int(input(f"Insira o valor n.º {count}: ")) # 2 3
# sum += value # 0 + 2 = 2 / 2 + 3 = 5
# print(f"Soma: {sum}")
# # calcular max e min
# if count == 1:
#     min = value # min = 2
#     max = value # max = 2
# else:
#     if value > max: # 3 > 2
#         max = value # max = 2
#     if value < min: # 3 < 2
#         min = value
 
 
# print(f"Máximo: {max} Mínimo: {min}")
# print(f"Média: {sum/count :.2f}")

