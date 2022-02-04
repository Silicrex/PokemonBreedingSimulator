import random

# ---------- SETTINGS
available_slots = 6  # How many slots are rolling? 1-6
runs = 10000

if available_slots == 0:
    print('0% chance')

total_tries = 0
for _ in range(runs):  # What is the chance of
    no_31s = True
    while no_31s:
        total_tries += 1
        for _ in range(available_slots):
            if random.randint(0, 31) == 31:
                no_31s = False
                break
print(f'Average tries: {total_tries/runs}')
print(f'Observed chance: {1 / (total_tries/runs):.3%}')
chance_for_31 = 1/32
print(f'Real chance: {1 - (1 - chance_for_31)**available_slots:.3%}')
