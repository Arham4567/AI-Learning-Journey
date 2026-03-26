"""Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
a + i = 0
Example:

integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]"""
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = []

for i in range(len(integer)):

    if integer[i]<0:
        y=integer[i]*1
        additive_inverse.append(y)
    else:
        y=integer[i]*-1
        additive_inverse.append(y)

print(additive_inverse)
