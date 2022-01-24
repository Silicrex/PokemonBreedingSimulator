import random

# ---------- SETTINGS
target_31s = 5  # AT LEAST how many 31 IVs is the goal? 6 = 6IV, must be between 0-6.
male_chance = 0.5  # Chance for offspring to be male
runs = 1  # How many trials to use to find an average
destiny_knot = None  # [True = always use] [False = never use] [None = use optimally]
# Destiny knot causes 5 IVs to be inherited by the offspring, instead of the normal 3
# Destiny knot is always better to use except when 0IV+0IV, or 1IV+1IV where the 31 is in the same position
interactive = True  # Pause after each breed, print detailed info (press enter or send any input to continue)

# random.seed(3555484)  # Can set seed or just turn it off by commenting out
all_tries = []  # List of total tries to reach goal from each run, averaged at the end
for _ in range(runs):
    male = [31, 31, 31, 0, 0, 0]  # IVs are represented as a list
    female = [0, 0, 0, 31, 31, 31]

    offspring = [0, 0, 0, 0, 0, 0]  # Placeholder list for generating the offspring
    offspring_gender = None  # Placeholder value

    tries = 0  # Tries for current run
    # while not (offspring.count(31) == 6 and offspring_gender == 'male'):  # Breed for 6IV male instead
    # You would specifically want a male in the case of propagating the IVs to a different species in the same egg group
    while not offspring.count(31) >= target_31s:
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
            new_total_unique_31s = 0  # How many unique 31s would we have if we did a replacement?
            for i in range(6):
                if offspring[i] == 31 or female[i] == 31:
                    new_total_unique_31s += 1
            # It's not worth replacing in the case where you get more overall 31s but less unique 31s
            beats_unique_31s = new_total_unique_31s > total_unique_31s
            if interactive:
                print(f'{new_total_unique_31s=}')
                print(f'{total_unique_31s=}')
                if beats_unique_31s:
                    print(f"Beats unique 31s! ({total_unique_31s} to {new_total_unique_31s})")
                    print(f"Overall 31s goes from {male_31s + female_31s} to {offspring_31s + female_31s}")
                if offspring_31s > male_31s:
                    if new_total_unique_31s >= total_unique_31s:
                        print('Offspring has more 31s and unique is at least as good')
                    else:
                        print('Offspring has more 31s but unique would be lower')
            if beats_unique_31s or offspring_31s > male_31s and new_total_unique_31s >= total_unique_31s:
                if interactive:
                    print('>>> Replace male')
                male = offspring.copy()
        else:
            offspring_gender = 'female'
            new_total_unique_31s = 0  # How many unique 31s would we have if we did a replacement?
            for i in range(6):
                if offspring[i] == 31 or male[i] == 31:
                    new_total_unique_31s += 1
            # It's not worth replacing in the case where you get more overall 31s but less unique 31s
            beats_unique_31s = new_total_unique_31s > total_unique_31s
            if interactive:
                print(f'{new_total_unique_31s=}')
                print(f'{total_unique_31s=}')
                if beats_unique_31s:
                    print(f"Beats unique 31s! ({total_unique_31s} to {new_total_unique_31s})")
                    print(f"Overall 31s goes from {male_31s + female_31s} to {male_31s + offspring_31s}")
                if offspring_31s > female_31s:
                    if new_total_unique_31s >= total_unique_31s:
                        print('Offspring has more 31s and unique is at least as good')
                    else:
                        print('Offspring has more 31s but unique would be lower')
            if beats_unique_31s or offspring_31s > female_31s and new_total_unique_31s >= total_unique_31s:
                if interactive:
                    print('>>> Replace female')
                female = offspring.copy()
        if interactive:
            print(f'Offspring #{tries} = {offspring} ({offspring_gender.capitalize()} {offspring.count(31)}IV)')
            input()  # Just to pause; enter anything to continue
    if interactive:
        print(f'GOAL REACHED AFTER {tries} TRIES')
    all_tries.append(tries)
print(f'Average amount of tries: {sum(all_tries) / len(all_tries)}')
