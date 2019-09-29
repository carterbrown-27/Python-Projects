# returns true if two strings share a letter
def sharesLetter(s1, s2):
    for c in s1:
        if c in s2: return True
    return False

list = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef","axzzz"]
maxProduct = 0
# check each string against each other string (not optimized & including self, cuz i'm too lazy 2 write non-complex for loops)
for s1 in list:
    for s2 in list:
        if not sharesLetter(s1,s2): maxProduct = max(len(s1)*len(s2), maxProduct)
print(maxProduct)
