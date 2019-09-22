from collections import defaultdict, namedtuple, Counter, deque

# Example 1: Named Tuples

User = namedtuple('User', 'name role')

user = User(name='Luke', role='bloke')

print(user.name)

print(user.role)

print(f'{user.name} is a {user.role}')


# Example 2: Default Dictionaries (defaultdict)

challenges_done = [('Luke', 10), ('Lola', 7), ('Walter', 5),
                   ('Hector', 3), ('Luke', 8), ('Lola', 4)]

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)


# Example 3: counter

words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
words[:5]

print(Counter(words).most_common(5))
