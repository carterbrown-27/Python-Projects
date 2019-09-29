n = 100
d = len(str(n)) # number of digits in number
lb = 9 * (d-1) * 10 ** (d-2) # lower bound, e.g 15 --> 9, 101 --> 180
print(lb)
print(str(lb + (n-lb)/d)[1 if ((n-lb) % d == 0) else 0]) # math!
