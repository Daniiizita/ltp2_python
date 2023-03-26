"""
7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
 meses e dias e mostre-a expressa apenas em dias.


"""
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em anos: "))
dias = int(input("Digite sua idade em dias: "))

idade_em_dias = anos * 365 + meses * 30 + dias

print(f"A idade em dias é {idade_em_dias} dias.")
