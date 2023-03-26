"""
21) Escrever um algoritmo que lê:
- a percentagem do IPI a ser acrescido no valor das peças
- o código da peça 1, valor unitário da peça 1, quantidade de peças 1
- o código da peça 2, valor unitário da peça 2, quantidade de peças 2
O algoritmo deve calcular o valor total a ser pago e apresentar o resultado.
Fórmula : (valor1*quant1 + valor2*quant2)*(IPI/100 + 1)

"""

ipi = float(input("Digite a percentagem do IPI a ser acrescido: "))

codigo1 = int(input("Digite o código da peça 1: "))

valor1 = float(input("Digite o valor unitário da peça 1: "))

quant1 = int(input("Digite a quantidade de peças 1: "))

codigo2 = int(input("Digite o código da peça 2: "))

valor2 = float(input("Digite o valor unitário da peça 2: "))

quant2 = int(input("Digite a quantidade de peças 2: "))


total = (valor1 * quant1 + valor2 * quant2) * (ipi / 100 + 1)

print(f"O valor total a ser pago é: R${total:.2f}")
