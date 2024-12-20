s = 'I love women so much'
# f = 'I Love Women So Much'

s = s.find('e')

print()
print(s)

# Solving dictionary changed size during iteration

d = {'l': [], 'm': [1, 2, 3], 'n': []}

while True:
    for x in d.keys():
        if d[x] == []:
            del d[x]
            break

    if [] in d.values():
        continue
    else:
        break

print(d)

# Solving set changed size during iteration

s = {1, 2, 3}

while True:
    for x in s:
        s.pop()
        break

    if len(s) > 1:
        continue
    else:
        break

print(s)

l = ['10', '28', '2024', '43', '28']

print(l.index('28'))

# for x in l:
#     l.remove(x)
#     del l[l.index(x)]

# print(l)

y_set = set((l))

print(y_set)
