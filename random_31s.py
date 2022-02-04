print('Chances are formulaically calculated and precise\n')
chance_for_31 = 1 / 32
for i in range(1, 7):
    chance_for_i_31s = chance_for_31**i
    print(f'Chance to roll {i}IV: 1/{int(1/chance_for_i_31s)} ({chance_for_i_31s:.9%})')