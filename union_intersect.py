
list1 = input("Enter the first list(comma-seperated): ").split(',')
list2 = input("Enter the second list(comma-seperated): ").split(',')

set1 = set(list1)
set2 = set(list2)

union_res = list(set1.union(set2))
intersection_res = list(set1.intersection(set2))
print("union:",union_res)
print("intersection:",intersection_res)


