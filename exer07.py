
combustivel=input("qual combustivel usado?\n"
                  " G para gasolina "
                  "E para etanol\n")
litros=float(input("quantos litros foram abastecidos\n"))
E=4.90
G=5.80
if combustivel == "g":
    preco = litros * G
    print(f"abastecido {litros} litros "
          f"e foi gasto {preco}2f")
elif combustivel=="e":
    preco=litros*E
    print(f"abatecido{litros} litros "
          f"e foi gasyo{preco}2f")
else:
    print("tipo de combustivel invalido")