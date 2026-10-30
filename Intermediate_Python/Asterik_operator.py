# 1. Multiplication and power
print(3 * 4, 2 ** 5)

# 2. Repeating sequences
print([0] * 5, "ab" * 3, (1, 2) * 2)

# 3. *args / **kwargs (see above)

# 4. Keyword-only marker
def f(a, *, b): ...

# 5. Unpacking iterables
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first, middle, last)

# 6. Merging containers
a, b = [1, 2], (3, 4)
merged = [*a, *b, 5]
d1, d2 = {"x": 1}, {"y": 2}
merged_d = {**d1, **d2}

# 7. Unpacking into function calls
print(*nums, sep=" | ")
values = (1, 2, 3)
print(max(*values))

# 8. Transposing with zip
matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))     # [(1, 4), (2, 5), (3, 6)]

# 9. Unpacking ranges and strings
print([*range(5)], [*"abc"])