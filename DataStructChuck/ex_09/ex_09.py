# Exercise 9_04 - Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages. The program
# looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps the sender's
# mail address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

""" fname = input("Enter file name: ")
if len(fname) < 1:
   fname = "mbox-short.txt"

handle = open(fname) """

handle = open("mbox-short.txt")
count = dict()
for line in handle:
    line = line.rstrip()
    if 'From ' in line:
        words = line.split()
        # print(words)
        for person in words:
            sender = words[1]
            # print(sender)
        count[sender] = count.get(sender, 0) + 1
        # print(sender)
print(count)
bigcount = None
bigsender = None
for k, v in count.items():
    if bigcount is None or v > bigcount:
        bigsender = k
        bigcount = v
print(bigsender, bigcount)
