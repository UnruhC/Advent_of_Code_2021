import numpy as np

filename = 'day02_input.txt'

with open(filename) as f:
#    depthValues = [
#		int(value) 
#		for value in f.read().split("\n")
#	]
	 driveCmds = f.read().split('\n')
# driveCmds = f.readlines().replace('\n','')

		
#print (driveCmds)
print('#-lines of input: ', len(driveCmds))

# =======================================day02 part#1=====
horizontal = 0
depth = 0
aim = 0

for idx in range(len(driveCmds)):
	
	(nxtDir, nxtSteps) = driveCmds[idx].split(' ')
		
	if (nxtDir == 'forward'): horizontal +=int(nxtSteps)
	elif (nxtDir == 'up'): depth -= int(nxtSteps)
	elif (nxtDir == 'down'): depth += int(nxtSteps)
	else: print ('Command not known')

  #print("Direction: ", nxtDir)
print('Submarine at position =', horizontal)
print('Submarine at depth =', depth)  
print('\nResult day02-part#1= ', horizontal*depth)


# =======================================day02 part#2=====
horizontal = 0
depth = 0
aim = 0

for idx in range(len(driveCmds)):
	
	(nxtDir, nxtSteps) = driveCmds[idx].split(' ')
		
	if (nxtDir == 'forward'): 
		horizontal +=int(nxtSteps)
		depth += (int(nxtSteps)*aim)
	elif (nxtDir == 'up'): aim -= int(nxtSteps)
	elif (nxtDir == 'down'): aim += int(nxtSteps)
	else: print ('Command not known')

  #print("Direction: ", nxtDir)
print('Submarine at position =', horizontal)
print('Submarine aims at =', aim)
print('Submarine at depth =', depth)  
print('\nResult day02-part#2= ', horizontal*depth)


