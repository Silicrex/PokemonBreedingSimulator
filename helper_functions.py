import random


# ------------------------------ IV slot inheritance

def apply_destiny_knot(iv_slots):  # Take iv_slots list, make copy, remove one random value
    iv_slots_copy = iv_slots.copy()
    iv_slots_copy.remove(random.choice(iv_slots_copy))
    return iv_slots_copy


def apply_normal_inheritance(iv_slots):  # Take iv_slots list, make copy, remove three random values
    iv_slots_copy = iv_slots.copy()
    for _ in range(3):
        iv_slots_copy.remove(random.choice(iv_slots_copy))
