# Creating
t = (1, 2, 3)
single = (5,)                       # the comma makes it a tuple
also = 1, 2, 3                      # parentheses are optional

# Immutability
# t[0] = 10                         # TypeError

# Unpacking
a, b, c = t
first, *middle, last = (1, 2, 3, 4, 5)
print(middle)                       # [2, 3, 4]

# Swapping values
x, y = 1, 2
x, y = y, x

# Returning multiple values
def min_max(values):
    return min(values), max(values)
lo, hi = min_max([4, 8, 1])

# Tuples as dictionary keys (lists can't be)
locations = {(13.08, 80.27): "Chennai", (12.97, 77.59): "Bengaluru"}

# Conversions
print(tuple([1, 2, 3]), list((1, 2, 3)))