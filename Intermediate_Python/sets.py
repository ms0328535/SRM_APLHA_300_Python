s = {1, 2, 3}
s.add(4)
s.update([5, 6])
s.discard(10)                       # no error if missing
# s.remove(10)                      # KeyError if missing

# Removing duplicates
print(set([1, 2, 2, 3, 3, 3]))                  # {1, 2, 3}
unique_ordered = list(dict.fromkeys([3, 1, 3, 2, 1]))   # keeps order

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)        # union
print(a & b)        # intersection
print(a - b)        # difference (in a, not b)
print(a ^ b)        # symmetric difference

# Subset checks
print({1, 2} <= a)          # subset
print(a.isdisjoint({9}))    # no common items

# Fast membership test
allowed = {"admin", "editor"}
print("admin" in allowed)

# Set comprehension
print({c.lower() for c in "HelloWorld" if c.isalpha()})

# Immutable set
fs = frozenset([1, 2, 3])