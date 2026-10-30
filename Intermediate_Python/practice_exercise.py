# 1. Find common items between two lists
l1, l2 = [1, 2, 3, 4], [3, 4, 5]
print(list(set(l1) & set(l2)))

# 2. Group words by first letter
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = {}
for w in words:
    groups.setdefault(w[0], []).append(w)
print(groups)

# 3. Find the most frequent item
data = [1, 3, 2, 3, 3, 1]
print(max(set(data), key=data.count))

# 4. Invert a dictionary
original = {"a": 1, "b": 2}
print({v: k for k, v in original.items()})