import random
import emoji

def emb (a=0,b=0):
    mao1 = {}
    mao2 = {}
    manilha = {}
    baralhoo = {
        emoji.emojize('4:heart_suit:'): {'poder': 1},
        emoji.emojize('4:spade_suit:'):  {'poder': 1},
        emoji.emojize('4:diamond_suit:'): {'poder': 1},
        emoji.emojize('4:diamond_suit:'): {'poder': 1},
        emoji.emojize('5:spade_suit:'): {'poder': 2},
        emoji.emojize('5:heart_suit:'): {'poder': 2},
        emoji.emojize('5:diamond_suit:'): {'poder': 2},
        emoji.emojize('5:club_suit:'):  {'poder': 2},
        emoji.emojize('6:diamond_suit:'):{'poder': 3},
        emoji.emojize('6:heart_suit:'): {'poder': 3},
        emoji.emojize('6:club_suit:'): {'poder': 3},
        emoji.emojize('6:spade_suit:'):  {'poder': 3},
        emoji.emojize('7:heart_suit:'): {'poder': 4},
        emoji.emojize('7:diamond_suit:'): {'poder': 4},
        emoji.emojize('7:club_suit:'): {'poder': 4},
        emoji.emojize('7:spade_suit:'):  {'poder': 4},
        emoji.emojize('Q:spade_suit:'):  {'poder': 5},
        emoji.emojize('Q:heart_suit:'): {'poder': 5},
        emoji.emojize('Q:diamond_suit:'): {'poder': 5},
        emoji.emojize('Q:club_suit:'): {'poder': 5},
        emoji.emojize('J:spade_suit:'):  {'poder': 6},
        emoji.emojize('J:diamond_suit:'): {'poder': 6},
        emoji.emojize('J:heart_suit:'): {'poder': 6},
        emoji.emojize('J:club_suit:'): {'poder': 6},
        emoji.emojize('K:spade_suit:'):  {'poder': 7},
        emoji.emojize('K:diamond_suit:'): {'poder': 7},
        emoji.emojize('K:club_suit:'): {'poder': 7},
        emoji.emojize('K:heart_suit:'): {'poder': 7},
        emoji.emojize('A:spade_suit:'):  {'poder': 8},
        emoji.emojize('A:heart_suit:'): {'poder': 8},
        emoji.emojize('A:club_suit:'):    {'poder': 8},
        emoji.emojize('A:diamond_suit:'): {'poder': 8},
    }
    items = list(baralhoo.items())  # List of tuples of (key,values)
    random.shuffle(items)

    while len(mao1) <= 0:
        mao2.update(items[:3])
        mao1.update(items[-3:])
        valuesmao2 = list(mao2.values())
        valuesmao1 = list(mao1.values())
        keysmao1 = list(mao1.keys())
        keysmao2 = list(mao2.keys())
        manilha.update(items[9:10])
        manilhakeys= list(manilha.keys())
        manilhavalue = list(manilha.values())     #vira retirado mas preciso ainda fazer a manilha pelo sistema de ranking
        #manilhavalue++
        cartes1=valuesmao1[2]['poder']
        cartes2=valuesmao2[2]['poder']

    #print(f'jogador mao 1 {keysmao1}''\n'f'e o do jogador 2 {keysmao2} o vira é esse {manilhakeys}.'

    b=int(cartes2)
    a=int(cartes1)
    return a,b
