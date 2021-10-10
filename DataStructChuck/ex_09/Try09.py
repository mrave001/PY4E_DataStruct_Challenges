handle = open("mbox-short.txt")
count = dict()
for line in handle:
    if 'From ' in line:
        words = line.split()
        #print(words)
        for item in words:
            sender = words[1]
        #print(sender)
        count[sender] = count.get(sender, 0) + 1
        #print(count[sender])
        
print(count)

#c = {'a':3, 'randal':56, 'miguel':31}
HiToLo = sorted([(v, k) for k, v in count.items()], reverse=True)
print(HiToLo[:4])
""" tmp = list()
for k,v in count.items():
    tmp.append((v,k))
#print(tmp)
HiToLo = sorted(tmp, reverse=True)
print(HiToLo)
for v,k in HiToLo[:4]:
    print(k,v)  """
