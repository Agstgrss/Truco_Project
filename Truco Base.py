from time import sleep
from random import randint

team2 = team1 = 0  # times
valc1 = valc2 = 0  # valor carta atual
pdt1 = pdt2 = 0    # ponto dos turnos
pri=''             # fez a primeira

print("O jogo começou")
while team1 < 12 or team2 < 12:            #Jogo em si
    for c in range (1,4):                  #Para cada turno (fazer 3 vezes)
        sleep(1)
        print("=-"*20)
        print("Sorteando as cartas")
        sleep(4)
        valc1 = randint(1, 1)              #aleatorizando as cartas do time 1
        valc2 = randint(1, 1)              #aleatorizando as cartas do time 2

        print(f'O valor das cartas do time 1 é:[{valc1}]')
        sleep(3)
        print(f'O valor das cartas do time 2 é:[{valc2}]')

        if valc1 > valc2:                  #se o valor das cartas do time 1 for maior
            sleep(3)
            print(f'A equipe 1 venceu o turno {c}')
            pdt1 = pdt1 + 1
            sleep(1)
            print(f'A equipe 1 tem {pdt1} pontos de turno nessa rodada ')
            if c == 1:                     #se for o primeiro turno
                pri = "pri1"
            if pdt1 == 2:                  #se os pontos do turno do time 1 for igual a dois
                sleep(1)
                print('A equipe 1 venceu a rodada')
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                break
            if c==3 and pri in 'pri1':     #se for o turno 3 e a equipe 1 venceu a primeira
                print('A equipe 1 venceu a rodada pois fez a primeira')
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                c=3

        if valc2 > valc1:                  #se o valor das cartas do time 2 for maior
            sleep(2)
            print(f'A equipe 2 venceu o turno {c}')
            pdt2 = pdt2 + 1
            sleep(1)
            print(f'A equipe 2 tem {pdt2} pontos de turno nessa rodada ')
            if c == 1:                     #se for o primeiro turno
                pri = "pri2"

            if pdt2 == 2:                  #se os pontos do turno do time 2 for igual a dois, 
                sleep(1)
                print('A equipe 2 venceu a rodada')
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                break
            if c==3 and pri in 'pri2':     #se for o turno 3 e a equipe 2 venceu a primeira
                print('A equipe 2 venceu a rodada pois fez a primeira')
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                c=3

        if valc1 == valc2:                 #Empate
            sleep(3)
            print('Empate')
            if c==3:                       #Se for a terceira todada
                print("Ual, 3 empates seguidos, a rodada começa de novo")
                pdt1 = pdt2 = 0
                break
            if pdt1 > pdt2:                #se o time 1 ganhou mais turnos do que o time 2
                pdt1 = pdt2 = 0
                team1 = team1 + 1
                print('A equipe 1 venceu o primeiro turno e levou a rodada')
                break
            elif pdt1 < pdt2:              #se o time 2 ganhou mais turnos do que o time 1
                pdt1 = pdt2 = 0
                team2 = team2 + 1
                print('A equipe 2 venceu o primeiro turno e levou a rodada')
                break
            elif pdt1 == 0 and pdt2 == 0:  #se o time 1 e o time 2 nao ganharam nenhum turno
                print('as equipes mostram a maior')
            elif pdt1 == 1 and pdt2 == 1:  #se o time 1 e o time 2 nao ganharam ambos um turno
                if pri in 'pri1':          #se o time 1 ganhou a primeira
                    print("o time 1 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team1 = team1 + 1
                    break
                elif pri in 'pri2':        #se o time 2 ganhou a primeira
                    print("o time 2 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team2 = team2 + 1
                    break
                else:                      #se for o segundo empate
                    print('Ultimo turno após 2 empates')
        c = c + 1                          #aumenta o turno
    pdt1 = pdt2 = 0                        #reseta os pontos do turno, nova rodada
    sleep(2)
    print('='*15)
    print(f'o time 1 tem {team1} pontos')
    print(f'o time 2 tem {team2} pontos')
    print('='*15)
    sleep(2)

if team1 >= 12:                            #se o time 1 tem 12 ou mais pontos
    print('o time 1 Ganhou!!!')
if team2 >= 12:                            #se o time 2 tem 12 ou mais pontos
    print('o time 2 Ganhou!!!') 


