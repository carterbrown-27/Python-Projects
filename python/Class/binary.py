str = ""
p = 1

num = int(input("enter a number:"))
while True:
    if num % (p*2) > 0:
        str = "1" + str
        num -= p
    else:
        str = "0" + str
    p *= 2
    if p > num: break

str =  "0b" + str
print(str)
