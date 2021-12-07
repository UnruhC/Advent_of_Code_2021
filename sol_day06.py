import numpy as np
dayAoC = '06'
filename = 'day'+dayAoC+'_input.txt'

fish = list(map(int, open(filename).readline().split(",")))

# Initialize Age-Histogram
ages_distribution = [0] * 9

# Initialize Age-Histogram with the Input
for f in fish:
    ages_distribution[f] += 1

for day in range(256):
    old_ages = ages_distribution
	# Roll distribution to the left (reflects the decrease of days by one)
    ages_distribution = ages_distribution[1:] + [0]
    ages_distribution[6] += old_ages[0] # Fish that is capable to bear a new one
    ages_distribution[8] += old_ages[0] # Newborn fishs
    if day == 79:
        print("Part 1:", sum(ages_distribution))
print("Part 2:", sum(ages_distribution))


