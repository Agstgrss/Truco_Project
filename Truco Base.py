from time import sleep
from random import randint

team2 = team1 = 0  # times
valc1 = valc2 = 0  # valor carta atual
pdt1 = pdt2 = 0    # ponto dos turnos
pri=''             # fez a primeira

print("O jogo começou")
print("+-"*20)
while team1 < 12 and team2 < 12:           #Jogo em si
    pdt1 = pdt2 = 0
    print("Embaralhando as cartas")
    for c in range (1,4):                  #Para cada turno (fazer 3 vezes)
        #sleep(1)
        print("=-"*20)
        print(f"TURNO {c}")
        print("=-" * 20)
        #sleep(4)
        valc1 = valc2 = 0                  #valor carta atual
        valc1 = randint(1, 2)              #aleatorizando as cartas do time 1
        valc2 = randint(1, 2)              #aleatorizando as cartas do time 2

        print(f'O valor das cartas do time 1 é:[{valc1}]')
        #sleep(3)
        print(f'O valor das cartas do time 2 é:[{valc2}]')

        if valc1>valc2:                    #se o valor da carta atual do time 2 for maior do que o time1
            if c == 1:                     #se for o primeiro turno
                pri = "pri1"
            print(f"o Time 1  venceu o turno {c}")
            pdt1 +=1
            print(f"o Time 1 tem {pdt1} pontos de turno")
            if pdt1==2:                    #se o ponto de turno do time 1 for igual a 2
                print("A equipe 1 venceu a rodada")
                team1 += 1
                break
        if valc2>valc1:                    #se o valor da carta atual do time 2 for maior do que o time1
            if c == 1:                     #se for o primeiro turno
                pri = "pri2"
            print(f"o Time 2 venceu o turno {c}")
            pdt2 +=1
            print(f"o Time 2 tem {pdt2} pontos de turno")
            if pdt2==2:                    #se os pontos de turno do time 2 for igual a dois
                print("A equipe 2 venceu a rodada")
                team2 += 1
                break
        if valc1==valc2:                   #EMPATE
            print("Empate")
            if c==1:                       #se for o primeiro turno
                pdt1=pdt2=1
            elif c==2:                     #se for o segundo turno
                if pdt1>pdt2:              #se o time1 tiver mais pontos de turno
                    print('O time 1 ganhou a rodada por que fez a primeira')
                    team1 += 1
                    break
                elif pdt2>pdt1:            #se o time2 tiver mais pontos de turno
                    print('O time 2 ganhou a rodada por que fez a primeira')
                    team2 += 2
                    break
            elif c==3:                     #se for o turno 3
                print("Os times empataram o ultimo turno")
                if pdt1 == pdt2:
                    print("os times empataram 3  vezes")
                    break
                elif pri in 'pri1':        #se o time 1 ganhou a primeira
                    print("o time 1 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team1 = team1 + 1
                    break
                elif pri in 'pri2':        #se o time 2 ganhou a primeira
                    print("o time 2 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team2 = team2 + 1
                    break
                break

    print('='*20)
    print(f"o time 1 tem {team1} pontos")
    print(f"o time 2 tem {team2} pontos")
    print('=' * 20)

if team1 >= 12:                            #se o time 1 tem 12 ou mais pontos
    print('o time 1 Ganhou!!!')
if team2 >= 12:                            #se o time 2 tem 12 ou mais pontos
    print('o time 2 Ganhou!!!')
