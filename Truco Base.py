from time import sleep
from random import randint
team2=team1=0
ptt1=ptt2=0
pdt1=pdt2=0
print("O jogo começou")
while team1<12 or team2<12:
    sleep(2)
    while pdt1<=2 or pdt2<=2:
        print("Sorteando as cartas")
        sleep(2)
        ptt1=randint(1,9)
        ptt2=randint(1,9)
        print(f'O valor do time1 é {ptt1}')
        print(f'O valor do time2 é {ptt2}')
        if ptt2 > ptt1:
            sleep(2)
            print('A equipe 2 venceu o turno')
            pdt2 = pdt2 + 1
            if pdt2==2:
                print('A equipe 2 venceu a rodada')
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                break
        if ptt1 > ptt2:
            sleep(3)
            print('A equipe 1 venceu o turno')
            pdt1 = pdt1 + 1
            if pdt1==2:
                print('A equipe 1 venceu a rodada')
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                break

        if ptt1==ptt2:
            sleep(3)
            print('Empate')


    sleep(2)
    print(f'o time1 tem {team1} pontos')
    sleep(2)
    print(f'o time2 tem {team2} pontos')






    if team1 >=12:
        print('o time1 Ganhou')
        break
    if team2 >= 12:
        print('o time2 Ganhou')
        break

