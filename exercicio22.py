"""
22) Escrever um algoritmo que lê a hora de início e hora de término 
de um jogo, ambas subdivididas em dois valores 
distintos : horas e minutos. Calcular e escrever a duração do jogo, 
também em horas e minutos, considerando que o tempo máximo de 
duração de um jogo é de 24 horas e que o jogo pode iniciar em um 
dia e terminar no dia seguinte.

"""

hora_inicio = int(input("Digite a hora de início do jogo: "))
min_inicio = int(input("Digite os minutos de início do jogo: "))
hora_fim = int(input("Digite a hora de término do jogo: "))
min_fim = int(input("Digite os minutos de término do jogo: "))

total_minutos_inicio = hora_inicio * 60 + min_inicio
total_minutos_fim = hora_fim * 60 + min_fim

duracao = total_minutos_fim - total_minutos_inicio

if duracao < 0:
    duracao += 1440

horas = duracao // 60
minutos = duracao % 60

print(f"A duração do jogo foi de {horas} horas e {minutos} minutos.")

