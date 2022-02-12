from helper_functions import *

# ---------- SETTINGS
target_31s = 6  # How many 31 IV's is the target? 6 = 6IV, must be between 0-6
male_chance = 0.5
runs = 5000
interactive = False
seed = random.random()  # None or seed. Used for running the comparisons on the same seed.
# ^ Use random.random() for same seed between unique/overall focus but random seed between runs of the program

total_tries_unique_focus = 0
total_tries_overall_focus = 0
for iteration in range(2):  # One iteration for unique IVs priority, one for overall IVs
    if seed is not None:
        random.seed(seed)
    for _ in range(runs):
        # For easy copy/paste: [0, 0, 0, 0, 0, 0] [31, 31, 31, 31, 31, 31]
        male = [31, 31, 31, 0, 0, 0]
        female = [0, 0, 0, 31, 31, 31]

        offspring = [0, 0, 0, 0, 0, 0]
        offspring_gender = None

        tries = 0
        while not offspring.count(31) >= target_31s:
            tries += 1
            if iteration == 0:  # Prioritize unique 31s
                destiny_knot = check_for_destiny_knot(male, female)
            else:  # Prioritize overall 31s
                destiny_knot = check_for_destiny_knot(male, female, prioritize_uniques=False)
            iv_slots = roll_inheritance(destiny_knot)
            if interactive:
                print(f'{male=}')
                print(f'{female=}')
                print(f'Knot ivs: {iv_slots}')
            offspring = generate_offspring(male, female, iv_slots, interactive=interactive)
            offspring_31s = offspring.count(31)
            if roll_gender(male_chance) == 'male':  # Gender roll
                offspring_gender = 'male'
                if iteration == 0:  # Unique IVs priority first
                    if check_for_replace(male, female, offspring, interactive=interactive):
                        if interactive:
                            print('>>> Replace male')
                        male = offspring.copy()
                else:  # Overall IVs priority
                    if check_for_replace(male, female, offspring, prioritize_overalls=True, interactive=interactive):
                        if interactive:
                            print('Replace male')
                        male = offspring.copy()
            else:
                offspring_gender = 'female'
                if iteration == 0:  # Unique IVs priority first
                    if check_for_replace(female, male, offspring, interactive=interactive):
                        if interactive:
                            print('>>> Replace female')
                        female = offspring.copy()
                else:  # Overall IVs priority
                    if check_for_replace(female, male, offspring, prioritize_overalls=True, interactive=interactive):
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
