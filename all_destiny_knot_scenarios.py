from helper_functions import *

# ---------- SETTINGS
prioritize_uniques = True  # Care more about progress towards 6IV pool than current IV count
male_chance = 0.5
runs = 1000
seed = 123  # None or seed. If seed given, will do both tests in each iteration using the same seed
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

            tries_with_knot = 0
            tries_without_knot = 0
            for iteration in range(2):  # Do one run with destiny knot, then one without
                if seed is not None:
                    random.seed(seed)
                for _ in range(runs):
                    while True:
                        if iteration == 0:  # First iteration, do with knot
                            tries_with_knot += 1
                            iv_slots = roll_inheritance(destiny_knot=True)
                        else:  # Second iteration, do without knot
                            tries_without_knot += 1
                            iv_slots = roll_inheritance()
                        offspring = generate_offspring(male, female, iv_slots)
                        if roll_gender(male_chance) == 'male':
                            if not prioritize_uniques and offspring.count(31) > male.count(31):
                                break
                            elif prioritize_uniques and check_for_replace(male, female, offspring):
                                break
                        else:
                            if not prioritize_uniques and offspring.count(31) > female.count(31):
                                break
                            elif prioritize_uniques and check_for_replace(female, male, offspring):
                                break

            print(f'{male_31_ivs}IV + {female_31_ivs}IV ({upper_bound - overlap_number} overlaps)'
                  f'{"" if tries_with_knot < tries_without_knot else " (NO KNOT WINS)"}')
            print(f'Average tries to make progress with destiny knot: {tries_with_knot/runs}')
            print(f'Average tries to make progress NO knot: {tries_without_knot/runs}')
