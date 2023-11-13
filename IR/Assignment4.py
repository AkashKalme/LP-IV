#                       Assignment No.: 4
# Write a map-reduce program to count the number of occurrences of each alphabetic character in the given dataset.
# The count for each letter should be case-insensitive.
# (i.e., include both upper-case and lower-case versions of the letter; Ignore non-alphabetic characters).
from collections import Counter

# Sample input data
data = [
    "apple banana cherry",
    "date elderberry fig",
    "grape honeydew",
]

# Mapper function


def mapper(text):
    counts = Counter(text.replace(" ", ""))
    for letter, count in counts.items():
        yield (letter, count)

# Reducer function


def reducer(mapped_data):
    letter_counts = {}
    for letter, count in mapped_data:
        if letter in letter_counts:
            letter_counts[letter] += count
        else:
            letter_counts[letter] = count
    return letter_counts


# Map phase
mapped_data = []
for line in data:
    for result in mapper(line):
        mapped_data.append(result)

# Reduce phase
reduced_data = reducer(mapped_data)

# Display the result
for letter, count in reduced_data.items():
    print(f"{letter}: {count}")
