#dictionary is unordered , mutable and allows duplicates

my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

#accessing elements

name_in_dict = my_dict["name"]
print(name_in_dict)

#adding the item

my_dict["email"] = "max@xyz.com"
print(my_dict)

#changeing the item
my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

#deleting the item

del my_dict["email"]

print("popped value:", my_dict.pop("age"))

print("popped item:", my_dict.popitem())

my_dict = {"name":"Max", "age":28, "city":"New York"}

#checking for keys

# use if in
if "name" in my_dict:
    print(my_dict["name"])

# using try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")  


# loop over keys
for key in my_dict:
    print(key, my_dict[key])

# loop over keys
for key in my_dict.keys():
    print(key)

# loop over values
for value in my_dict.values():
    print(value)

# loop over keys and values
for key, value in my_dict.items():
    print(key, value)

#coping dictionary

dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org

dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)# affects the original

dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()
# dict_copy = dict(dict_org)

dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

#merging two dictionary

my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# nested dictionary

my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
nested_dict = {"dictA": my_dict_1, "dictB": my_dict_2}
print(nested_dict)