nome=input("qual e o seu nome?\n")
idade=int(input("qual sua idade?\n"))
salario=float(input("qual o salario?\n"))
percentual=float(input("digite o percentual de aumento"))
valorp=salario * percentual/100
novosalario=salario+valorp
print(f"ola  {nomee}  minha idade e  {idade}  eu recebo  {salario:.2f}  mais tive um aumento de {valorp},entao no final irei receber {novosalario}")
