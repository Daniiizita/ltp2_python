"""
17) Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles formam
 ou não um triângulo. Supor que os valores lidos são inteiros e positivos.
   Caso os valores formem um triângulo, calcular e escrever a área deste 
   triângulo. Se não formam triângulo escrever os valores lidos. 
   ( se a > b + c não formam triângulo algum, se a é o maior).

"""

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b + c or b > a + c or c > a + b:
    print(f"{a}, {b} e {c} não formam um triângulo.")
else:
    
    s = (a + b + c) / 2
   
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Os valores {a}, {b} e {c} formam um triângulo de área {area :.2f}.")
