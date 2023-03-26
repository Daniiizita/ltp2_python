"""
8) 4. Faça um algoritmo que leia a idade de uma pessoa expressa
 em dias e mostre-a expressa em anos, meses e dias.

"""

idade_dias = int(input("insira sua idade em dias: \n"))

idade_anos = idade_dias // 365
dias_restantes = idade_dias % 365

idade_meses = idade_dias // 30
idade_dias = dias_restantes % 30


print(f"A idade é de {idade_anos} anos, {idade_meses} meses e {idade_dias} dias.")