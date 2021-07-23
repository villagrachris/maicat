str1 = 'asfhasdjasfkj'
str2 = 'fajhasfjkasjd'

output = ''
for index, char in enumerate(min(str1, str2)):
  output += '1' if str1[index] == str2[index] else '0'

print(output)