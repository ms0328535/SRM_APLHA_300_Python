fruits = ["apple", "banana", "cherry", "date"]

# Indexing and slicing
print(fruits[0], fruits[-1])        # first, last
print(fruits[1:3])                  # ['banana', 'cherry']
print(fruits[::-1])                 # reversed copy
print(fruits[::2])                  # every 2nd item

# Adding and removing
fruits.insert(1, "mango")           # insert at index
fruits.extend(["kiwi", "lime"])     # add many
fruits.remove("banana")             # remove by value
last = fruits.pop()                 # remove and return last
del fruits[0]                       # remove by index

# Searching and counting
print("kiwi" in fruits)
print(fruits.index("cherry"))
print([1, 2, 2, 3].count(2))

# Sorting
nums = [4, 1, 7, 3]
print(sorted(nums, reverse=True))   # new list, original unchanged
words = ["pear", "fig", "banana"]
words.sort(key=len)                 # sort by length

# Comprehensions with conditions
evens = [n for n in range(20) if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# Useful built-ins
print(sum(nums), min(nums), max(nums), len(nums))
for i, f in enumerate(words, start=1):
    print(i, f)
for a, b in zip([1, 2, 3], ["x", "y", "z"]):
    print(a, b)

# Copy pitfall
a = [1, 2, 3]
b = a            # same list, not a copy!
b.append(4)
print(a)         # [1, 2, 3, 4]
c = a.copy()     # real (shallow) copy