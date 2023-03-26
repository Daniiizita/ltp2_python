"""
6) Escreva um programa que leia um número entre 0 e 60 e imprima o seu
 sucessor, sabendo que o sucessor de 60 é 0. Não pode ser utilizado
   nenhuma estrutura de seleção (decisão) e nem repetição.

"""
num = int(input("Digite um número entre 0 e 60: "))
num = (num + 1) % 61
print(f"O sucessor é {num}")

