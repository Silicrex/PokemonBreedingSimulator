from helper_functions import *

# ---------- SETTINGS
target_31s = 6  # AT LEAST how many 31 IVs is the goal? 6 = 6IV, must be between 0-6.
do_replacements = True  # Replace progenitors as progress is made True/False
destiny_knot_setting = None  # [None = use optimally] [True = always use] [False = never use]
power_item_setting = True  # False = don't use. True = automatically use automatically. Or...
# Can manually provide power item data: needs to be a dict in this format {'slot': int, 'parent': string (gender)}
# For example, {'slot': 0, 'parent': 'male'}
must_be_male = False  # Is the goal a male 6IV offspring instead of any 6IV offspring?
male_chance = 0.5  # Chance for offspring to be male
runs = 10000  # How many trials to use to find an average
seed = 123  # None (random) or seed
interactive = False  # Pause after each breed, print detailed info (press enter or send any input to continue)

# ---------- Starting progenitors
male_base = [31, 31, 31, 31, 31, 31]
female_base = [0, 0, 0, 0, 0, 0]

if seed is not None:
    random.seed(seed)

all_tries = 0  # Total tries to reach goal from each run, averaged at the end
for _ in range(runs):
    male = male_base.copy()
    female = female_base.copy()

    offspring = [0, 0, 0, 0, 0, 0]  # Placeholder list for generating the offspring
    offspring_gender = None  # Placeholder value

    tries = 0  # Tries for current run
    while True:
        if offspring.count(31) >= target_31s:
            if not must_be_male:
                break
            elif offspring_gender == 'male':
                break
        tries += 1
        if destiny_knot_setting is None:  # Do optimally
            destiny_knot = check_for_destiny_knot(male, female)
        else:
            destiny_knot = destiny_knot_setting  # Bool
        power_item_data = None
        if power_item_setting is True:
            power_item_data = check_for_power_item(male, female)
        elif isinstance(power_item_setting, dict):
            power_item_data = power_item_setting.copy()
        iv_slots = roll_inheritance(destiny_knot, power_item_data)
        if interactive:
            print(f'{male=} ({male.count(31)}IV)')
            print(f'{female=} ({female.count(31)}IV)')
            print(f'{power_item_data=}')
            print(f'Inherited IV positions: {iv_slots}')
        offspring = generate_offspring(male, female, iv_slots, power_item_data, interactive)
        offspring_31s = offspring.count(31)
        offspring_gender = roll_gender(male_chance)
        if offspring_gender == 'male':
            if do_replacements and check_for_replace(male, female, offspring, interactive):
                if interactive:
                    print('>>> Replace male')
                male = offspring.copy()
        else:
            if do_replacements and check_for_replace(female, male, offspring, interactive):
                if interactive:
                    print('>>> Replace female')
                female = offspring.copy()
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    if interactive:
        print(f'GOAL REACHED AFTER {tries} TRIES')
    all_tries += tries
gender_text = ' Male' if must_be_male else ''
base_overlaps = 0  # How many overlaps the original pair had
for male_iv, female_iv in zip(male_base, female_base):
    if male_iv == female_iv == 31:
        base_overlaps += 1
overlaps_text = f"{base_overlaps} overlaps" if base_overlaps > 1 else f"{base_overlaps} overlap"
print(f'{male_base.count(31)}IV Male + {female_base.count(31)}IV Female ({overlaps_text}) TO '
      f'>= {target_31s}IV{gender_text}')
print(f'Average amount of tries: {all_tries/runs}')
