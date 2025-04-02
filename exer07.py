
combustivel=input("qual combustivel usado?\n"
                  "g para gasolina\n"
                  "e para etanol\n")
litros=float(input("quantos litros foram abastecidos\n"))
e=4.90
g=5.80
if combustivel == "g":
    preco = litros * g
    print(f"abastecido {litros} litros "
          f"e foi gasto {preco}2f")
elif combustivel=="e":
    preco=litros*e
    print(f"abatecido{litros} litros "
          f"e foi gasyo{preco}2f")
else:
    print("tipo de combustivel invalido")