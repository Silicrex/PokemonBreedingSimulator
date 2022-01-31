for male_31_ivs in range(7):  # Nested loop to get 0IV-0IV, 0IV-1IV, 0IV-2IV, etc without repeats (2IV-3IV == 3IV-2IV)
    print(f'Male = {male_31_ivs}IV')
    for female_31_ivs in range(male_31_ivs, 7):
        male = [0] * 6  # Start with 0IV
        for i in range(male_31_ivs):  # Fill in 31's according to current combination
            male[i] = 31
        female = [0] * 6
        for i in range(female_31_ivs):
            female[i] = 31
        total_31s = male_31_ivs + female_31_ivs
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
        for overlap_number in range(possible_overlaps):  # Loop goes from most to least overlaps
            if overlap_number != 0:  # Need to test first arrangement before we start shifting
                # Shift stats to the left (take first element, put it at the end; right shifting won't always work here)
                male.append(male.pop(0))
            print(f'{male_31_ivs}IV + {female_31_ivs}IV Overlaps: {upper_bound - overlap_number}')
            print(male, female)
    print()  # Newline
