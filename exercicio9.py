"""
9) Faça um algoritmo que leia as 3 notas de um aluno e calcule a
 média final deste aluno. Considerar que a média é ponderada e 
 que o peso das notas é: 2,3 e 5, respectivamente.

"""
nota1 = float(input("insira 1 a nota do aluno: "))
nota2 = float(input("insira 2 a nota do aluno: "))
nota3 = float(input("insira 3 a nota do aluno: "))


nota1 = nota1*2
nota2 = nota2*3
nota3 = nota3*5

media = (nota1 + nota2 + nota3) / 10 
#nao tinha certeza se deveria por o numero de notas na divisao ou a soma dos pesos, entao coloquei a soma dos pesos acima

print(f"A sua media é: {media :.2f}")
