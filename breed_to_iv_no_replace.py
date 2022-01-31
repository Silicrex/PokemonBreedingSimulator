import random

# ---------- SETTINGS
target_31s = 6  # AT LEAST how many 31 IVs is the goal? 6 = 6IV, must be between 0-6.
male_chance = 0.85  # Chance for offspring to be male
must_be_male = True
runs = 10000  # How many trials to use to find an average
destiny_knot = None  # [True = always use] [False = never use] [None = use optimally]
# Destiny knot causes 5 IVs to be inherited by the offspring, instead of the normal 3
# Destiny knot is always better to use except when 0IV+0IV, or 1IV+1IV where the 31 is in the same position
interactive = False  # Pause after each breed, print detailed info (press enter or send any input to continue)

# random.seed(3555484)  # Can set seed or just turn it off by commenting out
all_tries = 0  # List of total tries to reach goal from each run, averaged at the end
for _ in range(runs):
    male = [31, 31, 31, 31, 31, 31]  # IVs are represented as a list
    female = [31, 31, 31, 31, 31, 0]

    offspring = [0, 0, 0, 0, 0, 0]  # Placeholder list for generating the offspring
    offspring_gender = None  # Placeholder value

    tries = 0  # Tries for current run
    # while not (offspring.count(31) == 6 and offspring_gender == 'male'):  # Breed for 6IV male instead
    # You would specifically want a male in the case of propagating the IVs to a different species in the same egg group
    while True:
        if offspring.count(31) >= target_31s:
            if must_be_male:
                if offspring_gender == 'male':
                    break
            else:
                break
        tries += 1
        male_31s = male.count(31)
        female_31s = female.count(31)
        total_overall_31s = male_31s + female_31s
        total_unique_31s = 0  # How many positionally-unique 31s between both parents?
        for i in range(6):
            if male[i] == 31 or female[i] == 31:
                total_unique_31s += 1
        if destiny_knot is None:  # If no static value given, use optimally
            if total_overall_31s == 0 or total_overall_31s == 2 and total_unique_31s == 1:  # 0IV/0IV, 1IV/1IV same pos
                destiny_knot = False
                if interactive:
                    print('NO KNOT WOULD WIN')
            else:
                destiny_knot = True
        iv_slots = [0, 1, 2, 3, 4, 5]  # For determining which IVs to inherit, numbers are slot numbers
        if destiny_knot:  # Inherit 5 (only remove one)
            iv_slots.remove(random.choice(iv_slots))
        else:  # Remove 3
            for _ in range(3):
                iv_slots.remove(random.choice(iv_slots))
        if interactive:
            print(f'{male=}')
            print(f'{female=}')
            print(f'Inherited IV positions: {iv_slots}')
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
        offspring_31s = offspring.count(31)
        if random.random() <= male_chance:  # Gender roll
            offspring_gender = 'male'
        else:
            offspring_gender = 'female'
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    if interactive:
        print(f'GOAL REACHED AFTER {tries} TRIES')
    all_tries += tries
avg_tries = all_tries/runs
print(f'Average amount of tries: {avg_tries}')
print(f'Chance: {1/avg_tries * 100:.2f}%')
