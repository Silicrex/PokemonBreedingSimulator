import random

# ---------- SETTINGS
male_chance = 0.5
runs = 1
interactive = True
male = [31, 0, 0, 0, 0, 0]
female = [31, 0, 0, 0, 0, 0]
random.seed(1337)
overlaps = 0
# ----------

male_31s = male.count(31)
female_31s = female.count(31)
if male_31s + female_31s == 12:
    print('Impossible to make further progress, already maxed with two 6IVs')
    quit()
for male_iv, female_iv in zip(male, female):
    if male_iv == female_iv == 31:
        overlaps += 1
print(f'{male.count(31)}IV + {female.count(31)}IV ({overlaps} overlaps)')

overall_tries_with_knot = 0
for _ in range(runs):
    offspring = [0, 0, 0, 0, 0, 0]
    tries = 0  # Local try number
    while True:  # Loop ended when optimal progress is made
        tries += 1
        iv_slots = [0, 1, 2, 3, 4, 5]
        iv_slots.remove(random.choice(iv_slots))  # Use destiny knot
        if interactive:
            print(f'Inherited IV positions: {iv_slots}')
        for i in range(6):
            if i in iv_slots:
                if random.random() <= 0.5:  # Male draw
                    offspring[i] = male[i]
                    if interactive:
                        perfect_iv_text = ' (31)' if male[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Male{perfect_iv_text}')
                else:  # Female draw
                    offspring[i] = female[i]
                    if interactive:
                        perfect_iv_text = '(31)' if female[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Female {perfect_iv_text}')
            else:
                offspring[i] = random.randint(0, 31)
                if interactive:
                    print(f'[IV {i}] RANDOM = ({offspring[i]})')
        total_overall_31s = male_31s + female_31s
        total_unique_31s = 0  # How many positionally-unique 31s between both parents?
        for i in range(6):
            if male[i] == 31 or female[i] == 31:
                total_unique_31s += 1
        offspring_31s = offspring.count(31)
        if random.random() <= male_chance:  # Gender roll
            if interactive:
                print(f'Offspring #{tries} = {offspring} (Male {offspring.count(31)}IV)')
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
                    print('>>> Beats male')
                break
        else:
            if interactive:
                print(f'Offspring #{tries} = {offspring} (Male {offspring.count(31)}IV)')
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
                    print('>>> Beats female')
                break
        if interactive:
            input()  # Pause before continuing to next breed
    overall_tries_with_knot += tries
print(f'Average tries to make progress w/ destiny knot: {overall_tries_with_knot/runs}')
if interactive:
    print('Next, without destiny knot')

overall_tries_without_knot = 0
for _ in range(runs):
    offspring = [0, 0, 0, 0, 0, 0]
    tries = 0  # Local try number
    while True:  # Loop ended when optimal progress is made
        tries += 1
        iv_slots = [0, 1, 2, 3, 4, 5]
        for _ in range(3):
            iv_slots.remove(random.choice(iv_slots))  # Use destiny knot
        if interactive:
            print(f'Inherited IV positions: {iv_slots}')
        for i in range(6):
            if i in iv_slots:
                if random.random() <= 0.5:  # Male draw
                    offspring[i] = male[i]
                    if interactive:
                        perfect_iv_text = ' (31)' if male[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Male{perfect_iv_text}')
                else:  # Female draw
                    offspring[i] = female[i]
                    if interactive:
                        perfect_iv_text = '(31)' if female[i] == 31 else ''  # Signify when a 31 is inherited
                        print(f'[IV {i}] Female {perfect_iv_text}')
            else:
                offspring[i] = random.randint(0, 31)
                if interactive:
                    print(f'[IV {i}] RANDOM = ({offspring[i]})')
        total_overall_31s = male_31s + female_31s
        total_unique_31s = 0  # How many positionally-unique 31s between both parents?
        for i in range(6):
            if male[i] == 31 or female[i] == 31:
                total_unique_31s += 1
        offspring_31s = offspring.count(31)
        if random.random() <= male_chance:  # Gender roll
            if interactive:
                print(f'Offspring #{tries} = {offspring} (Male {offspring.count(31)}IV)')
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
                    print('>>> Beats male')
                break
        else:
            if interactive:
                print(f'Offspring #{tries} = {offspring} (Female {offspring.count(31)}IV)')
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
                    print('>>> Beats female')
                break
        if interactive:
            input()  # Pause before continuing to next breed
    overall_tries_without_knot += tries
print(f'Average tries to make progress without destiny knot: {overall_tries_without_knot/runs}')