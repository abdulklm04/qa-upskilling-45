from collection_utils import sum_list, find_duplicates, group_by_length, sort_by_value, two_sums

print(sum_list([1, 2, 3, 4]))
print(sum_list([]))
print(sum_list([-5, 5, 10]))

print(find_duplicates([1, 2, 2, 3, 3, 3]))
print(find_duplicates([1, 2, 3 ]))
print(find_duplicates([]))
print(find_duplicates(["a", "b", "a"]))

print(group_by_length(["a", "bb", "cc", "d"]))
print(group_by_length(["hello", "world", "hi"]))
print(group_by_length([]))

print(sort_by_value({"Ravi": 80, "Anu": 95, "Kiran": 70}))
print(sort_by_value({"a": 3, "b": 1, "c": 2}))
print(sort_by_value({}))

print(two_sums([2, 7, 11, 15], 9))
print(two_sums([3, 2, 4], 6))
print(two_sums([3, 3], 6))
print(two_sums([1, 2, 3], 10))
print(two_sums([], 5))