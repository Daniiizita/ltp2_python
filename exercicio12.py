"""
12) Calcule a média aritmética das 3 notas de um aluno e mostre, 
além do valor da média, uma mensagem de "Aprovado", caso a média 
seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.

"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f"Sua média é {media:.2f}. Aprovado!")
else:
    print(f"Sua média é {media:.2f}. Reprovado!")