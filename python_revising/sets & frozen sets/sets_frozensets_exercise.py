"""
    Find the elements in a given set that are not in another set

    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}

    the difference between set1 and set2 is {1,2,3}
"""

set1 = frozenset({1, 2, 3, 4, 5})
set2 = frozenset({4, 5, 6, 7, 8})
differ_set=set({})


for x in set1:
    if x not in set2:
        differ_set.add(x)
print(differ_set)