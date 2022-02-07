import random


def check_for_destiny_knot(male, female, prioritize_uniques=True):  # Return True if knot would be optimal
    male_31s = male.count(31)
    female_31s = female.count(31)
    if male_31s == 6 or female_31s == 6:  # Knot always optimal if either parent is a 6IV
        return True
    total_overall_31s = male_31s + female_31s
    total_unique_31s = 0  # How many positionally-unique 31s between both parents?
    for i in range(6):
        if male[i] == 31 or female[i] == 31:
            total_unique_31s += 1
    if prioritize_uniques:
        if total_unique_31s == total_overall_31s / 2:  # When unique 31s is half of overall, means all are overlaps
            return False
        else:
            return True
    else:  # Prioritizing overall 31s
        if total_overall_31s == 0 or total_overall_31s == 2 and total_unique_31s == 1:  # 0IV/0IV, 1IV/1IV same pos
            return False
        else:
            return True


def check_for_power_item(male, female):
    power_item_data = None  # Will stay None if all IVs are 31s or if none are
    for i in range(6):
        if male[i] == 31 and female[i] != 31:  # Power item optimal when one parent has 31 in spot other doesn't
            power_item_data = {'slot': i, 'parent': 'male'}
            break
        elif male[i] != 31 and female[i] == 31:
            power_item_data = {'slot': i, 'parent': 'female'}
            break
    return power_item_data


# For determining which IVs to inherit, numbers are slot numbers
def roll_inheritance(destiny_knot=False, power_item_data=None):  # power_item would be an int for slot 0-5
    iv_slots = [0, 1, 2, 3, 4, 5]
    if destiny_knot:  # Remove 1
        iv_slots.remove(random.choice(iv_slots))
    else:  # Remove 3
        for _ in range(3):
            iv_slots.remove(random.choice(iv_slots))
    if power_item_data is not None:  # power_item_data will be {'slot': slot, 'parent': parent}
        power_slot = power_item_data['slot']
        if power_slot not in iv_slots:  # If the power item slot didn't happen to be rolled already
            iv_slots.remove(random.choice(iv_slots))  # Take a random IV out, replace it with the power item IV
            iv_slots.append(power_slot)
            iv_slots.sort()
    return iv_slots


def generate_offspring(male, female, iv_slots, power_item_data=None, interactive=False):
    offspring = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        if i in iv_slots:  # For the positions left in the pool for inheritance
            if power_item_data and i == power_item_data['slot']:
                # power_item_data will be {'slot': slot, 'parent': parent}
                inherit_from_male = True if power_item_data['parent'] == 'male' else False
            else:
                inherit_from_male = random.random() <= 0.5
            if inherit_from_male:  # Inherit IV at this position from male
                offspring[i] = male[i]
                if interactive:
                    perfect_iv_text = ' (31)' if male[i] == 31 else ''  # Signify when a 31 is inherited
                    print(f'[IV {i}] Male{perfect_iv_text}')
            else:  # Inherit IV at this position from female
                offspring[i] = female[i]
                if interactive:
                    perfect_iv_text = '(31)' if female[i] == 31 else ''  # Signify when a 31 is inherited
                    print(f'[IV {i}] Female {perfect_iv_text}')
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


def check_for_replace(same_gender, other_gender, offspring, prioritize_overalls=False, interactive=False):
    same_gender_31s = same_gender.count(31)
    other_gender_31s = other_gender.count(31)
    offspring_31s = offspring.count(31)

    if prioritize_overalls:
        if offspring_31s > same_gender_31s:
            return True
        else:
            return False

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
            print(f"Overall 31s goes from {same_gender_31s + other_gender_31s} to {offspring_31s + other_gender_31s}")
        if offspring_31s > same_gender_31s:
            if new_total_unique_31s >= total_unique_31s:
                print('Offspring has more 31s and unique is at least as good')
            else:
                print('Offspring has more 31s but unique would be lower')
    if beats_unique_31s or offspring_31s > same_gender_31s and new_total_unique_31s >= total_unique_31s:
        return True
    else:
        return False
