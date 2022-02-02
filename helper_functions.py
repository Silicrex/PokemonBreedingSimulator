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
