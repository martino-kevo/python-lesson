# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")
print()

print(band)
print(band2)
print()

print(type(band))
print(len(band))
print()

# Accessing items in Dictionaries

print(band['vocals'])
print(band.get('vocals'))
print()

# List all keys in Dictionaries

print(band.keys())
print()

# List all values in Dictionaries

print(band.values())
print()

# List all key / value pairs as tuples in Dictionaries

print(band.items())
print()

# Verify a key exists in Dictionaries

print("guitar" in band)
print("triangle" in band)
print()

# Change values in Dictionaries

band['vocals'] = 'Coverdale'
band.update({'bass': 'JPJ'})

print(band)
print()

# Remove items from Dictionaries

print(band.pop('bass'))  # returns the value
print()

print(band)
print()

band['drums'] = 'Bonham'
print(band)
print()

print(band.popitem())  # returns a tuple
print()

print(band)
print()

# Delete and clear in Dictionaries

band['drums'] = 'Bonham'
del band['drums']
print(band)
print()

band2.clear()
print(band2)
print()

del band2

# Copy Dictionaries

# band2 = band  # creates a reference
# print("Bad copy!")
# print(band2)
# print(band)
# print()

# band2['drums'] = 'Dave'
# print(band)
# print()

band2 = band.copy()
band2['drums'] = 'Dave'
print("Good copy!")
print(band)
print(band2)
print()

# Copy using the dict() constructor function

band3 = dict(band)
print("Good copy!")
print(band3)
print()

# Nested Dictonaries

member1 = {
    'name': 'Dave',
    'instrument': 'vocals'
}
member2 = {
    'name': 'Sam',
    'instrument': 'guitar'
}
band = {
    'member1': member1,
    'member2': member2
}
print("Nested dict")
print(band)
print()

print(band['member1']['name'])
print()

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))
print()

# No duplicate allowed in a Set

nums = {1, 2, 2, 3}
print(nums)
print(len(nums))
print()

# True is duplicate of 1, False is a duplicate of 0

nums = {1, True, 2, False, 4, 3, 0}
print(nums)
print()

# Check if a value is in a Set

print(2 in nums)
print()

# but you cannot refer to a value in the Set with an index position or a key

# Add a new value to a Set

nums.add(8)
print(nums)
print()

# Add value from one Set to another

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
print()

# you can use update with lists, tuples and dictionaries too.


# Merge two Sets to create a new Set

one = {1, 2, 3}
two = {4, 5, 6}
my_new_set = one.union(two)
print(my_new_set)
print()

# keep only the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)
print()

# keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
print()
