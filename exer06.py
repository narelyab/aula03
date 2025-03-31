time1=input("qual seu time?")
time2=input("quem e o adversario?")
goltime1=int(input("digite o numero de gols do time 1"))
goltime2=int(input("digite o numero de gols do time 2"))
if goltime1>goltime2:
    print(f"{time1} vencedor")
else:
    if goltime2>goltime1:
        print(f"{time2} vencedor")
    else:
        print("empate")
        