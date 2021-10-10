# Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull
# the hour out from the 'From ' line by finding the time and then splitting
# the string a second time using a colon. Once you have accumulated the counts
# for each hour, print out the counts, sorted by hour as shown below.

handle = open("mbox-short.txt")
#time = list()
list2 = list()
count = dict()
for line in handle:
    line = line.rstrip()
    if 'From ' in line:
        words = line.split()
        time = words[5]
        hour = time[:2]
        count[hour] = count.get(hour, 0) + 1
#print(count)

list2 = [(k, v) for k, v in count.items()]
#for k, v in count.items():
    #list2.append((k, v))

list2.sort()
print(list2)
for k, v in list2:
	print(k, v)
