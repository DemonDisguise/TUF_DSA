# defaultdict
# dict subclass that calls a factory function to supply missing values

from collections import defaultdict

groups: defaultdict[str, list[str]] = defaultdict(list)

words = ["apple", "ant", "banana", "bat", "ball"]

for word in words:
    groups[word[0]].append(word)

print(groups)