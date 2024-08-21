largura = int(input("Digite a largura do terreno"))
altura = int(input("Digite a altura do terreno"))

area = largura * altura

if area < 100:
    print("A área é popular")

elif area > 100 < 500:
    print("A área é um terreno master B)")

elif area > 500:
    print("A área é VIP!!!!!.")

if largura > 10:
    print("""
        ______________________
        ALERTA: AREA COMERCIAL
        ----------------------
        """)
