import random


# ------------------------------ IV slot inheritance

def roll_inheritance(destiny_knot=False):  # For determining which IVs to inherit, numbers are slot numbers
    iv_slots = [0, 1, 2, 3, 4, 5]
    if destiny_knot:  # Remove 1
        iv_slots.remove(random.choice(iv_slots))
    else:  # Remove 3
        for _ in range(3):
            iv_slots.remove(random.choice(iv_slots))
    return iv_slots


# ------------------------------ Optimal breeding strategies

def check_for_destiny_knot(male, female):  # Return True if knot would be optimal
    male_31s = male.count(31)
    female_31s = female.count(31)
    if male_31s == 6 or female_31s == 6:  # Knot always optimal if either parent is a 6IV
        return True
    total_overall_31s = male_31s + female_31s
    total_unique_31s = 0  # How many positionally-unique 31s between both parents?
    for i in range(6):
        if male[i] == 31 or female[i] == 31:
            total_unique_31s += 1
    if total_unique_31s == total_overall_31s / 2:  # When unique 31s is half of overall, means all are overlaps
        return False
    else:
        return True


# ------------------------------ Apply IVs

def generate_offspring(male, female, iv_slots, interactive=False):
    offspring = [0, 0, 0, 0, 0, 0]
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
        else:  # IV taken out of the inherited pool, so roll
            offspring[i] = random.randint(0, 31)
            if interactive:
                print(f'[IV {i}] RANDOM = ({offspring[i]})')
    return offspring


def roll_gender(male_chance):
    if random.random() <= male_chance:  # Gender roll
        return 'male'
    else:
        return 'female'


def check_for_replace(same_gender, other_gender, offspring, interactive=False):
    same_gender_ivs = same_gender.count(31)
    other_gender_ivs = other_gender.count(31)
    offspring_31s = offspring.count(31)
    total_unique_31s = 0
    new_total_unique_31s = 0  # How many unique 31s would we have if we did a replacement?
    for i in range(6):
        if same_gender[i] == 31 or other_gender[i] == 31:
            total_unique_31s += 1
        if offspring[i] == 31 or other_gender[i] == 31:
            new_total_unique_31s += 1
    # It's not worth replacing in the case where you get more overall 31s but less unique 31s
    beats_unique_31s = new_total_unique_31s > total_unique_31s
    if interactive:
        print(f'{new_total_unique_31s=}')
        print(f'{total_unique_31s=}')
        if beats_unique_31s:
            print(f"Beats unique 31s! ({total_unique_31s} to {new_total_unique_31s})")
            print(f"Overall 31s goes from {same_gender_ivs + other_gender_ivs} to {offspring_31s + other_gender_ivs}")
        if offspring_31s > same_gender_ivs:
            if new_total_unique_31s >= total_unique_31s:
                print('Offspring has more 31s and unique is at least as good')
            else:
                print('Offspring has more 31s but unique would be lower')
    if beats_unique_31s or offspring_31s > same_gender_ivs and new_total_unique_31s >= total_unique_31s:
        return True
    else:
        return False
