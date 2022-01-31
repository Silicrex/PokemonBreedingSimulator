import random

# ---------- SETTINGS
target_31s = 5  # How many 31 IV's is the target? 6 = 6IV, must be between 0-6
male_chance = 0.5
seed = random.random()  # "None" or seed. Used for running the comparisons on the same seed.
runs = 1000
interactive = False

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

