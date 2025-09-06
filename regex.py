import re

page = ''
with open('page.html', 'r', encoding='utf-8') as f:
     page = f.read()

names = re.finditer(r'"title":"[A-Z]\w+\s([A-Z]\w+)"', page)
name_list = [name.group(1) for name in names]
# name_list = list(name_list)
d = {}
for sur in name_list:
     d[sur] = d.get(sur, 0) + 1

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print(sorted_dict)

# with open('surnames.txt', 'w', encoding='utf-8') as f:
#      for item in sorted_dict.items():
#           f.write(f'{item} \n')