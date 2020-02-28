import random

file=open("input.txt", "w")

each =1
while each<101:
	random_number=random.randint(8,20)
	file.write(str(random_number)+"\n")
	each+=1