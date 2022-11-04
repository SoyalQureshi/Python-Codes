import re
mystr = '''this is
           the multiline
           string'''
pattern = re.compile(r'string')
matches = pattern.finditer(mystr)
for match in matches:
    print(match)

else:
    print("no match")
