# Exercise 07_02 - Use the name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0 
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence"):
        continue
    ipos = line.find(":")
    xpos = float(line[ipos+1:])
    total = xpos + total
    count = count + 1
print("Average spam confidence: ", total/count)    