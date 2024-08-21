nome = str(input("Digite o nome do funcionário: "))
tempoDeEmpresa = int(input("Digite quanto tempo o funcionário trabalha na empresa: "))
salario = int(input("Digite o salário do funcionário: "))
tipo = int(input("Digite o tipo do funcionário: "))
recebimento = int

if tempoDeEmpresa < 3:
    salario * 0.03
    print(salario)

elif tempoDeEmpresa >= 3 < 10:
    salario * 0.10
    print(salario)

elif tempoDeEmpresa >= 10:
    salario * 0.20
    print(salario)

