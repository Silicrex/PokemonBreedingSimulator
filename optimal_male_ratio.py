import random
import pylab


# ---------- SETTINGS
runs = 100
start_range = 20  # Inclusive range
end_range = 90  # Inclusive range

percents = [x/100 for x in list(range(start_range, end_range + 1))]  # List of percent values to iterate through
average_tries_per_percent = []
for male_chance in percents:
    total_tries_for_percent = 0
    for run in range(runs):
        # print(f'{male_chance} @ {run=}')
        male = [31, 31, 31, 31, 31, 31]
        female = [0, 0, 0, 0, 0, 0]

        offspring = [0, 0, 0, 0, 0, 0]
        offspring_gender = None

        tries = 0
        while not (offspring.count(31) == 6 and offspring_gender == 'male'):
        # while not (offspring.count(31) == 6):
            tries += 1
            iv_slots = [0, 1, 2, 3, 4, 5]
            iv_slots.remove(random.choice(iv_slots))
            for i in range(6):
                if i in iv_slots:
                    if random.random() <= 0.5:  # Male draw
                        offspring[i] = male[i]
                    else:  # Female draw
                        offspring[i] = female[i]
                else:
                    offspring[i] = random.randint(0, 31)
            if random.random() <= male_chance:  # Gender roll
                offspring_gender = 'male'
                if offspring.count(31) > male.count(31):
                    male = offspring.copy()
            else:
                offspring_gender = 'female'
                if offspring.count(31) > female.count(31):
                    female = offspring.copy()
        total_tries_for_percent += tries
    average_tries_per_percent.append(total_tries_for_percent / runs)
# print(average_tries_per_percent)
min_value = min(average_tries_per_percent)
min_value_index = average_tries_per_percent.index(min_value)
print(f'Optimal male chance: {percents[min_value_index] * 100}%')
if 0.5 in percents:
    percent_index = percents.index(0.5)
    print(f'Average tries for 50-50: {average_tries_per_percent[percent_index]}')
    print(f'Average tries for found optimal: {average_tries_per_percent[min_value_index]}')
pylab.plot(percents, average_tries_per_percent)
pylab.title("Avg Tries For 6IV Male By Gender Ratio")
pylab.xlabel("decimal% chance to be male")
pylab.ylabel("Average tries (lower = better)")
pylab.show()
