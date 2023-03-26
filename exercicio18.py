"""
18) Escrever um algoritmo que lê a hora de início de um jogo e a hora do 
final do jogo (considerando apenas horas inteiras) e calcula a 
duração do jogo em horas, sabendo-se que o tempo máximo de duração 
do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar 
no dia seguinte.


"""

hora_inicio = int(input("Digite a hora de início do jogo: "))
hora_fim = int(input("Digite a hora do fim do jogo: "))

if hora_fim < hora_inicio:
    hora_fim += 24

duracao = hora_fim - hora_inicio
print(f"A duração do jogo foi de {duracao} horas.")


hora_inicio = int(input("Digite a hora de início do jogo: "))
hora_fim = int(input("Digite a hora do fim do jogo: "))

if hora_fim < hora_inicio:
    hora_fim += 24

duracao = hora_fim - hora_inicio
print(f"A duração do jogo foi de {duracao} horas.")
