from helper_functions import *

# ---------- SETTINGS
male_chance = 0.5
runs = 1000
interactive = False
seed = 1337  # None or seed. Used for running the comparisons on the same seed.
# ^ Use random.random() for same seed between unique/overall focus but random seed between runs of the program

male = [31, 31, 31, 0, 0, 0]
female = [31, 31, 31, 0, 0, 0]
# ----------

if male.count(31) + female.count(31) == 12:
    print('Impossible to make further progress, already maxed with two 6IVs')
    quit()

overall_tries_with_knot = 0
overall_tries_without_knot = 0
for iteration in range(2):  # Do a run with destiny knot, then run without
    if seed is not None:
        random.seed(seed)
    for _ in range(runs):
        tries = 0  # Local try number
        while True:  # Loop will break when optimal progress is made
            tries += 1
            if iteration == 0:  # Do destiny knot first
                iv_slots = roll_inheritance(destiny_knot=True)
            else:
                iv_slots = roll_inheritance()
            if interactive:
                print(f'Inherited IV positions: {iv_slots}')
            offspring = generate_offspring(male, female, iv_slots, interactive)
            if roll_gender(male_chance) == 'male':  # Gender roll
                if interactive:
                    print(f'Offspring #{tries} = {offspring} (Male {offspring.count(31)}IV)')
                if check_for_replace(male, female, offspring, interactive):
                    if interactive:
                        print('>>> Beats male')
                    break
            else:
                if interactive:
                    print(f'Offspring #{tries} = {offspring} (Male {offspring.count(31)}IV)')
                if check_for_replace(female, male, offspring, interactive):
                    if interactive:
                        print('>>> Beats female')
                    break
            if interactive:
                input()  # Pause before continuing to next breed
        if iteration == 0:
            overall_tries_with_knot += tries
        else:
            overall_tries_without_knot += tries
base_overlaps = 0  # How many overlaps the original pair had
for male_iv, female_iv in zip(male, female):
    if male_iv == female_iv == 31:
        base_overlaps += 1
overlaps_text = f"{base_overlaps} overlaps" if base_overlaps > 1 else f"{base_overlaps} overlap"
print(f'{male.count(31)}IV Male + {female.count(31)}IV Female ({overlaps_text})')
print(f'Average tries to make progress w/ destiny knot: {overall_tries_with_knot/runs}')
print(f'Average tries to make progress without destiny knot: {overall_tries_without_knot/runs}')
print('(Progress towards optimally breeding to 6IV)')
