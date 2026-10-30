person = {"name": "Priya", "age": 25}

# Safe access
print(person.get("city"))               # None, no error
print(person.get("city", "Unknown"))    # default value

# Adding, updating, removing
person["city"] = "Chennai"
person.update({"age": 26, "job": "Dev"})
person.pop("job")
del person["age"]

# Looping
for key in person: print(key)
for value in person.values(): print(value)
for key, value in person.items(): print(key, value)

# Dictionary comprehension
squares = {n: n**2 for n in range(5)}
flipped = {v: k for k, v in squares.items()}

# Merging
d1, d2 = {"a": 1}, {"b": 2}
merged = {**d1, **d2}
merged2 = d1 | d2                       # Python 3.9+

# Counting words
text = "the cat and the hat and the bat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)

# Sorting by value
ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

# Nested dictionaries
students = {
    "Asha": {"math": 90, "sci": 85},
    "Ravi": {"math": 70, "sci": 95},
}
print(students["Asha"]["math"])