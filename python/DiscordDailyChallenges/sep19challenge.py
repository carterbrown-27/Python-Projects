import  math
n = 189

refPoint = 0
lastRefPoint = 0
d = 0
while n >= refPoint: # find a 999...999 ref point
    lastRefPoint = refPoint
    d += 1
    refPoint += (9 * d * 10 ** (d-1))

l = n - lastRefPoint # leftover digits

num = str((10 ** (d-1) - 1)  + (math.ceil(l/d)))
print(num[((d if l>0 else d-1) if l % d == 0 else l % d) - 1])
