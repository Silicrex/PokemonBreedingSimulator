import random


# ------------------------------ IV slot inheritance

def roll_inheritance(iv_slots, destiny_knot=False):  # Take iv_slots list, return new list
    iv_slots_copy = iv_slots.copy()
    if destiny_knot:
        iv_slots_copy.remove(random.choice(iv_slots_copy))
    else:
        for _ in range(3):
            iv_slots_copy.remove(random.choice(iv_slots_copy))
    return iv_slots_copy


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
