def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates

def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

def get_value(pair):
    return pair[1]

def sort_by_value(data):
    sorted_pairs = sorted(data.items(), key=get_value)
    return dict(sorted_pairs)

def two_sums(numbers, target):
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        seen[number] = index
    return []