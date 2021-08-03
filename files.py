# reading and processing files

# specifying the file to open
fh = open("Crime and Punishment.txt","r")

# reads the contents of the file line by line into a list called lines, counting the number of lines read
count = 0
lines = []
for line in fh:
    lines.append(line)
    count = count + 1
# closing the file
fh.close()

# compare count with length from len() function (identical)
print(len(lines))
print(count)

# calculates average length of a line
total = 0
for line in lines:
    total = total + len(line)
avg_length = total/count
print(avg_length)

# creates a list of all of the words in the file
words = []
for line in lines:
    lwords = line.split()
    for word in lwords:
        words.append(word)
# print first 100 words
for i in range(100):
    print(words[i])
# length of the list
len(words)

# counts the number of occurrences of a word in the list of words
# case sensitive!
count = 0
for word in words:
    if word.lower() == "is":
        count = count + 1
print("Number of 'is'",count)
