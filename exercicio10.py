"""
10) Faça um algoritmo que leia o tempo de duração de um evento em uma 
fábrica expressa em segundos e mostre-o expresso em horas, minutos e 
segundos.

"""
duracao_evento = int(input("insira o valor de duracao em segundos do evento: "))

duracao_horas = duracao_evento // 3600
duracao_minutos = (duracao_evento % 3600) // 60
duracao_segundos = (duracao_evento % 3600) % 60

print(f"A duracao do evento foi de {duracao_horas} Hora(s), {duracao_minutos} Minutos e {duracao_segundos} Segundos")

