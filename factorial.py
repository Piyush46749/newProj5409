from datetime import datetime
import time
file=open("input.txt", "r+")
log_file=open("log.csv", "w+")
log_file.write("Request_ID, Time, N, Result \n")
for i, each in enumerate(file):
	before_time=datetime.now()
	fact=1
	num=each.replace("\n", "")
	for j in range(1,int(num)+1):
		fact=fact*j
		after_time=datetime.now()
	time_taken=after_time-before_time
	log_file.write(str(i)+","+str(time_taken)+","+str(num)+","+str(fact)+"\n")
	print(fact)