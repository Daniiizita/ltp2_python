notas_disponiveis = [200, 100, 50, 20, 10, 5, 2, 1]

valor_saque = int(input("Digite o valor do saque: "))

for nota in notas_disponiveis:
    quantidade_notas = valor_saque // nota
    if quantidade_notas > 0:
        print(f"{quantidade_notas} notas de R${nota}")
    valor_saque %= nota
