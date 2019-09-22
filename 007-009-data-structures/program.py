#!python3

numlist = [1, 2, 3, 4, 5]

print(numlist)

# Output: [1, 2, 3, 4, 5]

numlist.reverse()
print(numlist)

# Expect: [5, 4, 3, 2, 1]

numlist.sort()
print(numlist)

# Expect: [1, 2, 3, 4, 5]

mystring = "luke"

for i in list(mystring):
    print(i)
# Expect: String 'luke' printed one character per line

l = list(mystring)
t = tuple(mystring)

print(l)
# Expect: ['l', 'u', 'k', 'e']

print(t)
# Expect: ('l', 'u', 'k', 'e')

l[0] = "n"

print(l)
# Expect: ['n', 'u', 'k', 'e']

# t[0] = "m"
# Expect Error: Traceback(most recent call last): File "<pyshell#59>", line 1, in < module > t[0] = "m"
# TypeError: 'tuple' object does not support item assignment

l.pop(1)
# Expect output
print(l)
# Expect: ['n', 'k', 'e']


l.insert(1, "i")
print(l)
# Expect: ['n', 'i', 'k', 'e']

del l[0]
# Expect no output to be returned (different to pop())
print(l)
# Expect: ['i', 'k', 'e']

l.insert(0, "b")
print(l)
# Expect: ['b', 'i', 'k', 'e']

l.append("s")
print(l)
# Expect: ['b', 'i', 'k', 'e', 's']

# DICTS:

household = {'luke': 35, 'lola': 35, 'walter': 4, 'hector': 1}

print(household)
# Expect dict to be printed

parents = {}
parents['luke'] = 35
print(parents)
# Expect {'luke': 35}

parents['lola'] = 35
print(parents)
# Expect {'luke': 35, 'lola': 35}

print(household.keys())
# Expect: dict_keys(['luke', 'lola', 'walter', 'hector'])

print(household.values())
# Expect; dict_values([35, 35, 4, 1])

print(household.items())
# Expect: dict_items([('luke', 35), ('lola', 35), ('walter', 4), ('hector', 1)])

for keys in household.keys():
    print(keys)
# Expect names printed one per line

for values in household.values():
    print(values)
# Expect ages printed one per line

for keys, values in household.items():
    print(keys + str(values))

# Expect names and ages printed with no spaces one pair per line

for keys, values in household.items():
    print('%s is %d years of age' % (keys, values))

# Better formatted output
