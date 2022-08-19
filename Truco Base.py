from time import sleep
from random import randint

team2 = team1 = 0  # times
valc1 = valc2 = 0  # valor carta
pdt1 = pdt2 = 0    # ponto dos turnos
pri=''             # fez a primeira

print("O jogo começou")
while team1 < 12 or team2 < 12:            #Jogo em si
    for c in range (1,4):                  #Cada rodada com 3 turnos
        sleep(1)
        print("=-"*20)
        print("Sorteando as cartas")
        sleep(4)
        valc1 = randint(1, 1)              #aleatorizando as cartas
        valc2 = randint(1, 1)

        print(f'O valor das cartas do time 1 é:[{valc1}]')
        sleep(3)
        print(f'O valor das cartas do time 2 é:[{valc2}]')

        if valc1 > valc2:  # valor das cartas do time 1 é superior
            sleep(3)
            print(f'A equipe 1 venceu o turno {c}')
            pdt1 = pdt1 + 1
            sleep(1)
            print(f'A equipe 1 tem {pdt1} pontos de turno nessa rodada ')
            if c == 1:
                pri = "pri1"
            if pdt1 == 2:
                sleep(1)
                print('A equipe 1 venceu a rodada')
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                break
            if c==3 and pri in 'pri1':
                print('A equipe 1 venceu a rodada pois fez a primeira')
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                c=3

        if valc2 > valc1:  # valor das cartas do time 2 é superior
            sleep(2)
            print(f'A equipe 2 venceu o turno {c}')
            pdt2 = pdt2 + 1
            sleep(1)
            print(f'A equipe 2 tem {pdt2} pontos de turno nessa rodada ')
            if c == 1:
                pri = "pri2"

            if pdt2 == 2:
                sleep(1)
                print('A equipe 2 venceu a rodada')
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                break
            if c==3 and pri in 'pri2':
                print('A equipe 2 venceu a rodada pois fez a primeira')
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                c=3

        if valc1 == valc2:  # Empate
            sleep(3)
            print('Empate')
            if c==3:
                print("outro empate começe dnv")
                pdt1 = pdt2 = 0
                break
            if pdt1 > pdt2:
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                print('A equipe 1 venceu o primeiro turno e levou a rodada')
                break
            elif pdt1 < pdt2:
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                print('A equipe 2 venceu o primeiro turno e levou a rodada')
                break
            elif pdt1 == 0 and pdt2 == 0:
                print('as equipes mostram a maior')
            elif pdt1 == 1 and pdt2 == 1:
                if pri in 'pri1':
                    print("o time 1 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team1 = team1 + 1
                    break
                elif pri in 'pri2':
                    print("o time 2 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team2 = team2 + 1
                    break
                else:
                    print('Ultimo turno após 2 empates')
        c = c + 1
    pdt1 = pdt2 = 0
    sleep(2)
    print('='*15)
    print(f'o time 1 tem {team1} pontos')
    print(f'o time 2 tem {team2} pontos')
    print('='*15)
    sleep(2)

if team1 >= 12:
    print('o time 1 Ganhou!!!')
if team2 >= 12:
    print('o time 2 Ganhou!!!')


