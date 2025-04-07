hora1=int(input("h1 que horas sao?"))
minuto1=int(input("m1 e quantos minutos?"))
hora2=int(input("h2 que horas sao ?"))
minuto2=int(input("m2 e quantos minutos?"))

if hora1>12:
    hora1=hora1-12
if hora2>12:
    hora2=hora2-12
somaH=hora1+hora2
if somaH>12:
    somaH=somaH-12
    print(somaH)
somaM=minuto1+minuto2
if somaM >=60:
    somaH+=1
    somaM=somaM % 60
    print(somaH,somaM)












