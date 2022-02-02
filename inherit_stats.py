from helper_functions import *
runs = 100000

specific_stats = 3  # Chance of how many specific stats being inherited? Range of 1 through number of IVs inherited
destiny_knot = False  # True or False toggle

stats_included = 0  # Number of times successful
for _ in range(runs):
    iv_slots = [0, 1, 2, 3, 4, 5]
    iv_slots = roll_inheritance(iv_slots, destiny_knot)
    # Arbitrarily use first 'specific_stats' stats as target
    # Check if that set is a subset of the IV slots we're left with
    if set(range(specific_stats)).issubset(set(iv_slots)):
        stats_included += 1

result = stats_included / runs  # Approximation based on avg
print(f'Avg % of times specific {specific_stats} inherited: {stats_included / runs:.4%}\n'
      f'Avg % of times not: {(runs - stats_included) / runs:.4%}')
