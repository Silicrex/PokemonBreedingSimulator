from helper_functions import *

# ---------- SETTINGS
specific_slots_num = 6  # Going for how many specific slots?
do_replacements = True  # Replace progenitors as progress is made True/False
destiny_knot_setting = None  # [None = use optimally] [True = always use] [False = never use]
power_item_setting = True  # False = don't use. True = automatically use optimally. Or...
# Can manually provide power item data: needs to be a dict in this format {'slot': int, 'parent': string (gender)}
# For example, {'slot': 0, 'parent': 'male'}
must_be_male = True  # Is the goal a male 6IV offspring instead of any 6IV offspring?
male_chance = 0.5  # Chance for offspring to be male
runs = 10000  # How many trials to use to find an average
seed = None  # None (random) or seed
interactive = False  # Pause after each breed, print detailed info (press enter or send any input to continue)

# ---------- Starting progenitors
# For easy copy/paste: [31, 31, 31, 31, 31, 31] [0, 0, 0, 0, 0, 0]
male_base = [31, 31, 31, 31, 31, 31]
female_base = [0, 0, 0, 0, 0, 0]

if seed is not None:
    random.seed(seed)

list_of_slots = list(range(specific_slots_num))

all_tries = 0  # Total tries to reach goal from each run, averaged at the end
count2 = 0
for _ in range(runs):
    male = male_base.copy()
    female = female_base.copy()

    offspring = [0, 0, 0, 0, 0, 0]  # Placeholder list for generating the offspring
    offspring_gender = None  # Placeholder value

    tries = 0  # Tries for current run
    while True:
        if offspring.count(31) >= specific_slots_num:
            gender_check = True  # Flag for success condition
            slot_check = True  # Flag success condition
            if must_be_male and offspring_gender != 'male':
                gender_check = False
            for i in list_of_slots:
                if offspring[i] != 31:
                    slot_check = False
                    break  # Break out of check for slots, not main loop
            if gender_check and slot_check:  # If all pass
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
            if do_replacements and check_for_specific_positions_replace(male, female, offspring, specific_slots_num):
                if interactive:
                    print('>>> Replace male')
                male = offspring.copy()
        else:
            if do_replacements and check_for_specific_positions_replace(female, male, offspring, specific_slots_num):
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
overlaps_text = f"{base_overlaps} overlaps" if base_overlaps != 1 else f"{base_overlaps} overlap"
male_slots = []
female_slots = []
for index, values in enumerate(zip(male_base, female_base)):
    # values = tuple of (male IV, female IV)
    if values[0] == 31:
        male_slots.append(str(index))
    if values[1] == 31:
        female_slots.append(str(index))
print(f'Male: {male_base.count(31)}IV [Slot {", ".join(male_slots)}]\n'
      f'Female: {female_base.count(31)}IV Female [Slot {", ".join(female_slots)}]\n'
      f'({overlaps_text})\n'
      f'Goal: >= {specific_slots_num}IV{gender_text} [Slot {", ".join([str(x) for x in list_of_slots])}]')
print(f'Average amount of tries: {all_tries/runs}')