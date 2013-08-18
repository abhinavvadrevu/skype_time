def get_times(str):
	p = len(str)
	i=0
	out = [] #append items of form [date, duration]
	while i<p:
		if str[i:i+8] == "duration":
			k = i
			while str[k] != '*':
				k+=1
			while str[k] != ' ':
				k-=1
			k -= 1
			duration = ''
			while str[k] != ' ':
				if str[k] != '.':
					duration = str[k] + duration
				k -=1
			print(duration)
			k = i
			while str[k] != '[':
				k -= 1
			date = ''
			while str[k] !=']':
				date += str[k]
				k+=1
			date +=']'
			out.append([date,duration])
		i += 1
	return out

def get_date(dateinp):
	k = 1
	out = ''
	print(dateinp)
	while dateinp[k] != " ":
		print(dateinp[k])
		out += dateinp[k]
		k += 1
	return out

def get_time(inp):
	i = 0
	curpart = ''
	time=[]
	while i<len(inp):
		if (inp[i]) == ":":
			curpart = int(curpart)
			time.append(curpart)
			curpart=''
			i +=1
		curpart += inp[i]
		i+=1
	curpart = int(curpart)
	time.append(curpart)
	while len(time) != 3:
		time = [0] + time
	return time

	
i = open("skypedad.txt",'r')
j = i.read()
i.close()

k = get_times(str(j))

l = open("out","w")
output={}
for x in k:
	#l.write("date:")
	l.write(get_date(str(x[0])))
	l.write("\n")
	#l.write("duration: ")
	#print(get_time(x[1]))
	l.write(x[1])
	l.write("\n")
l.close()

m = open("out","r")
datetimelist = m.readlines()
m.close()
for x in range(len(datetimelist)):
	#print(x)
	datetimelist[x] = str(datetimelist[x])[:-1]
#print(datetimelist)


output = {}
for x in range(len(datetimelist)):
	if x%2 ==0:
		total = [0,0,0]
		time = datetimelist[x+1]
		if output.has_key(datetimelist[x]):
			parsedtime = get_time(time)
			#print(parsedtime)
			total = output[datetimelist[x]]
			for y in range(len(parsedtime)):
				total[y] += parsedtime[y]
			output[datetimelist[x]] = total
		else:
			total = get_time(time)
			output[datetimelist[x]] = total

print(output)


def fixtimeformat(time):
	s = time[2]
	m = time[1]
	h = time[0]
	news = s%60
	m += (s-s%60)/60
	newm = m%60
	h += (m-m%60)/60
	return [h,newm,news]

for x in range(len(datetimelist)):
	if x%2 ==0:
		key = datetimelist[x]
		time = output[key]
		value = fixtimeformat(time)
		output[key] = value
print("NEWONE")
print(output)


#FIND OUT AVERAGE TIME
totaltime = [0,0,0]
for x in range(len(datetimelist)):
	if x%2 ==0:
		key = datetimelist[x]
		value = output[key]
		totaltime[0] += value[0]
		totaltime[1] += value[1]
		totaltime[2] += value[2]


print("total time:")
totaltime = fixtimeformat(totaltime)
print(totaltime)
print("total days:")
totaldays = len(datetimelist)/2
print(totaldays)




print("average time per day:")

totalsecs = totaltime[0]*3600 + totaltime[1]*60 + totaltime[2]
avesecs = totalsecs/float(totaldays)
hours = avesecs//3600
mins = (avesecs - (hours)*3600)//60
secs = avesecs - (hours)*3600 - (mins*60)



print(str(hours) + " hours, " + str(mins) + " mins, and "+str(secs) + " seconds")
