"""
11) O custo ao consumidor de um carro novo é a soma do custo de fábrica 
com a percentagem do distribuidor e dos impostos (aplicados ao custo 
de fábrica). Supondo que a percentagem do distribuidor seja de 28% e
 os impostos de 45%, escrever um algoritmo que leia o custo de fábrica 
 de um carro e escreva o custo ao consumidor.

"""
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45
custo_consumidor = custo_fabrica + percentagem_distribuidor + impostos

print(f"O custo ao consumidor é: R${custo_consumidor:.2f}")