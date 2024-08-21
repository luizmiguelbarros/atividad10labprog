nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = nota1 + nota2 / 2

if media < 4.9:
    print("Está abaixo da média mínima... Reprovado!")

elif media > 5 < 6.9:
    print("Recuperação")

elif media > 7:
    print("Está acima da média! Aprovado!")