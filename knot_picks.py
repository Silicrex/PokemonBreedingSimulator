import random
runs = 100000

attack_included = 0
attack_not_included = 0
for _ in range(runs):
    iv_slots = [0, 1, 2, 3, 4, 5]
    mutation_roll = random.choice(iv_slots)
    if mutation_roll != 1:
        attack_included += 1
    else:
        attack_not_included += 1
print(f'{attack_included/runs=}\n'
      f'{attack_not_included/runs=}')
