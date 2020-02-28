from datetime import datetime
log_file=open("log1.csv", "w+")
log_file.write("Request_ID,Time,N,Result\n")
file=open("input.txt", "r+")
for j, each in enumerate(file):
	before_time=datetime.now()
	last_num=0
	n1=0
	n2=1
	fib="0|1"
	for i in range(2,int(each)):
		last_num=n1+n2
		n1=n2
		n2=last_num
		after_time=datetime.now()
		time_taken=after_time-before_time
		fib=fib+"|"+str(n2)
	print (fib)
	log_file.write(str(j)+","+str(time_taken)+","+str(each)+","+str(fib))
	log_file.write("\n")