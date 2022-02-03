import random
from helper_functions import *

# ---------- SETTINGS
target_31s = 5  # How many 31 IV's is the target? 6 = 6IV, must be between 0-6
male_chance = 0.5
runs = 1000
interactive = False
seed = 123  # "None" or seed. Used for running the comparisons on the same seed.

if isinstance(seed, int):
    random.seed(seed)

total_tries_unique_focus = 0
for _ in range(runs):
    male = [31, 31, 31, 0, 0, 0]
    female = [0, 0, 0, 31, 31, 31]

    offspring = [0, 0, 0, 0, 0, 0]
    offspring_gender = None

    tries = 0
    while not offspring.count(31) >= target_31s:
        tries += 1
        destiny_knot = check_for_destiny_knot(male, female)
        iv_slots = roll_inheritance(destiny_knot)
        if interactive:
            print(f'{male=}')
            print(f'{female=}')
            print(f'Knot ivs: {iv_slots}')
        offspring = generate_offspring(male, female, iv_slots, interactive)
        offspring_31s = offspring.count(31)
        offspring_gender = roll_gender(male_chance)
        if offspring_gender == 'male':  # Gender roll
            if check_for_replace(male, female, offspring, interactive):
                if interactive:
                    print('>>> Replace male')
                male = offspring.copy()
        else:
            offspring_gender = 'female'
            if check_for_replace(female, male, offspring, interactive):
                if interactive:
                    print('>>> Replace female')
                female = offspring.copy()
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    total_tries_unique_focus += tries
print(f'Average tries for {target_31s}IV prioritizing unique IVs: {total_tries_unique_focus/runs}')

if isinstance(seed, int):
    random.seed(seed)

total_tries_overall_focus = 0
for _ in range(runs):
    male = [31, 31, 31, 0, 0, 0]
    female = [0, 0, 0, 31, 31, 31]

    offspring = [0, 0, 0, 0, 0, 0]
    offspring_gender = None

    tries = 0
    while not offspring.count(31) >= target_31s:
        male_31s = male.count(31)
        female_31s = female.count(31)
        total_overall_31s = male_31s + female_31s
        total_unique_31s = 0  # How many positionally-unique 31s between both parents?
        for i in range(6):
            if male[i] == 31 or female[i] == 31:
                total_unique_31s += 1
        if total_overall_31s == 0 or total_overall_31s == 2 and total_unique_31s == 1:  # 0IV/0IV, 1IV/1IV same pos
            destiny_knot = False
        else:
            destiny_knot = True
        tries += 1
        iv_slots = [0, 1, 2, 3, 4, 5]
        iv_slots.remove(random.choice(iv_slots))
        if interactive:
            print(f'{male=}')
            print(f'{female=}')
            print(f'Knot ivs: {iv_slots}')
        for i in range(6):
            if i in iv_slots:  # For the positions left in the pool for inheritance
                if random.random() <= 0.5:  # Inherit IV at this position from male
                    offspring[i] = male[i]
                    if interactive:
                        perfect_iv_text = ' (31)' if male[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Male{perfect_iv_text}')
                else:  # Inherit IV at this position from female
                    if interactive:
                        perfect_iv_text = '(31)' if female[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Female {perfect_iv_text}')
                    offspring[i] = female[i]
            else:  # IVs taken out of the inherited pool
                offspring[i] = random.randint(0, 31)
                if interactive:
                    print(f'[IV {i}] RANDOM = ({offspring[i]})')
        if random.random() <= male_chance:  # Gender roll
            offspring_gender = 'male'
            if offspring.count(31) > male.count(31):
                if interactive:
                    print('Replace male')
                male = offspring.copy()
        else:
            offspring_gender = 'female'
            if offspring.count(31) > female.count(31):
                if interactive:
                    print('Replace female')
                female = offspring.copy()
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    total_tries_overall_focus += tries
print(f'Average tries for {target_31s}IV prioritizing overall IVs: {total_tries_overall_focus/runs}')

import random
from helper_functions import *

# ---------- SETTINGS
target_31s = 5  # How many 31 IV's is the target? 6 = 6IV, must be between 0-6
male_chance = 0.5
runs = 1000
interactive = False
seed = random.random()  # None or seed. Used for running the comparisons on the same seed.

total_tries_unique_focus = 0
total_tries_overall_focus = 0
for iteration in range(2):  # One iteration for unique IVs priority, one for overall IVs
    if seed is not None:
        random.seed(seed)
    for _ in range(runs):
        male = [31, 31, 31, 0, 0, 0]
        female = [0, 0, 0, 31, 31, 31]

        offspring = [0, 0, 0, 0, 0, 0]
        offspring_gender = None

        tries = 0
        while not offspring.count(31) >= target_31s:
            tries += 1
            if iteration == 0:  # Unique focus uses different destiny knot logic
                destiny_knot = check_for_destiny_knot(male, female)
            else:

            iv_slots = roll_inheritance(destiny_knot)
            if interactive:
                print(f'{male=}')
                print(f'{female=}')
                print(f'Knot ivs: {iv_slots}')
            offspring = generate_offspring(male, female, iv_slots, interactive)
            offspring_31s = offspring.count(31)
            if roll_gender(male_chance) == 'male':  # Gender roll
                offspring_gender = 'male'
                if iteration == 0:  # Unique IVs priority first
                    if check_for_replace(male, female, offspring, interactive):
                        if interactive:
                            print('>>> Replace male')
                        male = offspring.copy()
                else:
                    if offspring.count(31) > male.count(31):
                        if interactive:
                            print('Replace male')
                        male = offspring.copy()
            else:
                offspring_gender = 'female'
                if iteration == 0:  # Unique IVs priority first
                    if check_for_replace(female, male, offspring, interactive):
                        if interactive:
                            print('>>> Replace female')
                        female = offspring.copy()
                else:
                    if offspring.count(31) > female.count(31):
                        if interactive:
                            print('Replace female')
                        female = offspring.copy()
            if interactive:
                print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
                input()  # Just to pause; enter anything to continue
        if iteration == 0:  # Unique IVs priority first
            total_tries_unique_focus += tries
        else:
            total_tries_overall_focus += tries
print(f'Average tries for {target_31s}IV prioritizing unique IVs: {total_tries_unique_focus/runs}')
print(f'Average tries for {target_31s}IV prioritizing overall IVs: {total_tries_overall_focus / runs}')

