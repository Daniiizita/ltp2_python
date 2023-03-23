"""
5) Escreva um programa que exiba o valor total a ser pago em 
empréstimo bancário. O programa deve solicitar ao usuário os 
seguintes dados: 
- Valor emprestado 
- Meses para quitar o empréstimo 
- Taxa de juros mensais 
Utilize a seguinte fórmula para calcular o valor total pago ao final 
do empréstimo: 
ValorFinal = ValorEmprestado * (1 + juros) ** meses 

"""

valor_emprestado = float(input("insira o valor que será emprestado: "))

meses = int(input("insira o valor de meses para quitação do emprestimo: "))

taxa_de_juros = float(input("insira o valor da taxa de juros mensais: "))


taxa_de_juros = (taxa_de_juros * valor_emprestado) / 100

valor_final = valor_emprestado * (1 + taxa_de_juros) ** meses 

print(f"o valor final a ser pago na quitação do empréstimo será de R$ {valor_final:.2f}")
