import random

# ---------- SETTINGS
male_chance = 0.5
runs = 1000


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
            tries_with_knot = 0
            for _ in range(runs):
                offspring = [0, 0, 0, 0, 0, 0]

                while True:
                    tries_with_knot += 1
                    iv_slots = [0, 1, 2, 3, 4, 5]
                    iv_slots.remove(random.choice(iv_slots))  # Use destiny knot
                    for i in range(6):
                        if i in iv_slots:
                            if random.random() <= 0.5:  # Male draw
                                offspring[i] = male[i]
                            else:  # Female draw
                                offspring[i] = female[i]
                        else:
                            offspring[i] = random.randint(0, 31)
                    if random.random() <= male_chance:  # Gender roll
                        offspring_gender = 'male'
                        if offspring.count(31) > male.count(31):
                            break
                    else:
                        offspring_gender = 'female'
                        if offspring.count(31) > female.count(31):
                            break

            # Simulate without knot
            tries_without_knot = 0
            for _ in range(runs):
                offspring = [0, 0, 0, 0, 0, 0]

                while True:
                    tries_without_knot += 1
                    iv_slots = [0, 1, 2, 3, 4, 5]
                    for _ in range(3):  # Non-destiny knot, leave 3 fixed, 3 random
                        iv_slots.remove(random.choice(iv_slots))
                    for i in range(6):
                        if i in iv_slots:
                            if random.random() <= 0.5:  # Male draw
                                offspring[i] = male[i]
                            else:  # Female draw
                                offspring[i] = female[i]
                        else:
                            offspring[i] = random.randint(0, 31)
                    if random.random() <= male_chance:  # Gender roll
                        offspring_gender = 'male'
                        if offspring.count(31) > male.count(31):
                            break
                    else:
                        offspring_gender = 'female'
                        if offspring.count(31) > female.count(31):
                            break

            print(f'{male_31_ivs}IV + {female_31_ivs}IV ({upper_bound - overlap_number} overlaps)'
                  f'{"" if tries_with_knot < tries_without_knot else " (NO KNOT WINS)"}')
            print(f'Average tries to make progress with destiny knot: {tries_with_knot/runs}')
            print(f'Average tries to make progress NO knot: {tries_without_knot/runs}')
