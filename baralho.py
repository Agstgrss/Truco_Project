import random
mao1 = []
mao2 = []
baralho = {
    4.1: {'nipe': 'copas', 'poder': 1},
    4.2: {'nipe': 'espadas', 'poder': 1},
    4.3: {'nipe': 'ouros', 'poder': 1},
    4.4: {'nipe': 'paus', 'poder': 1},
    5.1: {'nipe': 'paus', 'poder': 2},
    5.2: {'nipe': 'copas', 'poder': 2},
    5.3: {'nipe': 'ouros', 'poder': 2},
    5.4: {'nipe': 'espadas', 'poder': 2},
    6.1: {'nipe': 'ouros', 'poder': 3},
    6.2: {'nipe': 'copas', 'poder': 3},
    6.3: {'nipe': 'paus', 'poder': 3},
    6.4: {'nipe': 'espadas', 'poder': 3},
    7.1: {'nipe': 'copas', 'poder': 4},
    7.2: {'nipe': 'ouros', 'poder': 4},
    7.3: {'nipe': 'paus', 'poder': 4},
    7.4: {'nipe': 'espadas', 'poder': 4},
    11.1: {'nipe': 'espadas', 'poder': 5},
    11.2: {'nipe': 'copas', 'poder': 5},
    11.3: {'nipe': 'ouros', 'poder': 5},
    11.4: {'nipe': 'paus', 'poder': 5},
    12.1: {'nipe': 'espadas', 'poder': 6},
    12.2: {'nipe': 'ouros', 'poder': 6},
    12.3: {'nipe': 'copas', 'poder': 6},
    12.4: {'nipe': 'paus', 'poder': 6},
    13.1: {'nipe': 'espadas', 'poder': 7},
    13.2: {'nipe': 'ouros', 'poder': 7},
    13.3: {'nipe': 'paus', 'poder': 7},
    13.4: {'nipe': 'copas', 'poder': 7},
    14.1: {'nipe': 'espadas', 'poder': 8},
    14.2: {'nipe': 'copas', 'poder': 8},
    14.3: {'nipe': 'paus', 'poder': 8},
    14.4: {'nipe': 'ouros', 'poder': 8},
}
cartas = baralho.items()
mao1 = random.sample(cartas, 39)

# k, v in baralho.items():
    #print(f'O {k} é {v}')

print(mao1)
