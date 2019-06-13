#JTKIM
#4/22/19
#problem 7

f = open("testText.txt", "r")

newF = open("newTestText.txt", "w")

counter = 1

for line in f:
    if counter % 2 != 0:
        newF.write(line)
    counter +=1

f.close()
newF.close()
