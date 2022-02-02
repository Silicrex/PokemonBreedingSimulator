import random
import math

# Some Pokemon in the game are fixed to have at least three 31s. What's the chance you get the three you want?
# (It's the same as inheriting 3 stats without Destiny Knot)
# Also I see now this is just a 6-choose-3 combinations problem

# By simulation
runs = 100000
count = 0
for _ in range(runs):
    iv_slots = [0, 1, 2, 3, 4, 5]
    for _ in range(3):
        iv_slots.remove(random.choice(iv_slots))
    if set(range(3)).issubset(set(iv_slots)):
        count += 1
print(f'{count/runs:.3%}')

# By combinations (direct)
combinations = math.factorial(6)/(math.factorial(3) * math.factorial(6 - 3))
print(f'1/{combinations} ({1/combinations:.2%})')
