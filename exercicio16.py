"""
16) Escreva um algoritmo que leia o código de um aluno e suas três notas.
 Calcule a média ponderada do aluno, considerando que o peso para a maior
   nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, 
   suas três notas, a média calculada e uma mensagem "APROVADO" se a 
   média for maior ou igual a 5 e "REPROVADO" se a média for menor que 5.

"""

codigo = input("Digite o código do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maior_nota = max(nota1, nota2, nota3)
media = (maior_nota*4 + (nota1 + nota2 + nota3 - maior_nota)*3) / 10

print("Código do aluno:", codigo)
print("Notas:", nota1, ",", nota2, "e", nota3)
print("Média:", media)

if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO")
