import numpy as np
dayAoC = '05'
filename = 'day'+dayAoC+'_input.txt'

num_input_lines = 0
lst_x1 = []
lst_x2 = []
lst_y1 = []
lst_y2 = []

for line in open(filename):
	start,end = line.split('->')
	x1,y1 = start.split(',')
	x2,y2 = end.split(',')
	lst_x1.append(int(x1.strip()))
	lst_y1.append(int(y1.strip()))
	lst_x2.append(int(x2.strip()))
	lst_y2.append(int(y2.strip()))

max_coord_x = max(max(lst_x1), max(lst_x2))
max_coord_y = max(max(lst_y1), max(lst_y2))

vents1 = np.zeros((max_coord_y+1, max_coord_x+1), dtype=int)
vents2 = np.zeros((max_coord_y+1, max_coord_x+1), dtype=int)

dangerous_pos01 = 0		
dangerous_pos02 = 0		
for idx in range(len(lst_x1)):
	dx = lst_x2[idx]-lst_x1[idx]
	dy = lst_y2[idx]-lst_y1[idx]
	for i in range(1+max(abs(dx),abs(dy))):
		x = lst_x1[idx]+(1 if dx>0 else (-1 if dx<0 else 0))*i
		y = lst_y1[idx]+(1 if dy>0 else (-1 if dy<0 else 0))*i
		if dx==0 or dy==0:
			vents1[(y,x)] += 1
		vents2[(y,x)] += 1
		

		
dVents1 = vents1.flatten()
dVents2 = vents2.flatten()
for k in range(len(dVents1)):
	if dVents1[k] > 1:
		dangerous_pos01+=1
	if dVents2[k] > 1:
		dangerous_pos02+=1
		

print('Result part 01 :', dangerous_pos01)
print('Result part 02 :', dangerous_pos02)


