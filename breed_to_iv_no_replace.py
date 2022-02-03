import random
from helper_functions import *

# ---------- SETTINGS
target_31s = 6  # AT LEAST how many 31 IVs is the goal? 6 = 6IV, must be between 0-6.
male_chance = 0.77  # Chance for offspring to be male
must_be_male = True
runs = 1000  # How many trials to use to find an average
destiny_knot_setting = None  # [True = always use] [False = never use] [None = use optimally]
seed = 3555484  # None or seed
interactive = False  # Pause after each breed, print detailed info (press enter or send any input to continue)

if seed is not None:
    random.seed(seed)

all_tries = 0  # List of total tries to reach goal from each run, averaged at the end
for _ in range(runs):
    male = [31, 31, 31, 31, 31, 31]  # IVs are represented as a list
    female = [0, 0, 0, 0, 0, 0]

    offspring = [0, 0, 0, 0, 0, 0]  # Placeholder list for generating the offspring
    offspring_gender = None  # Placeholder value

    tries = 0  # Tries for current run
    while True:
        if offspring.count(31) >= target_31s:
            if not must_be_male:
                break
            if must_be_male and offspring_gender == 'male':
                break
        tries += 1
        if destiny_knot_setting is None:  # Do optimally
            destiny_knot = check_for_destiny_knot(male, female)
        else:
            destiny_knot = destiny_knot_setting  # Bool
        iv_slots = [0, 1, 2, 3, 4, 5]  # For determining which IVs to inherit, numbers are slot numbers
        iv_slots = roll_inheritance(iv_slots, destiny_knot)
        if interactive:
            print(f'{male=}')
            print(f'{female=}')
            print(f'Destiny knot = {destiny_knot}')
            print(f'Inherited IV positions: {iv_slots}')
        offspring = generate_offspring(male, female, iv_slots, interactive)
        offspring_gender = roll_gender(male_chance)
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    if interactive:
        print(f'GOAL REACHED AFTER {tries} TRIES')
    all_tries += tries
avg_tries = all_tries/runs
print(f'Average amount of tries: {avg_tries}')
print(f'Chance: {1/avg_tries:.2%}')
