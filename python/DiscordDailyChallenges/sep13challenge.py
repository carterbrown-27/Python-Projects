import re
str = "python"
pattern = "*th?n"

pattern = pattern.replace("*",r"[\S\s]*")
pattern = pattern.replace("?",r"[\S\s]")

pattern = re.compile("^" + pattern + "$")
print(re.search(pattern,str) is not None);
