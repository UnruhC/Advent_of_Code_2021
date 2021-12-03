import numpy as np

filename = 'day03_input.txt'

with open(filename) as f:
	measurements = f.read().split('\n')

dayAoC = '03'
		
numMeasurements = len(measurements)
bitsPerMeasurement = len(measurements[0])
print('\n\n--------------------------------------')
print('#-lines of input: ', numMeasurements)
print('#-bits per measurement: ', bitsPerMeasurement)
print('--------------------------------------')

# =======================================day03 part#1=====
gamma_rate = np.zeros((bitsPerMeasurement,), dtype=int)
epsilon_rate = np.zeros((bitsPerMeasurement,), dtype=int)
binarry_measurements = np.zeros((numMeasurements,bitsPerMeasurement), dtype=int)

lineCnt = 0
for singleMeasurement in measurements:
	for bitPos in range(bitsPerMeasurement):
		binarry_measurements[lineCnt, bitPos] = int(singleMeasurement[bitPos])
	lineCnt += 1

print('Sum over measurements ', np.sum(binarry_measurements, axis=0))

gamma_rate_tmp = np.sum(binarry_measurements, axis=0) > (numMeasurements/2)
epsilon_rate_tmp = np.sum(binarry_measurements, axis=0) <= (numMeasurements/2)

print('  Gamma-Rate : ', gamma_rate_tmp.astype(int))
print('Epsilon-Rate : ', epsilon_rate_tmp.astype(int))

g1 = gamma_rate_tmp.astype(int)
e1 = epsilon_rate_tmp.astype(int)

gamma_rate_int = g1.dot(2**np.arange(g1.size)[::-1])
epsilon_rate_int = e1.dot(2**np.arange(e1.size)[::-1])

print('Gamma-Rate Value   = ', gamma_rate_int)
print('Esplion-Rate Value = ', epsilon_rate_int)

print('\nResult day'+dayAoC+'-part#1= ', gamma_rate_int*epsilon_rate_int)
print('======================================\n')

# ======================================day03 part#2=====
oxygen_generator_rating = binarry_measurements
co2_scrubber_rating = binarry_measurements

for bitPos in range(bitsPerMeasurement):
	numCriteriaOxy = len(oxygen_generator_rating)
	criteria_oxy = np.sum(oxygen_generator_rating, axis=0) >= (numCriteriaOxy/2)
	lineCnt = 0
	lineIdx = []
	for nxtMeasurement in oxygen_generator_rating:
		if (nxtMeasurement[bitPos] == int(criteria_oxy[bitPos])):
			a = 0
		else:
			lineIdx.append(lineCnt)
		lineCnt += 1
	oxygen_generator_rating = np.delete( oxygen_generator_rating, lineIdx, axis=0)
print('Oxygen Generator Rating =', oxygen_generator_rating)
oxyGenRatingValue = oxygen_generator_rating.dot(2**np.arange(oxygen_generator_rating.size)[::-1])
print('     OxyGenRating Value = ', oxyGenRatingValue)

numCriteriaCO2 = len(co2_scrubber_rating)
criteria_co2 = np.sum(co2_scrubber_rating, axis=0) <= (numCriteriaCO2/2)

for bitPos in range(bitsPerMeasurement):
	numCriteriaCO2 = len(co2_scrubber_rating)
	criteria_co2 = np.sum(co2_scrubber_rating, axis=0) < (numCriteriaCO2/2)
	lineCnt = 0
	lineIdx = []
	if (numCriteriaCO2==1):
		break
	for nxtMeasurement in co2_scrubber_rating:
		if (nxtMeasurement[bitPos] == int(criteria_co2[bitPos])):
			a = 0
		else:
			lineIdx.append(lineCnt)
		lineCnt += 1
	co2_scrubber_rating = np.delete( co2_scrubber_rating, lineIdx, axis=0)
print('CO2 Scrubber Rating  =', co2_scrubber_rating)
co2ScrubRateValue = co2_scrubber_rating.dot(2**np.arange(co2_scrubber_rating.size)[::-1])
print('  CO2ScrubRate Value = ', co2ScrubRateValue)
print('\nResult day'+dayAoC+'-part#2= ', oxyGenRatingValue*co2ScrubRateValue)

