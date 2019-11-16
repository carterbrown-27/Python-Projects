from SimpleGraphics import *

TEST_CASE = int(input("enter test case #: "))
list = []
biggest = 0
with open("case"+str(TEST_CASE)+".txt") as f:
    for line in f:
        new = []
        arr = line.strip().split("\t");
        for s in arr:
            new.append(int(s))
        list.append(new)
        # print(new)
        biggest = max(biggest, max(new))

h = 600 / len(list)
# w = 800 / len(list[0])
w = h

resize(w*len(list[0]),600)

y = 0
for l in list:
    x = 0
    for i in l:
        if i == 1 :
            setColor(0,255,0)
        elif i == biggest:
            setColor(255,0,0)
        else:
            sat = 255*(biggest-i)//biggest
            setColor(sat,sat,255)
        rect(w*x,h*y,w,h)
        x+=1
    y+=1

saveEPS("outputImg"+str(TEST_CASE)+".eps")
