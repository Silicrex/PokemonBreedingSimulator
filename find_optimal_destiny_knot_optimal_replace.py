import random

# ---------- SETTINGS
male_chance = 0.5
runs = 1000
interactive = False


for male_31_ivs in range(7):  # Nested loop to get 0IV-0IV, 0IV-1IV, 0IV-2IV, etc without repeats (2IV-3IV == 3IV-2IV)
    for female_31_ivs in range(male_31_ivs, 7):
        male = [0] * 6  # Start with 0IV
        for i in range(male_31_ivs):  # Fill in 31's according to current combination
            male[i] = 31
        female = [0] * 6
        for i in range(female_31_ivs):
            female[i] = 31
        total_31s = male_31_ivs + female_31_ivs
        if total_31s == 12:  # Check for 6IV-6IV, which has already made all progress possible
            print('Reached 6IV-6IV, no more progress can be made')
            break
        # At this point, starting male and starting female are set
        # Next, try for each arrangement of possible overlaps (ie 2IV-2IV can have 0-2 overlaps; makes a BIG DIFFERENCE)
        if total_31s <= 6:  # When sum of 31's is <= 6, it's possible to have no overlap
            lower_bound = 0  # Lowest possible amount of overlaps for combination
        else:  # Once sum of 31's exceeds 6, lower bound becomes the difference between sum and 6
            # For example, 4IV-4IV. Sum of 8. The lowest overlap arrangement possible is 2 (8 minus 6).
            # Would look like [0, 0, 31, 31, 31, 31] [31, 31, 31, 31, 0, 0]
            lower_bound = total_31s - 6
        # First parent (arbitrarily chosen as male) always has less than or equal to amount of 31's as second parent
        upper_bound = male_31_ivs  # Highest possible amount of overlaps for combination
        possible_overlaps = 1 + upper_bound - lower_bound  # 1 in start bc a range like 3-3 overlaps is still one to do
        for overlap_number in range(possible_overlaps):
            if overlap_number != 0:  # Need to test first arrangement before we start shifting
                # Shift stats to the left (take first element, put it at the end; right shifting won't always work here)
                male.append(male.pop(0))

            # Simulate with knot first
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
                                    perfect_iv_text = '(31)' if female[
                                                                    i] == 31 else ''  # Signify when a 31 is inherited
                                    print(f'[IV {i}] Female {perfect_iv_text}')
                        else:
                            offspring[i] = random.randint(0, 31)
                            if interactive:
                                print(f'[IV {i}] RANDOM = ({offspring[i]})')
                    male_31s = male.count(31)
                    female_31s = female.count(31)
                    total_overall_31s = male_31s + female_31s
                    total_unique_31s = 0  # How many positionally-unique 31s between both parents?
                    for i in range(6):
                        if male[i] == 31 or female[i] == 31:
                            total_unique_31s += 1
                    offspring_31s = offspring.count(31)
                    if random.random() <= male_chance:  # Gender roll
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
                                    perfect_iv_text = '(31)' if female[
                                                                    i] == 31 else ''  # Signify when a 31 is inherited
                                    print(f'[IV {i}] Female {perfect_iv_text}')
                        else:
                            offspring[i] = random.randint(0, 31)
                            if interactive:
                                print(f'[IV {i}] RANDOM = ({offspring[i]})')
                    male_31s = male.count(31)
                    female_31s = female.count(31)
                    total_overall_31s = male_31s + female_31s
                    total_unique_31s = 0  # How many positionally-unique 31s between both parents?
                    for i in range(6):
                        if male[i] == 31 or female[i] == 31:
                            total_unique_31s += 1
                    offspring_31s = offspring.count(31)
                    if random.random() <= male_chance:  # Gender roll
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
            print(f'{male_31_ivs}IV + {female_31_ivs}IV ({upper_bound - overlap_number} overlaps)'
                  f'{"" if overall_tries_with_knot < overall_tries_without_knot else " (NO KNOT WINS)"}')
            print(f'Average tries to make progress with destiny knot: {overall_tries_with_knot / runs}')
            print(f'Average tries to make progress NO knot: {overall_tries_without_knot / runs}')
