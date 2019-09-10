import math
list = [1,4,5,6,7,3,2,8,9,11,15,5,4] # len = 12
list.sort()
isEven = len(list) % 2 == 0

if isEven:
    a = int(len(list) / 2 - 1)
    b = a + 1
    print(str(list[a])+", "+str(list[b]))
else:
    a = int(math.floor(len(list) / 2))
    print(str(list[a]))
