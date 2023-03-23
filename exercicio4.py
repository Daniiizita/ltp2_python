"""
Uma empresa contrata um colaborador a R$ 120,00 por dia. 
Escreva um programa que solicite o número de dias trabalhados pelo encanador e 
imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda. 

"""


dias_trabalhados = int(input("insira o numero de dias trabalhados: "))

valor_dia = 120

valor_bruto = valor_dia * dias_trabalhados

valor_liquido = valor_bruto - ((valor_bruto / 8) * 1.0)

print(f"O valor do salário que o trabalhador recebeu é de R$ {valor_liquido:.2f}")
