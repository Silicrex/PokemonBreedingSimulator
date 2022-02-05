import pylab
from helper_functions import *


# ---------- SETTINGS
target_ivs = 6  # 1-6, but it's pretty much a flat line unless you use 6
must_be_male = True  # Does the offspring have to be male?
runs = 10000
# Following settings are for what range of male ratios to use. 50-60 would be 50, 51, 52... 60
start_range = 40  # Inclusive range
end_range = 90  # Inclusive range
seed = None  # None = random, or can specify speed
# pylab.ylim(0, 200)  # BE CAREFUL ABOUT SCALE IF YOU ARE CHANGING TARGET_IVS TO ANYTHING LESS THAN 6

if seed is not None:
    random.seed(seed)

percents = [x/100 for x in list(range(start_range, end_range + 1))]  # List of percent values to iterate through
average_tries_per_percent = []
for male_chance in percents:
    total_tries_for_percent = 0
    for run in range(runs):
        # print(f'{male_chance} @ {run=}')
        # ---------- Starting progenitors (can set)
        male = [31, 31, 31, 31, 31, 31]
        female = [0, 0, 0, 0, 0, 0]

        offspring = [0, 0, 0, 0, 0, 0]
        offspring_gender = None

        tries = 0
        while True:
            if offspring.count(31) >= target_ivs:
                if not must_be_male:
                    break
                elif offspring_gender == 'male':
                    break
            tries += 1
            destiny_knot = check_for_destiny_knot(male, female)
            iv_slots = roll_inheritance(destiny_knot=destiny_knot)
            offspring = generate_offspring(male, female, iv_slots)
            offspring_gender = roll_gender(male_chance)
            if offspring_gender == 'male':
                if check_for_replace(male, female, offspring):
                    male = offspring.copy()
            else:
                if check_for_replace(female, male, offspring):
                    female = offspring.copy()
        total_tries_for_percent += tries
    average_tries_per_percent.append(total_tries_for_percent / runs)

# Generate a line of best fit for the data
best_fit_model = pylab.polyfit(percents, average_tries_per_percent, 2)
best_fit_y = list(pylab.polyval(best_fit_model, percents))  # Convert to list to use index()

# Prints
min_y = min(average_tries_per_percent)  # Value of lowest tries
min_x = percents[average_tries_per_percent.index(min_y)]  # Get corresponding x value to min y
min_best_fit_y = min(best_fit_y)
min_best_fit_x = percents[best_fit_y.index(min_best_fit_y)]

print(f'Observed optimal male chance: {min_x:.0%}')
if 0.5 in percents:  # For comparing to 50% male ratio
    even_ratio_index = percents.index(0.5)
    print(f'Average tries for 50% male ratio: {average_tries_per_percent[even_ratio_index]}')
print(f'Average tries for found optimal ({min_x:.0%}): {min_y}')
print(f'Line of best fit optimal ({min_best_fit_x:.0%}): {min_best_fit_y:.4f}')

# Plot the data
pylab.plot(percents, average_tries_per_percent, label='Simulation Results')
pylab.plot(percents, best_fit_y, label='Line of Best Fit')
gender_text = ' Male' if must_be_male else ''
pylab.title(f"Avg Tries For {target_ivs}IV{gender_text} By Gender Ratio (Lower = Better)")
pylab.xlabel("Decimal% Chance to Be Male")
pylab.ylabel("Average Tries")
pylab.legend(loc='best')
pylab.show()
