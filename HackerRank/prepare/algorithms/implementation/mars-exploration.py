# https://www.hackerrank.com/challenges/mars-exploration/
string = input()
count = 0
for i in range(0,len(string),3):
    if string[i] != "S":
        count +=1
    if string[i+1] != "O":
        count +=1
    if string[i+2] != "S":
        count+=1
print(count)
