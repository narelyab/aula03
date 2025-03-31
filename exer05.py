nota1=float(input("informe a primeira nota"))
nota2=float(input("informe a ssegunda nota"))
nota3=float(input("informe a terceira nota"))
media=(nota1+nota2+nota3)/3
if media>=7:
    print(f"aprovado")
elif media >= 4:
    print(f"recuperacao")
else:
    print(f"reprovado")
