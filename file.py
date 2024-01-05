#!/usr/bin/python3
prime = [1,2,3,5,7]

for x in range(8,251):
	check = True
	for d in [2,3,5,7]:
		if x % d == 0:
			check = False
		
	if check == True:
		prime.append(x)
print(prime)
#print(len(prime))
with open("results.txt",'w') as f:
	for a in prime:
		f.write(str(a)+ " ")