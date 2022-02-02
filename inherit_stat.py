from helper_functions import *
runs = 100000

destiny_knot = True

# Arbitrarily using attack stat to see outcomes for a particular stat
attack_included = 0  # How many times was attack selected for inheritance
for _ in range(runs):
    iv_slots = [0, 1, 2, 3, 4, 5]
    if destiny_knot:  # Destiny knot = inherit all but one
        iv_slots = roll_inheritance(iv_slots, destiny_knot=True)
    else:  # Otherwise, inherit 3 of 6
        iv_slots = roll_inheritance(iv_slots)
    if 0 in iv_slots:
        attack_included += 1

print(f'Avg % of times inherited: {attack_included/runs:.4%}\n'
      f'Avg % of times not: {(runs - attack_included)/runs:.4%}')
