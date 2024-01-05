#!/usr/bin/python3
prime = [1,2,3,5,7,11,13] # 13² = 169 and 17² = 289 > 250 we chose minimal prime deviders that their square is less than 250 

for x in range(14,251):
	check = True
	for d in [2,3,5,7,11,13]:
		if x % d == 0:
			check = False
		
	if check == True:
		prime.append(x)
print(prime)
print(len(prime))
with open("results.txt",'w') as f:
	for a in prime:
		f.write(str(a)+ " ")