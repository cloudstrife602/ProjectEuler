"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

"""
Author note: This doesn't actually solve anything... It does produce the
correct answer but not very efficiently. There is a pattern in how the
permutations are found and this doesn't take that into account. This solution
also uses far more memory than would be necessary in an efficient solution.
"""
import itertools


class PE24(object):
    """Brute force solution to PE24."""

    def permutations(self, integers):
        integers.sort()
        permutations = []
        for permutation in itertools.permutations(integers):
            permutations.append(permutation)
        return permutations

target = 1000000
p = PE24()
permutations = p.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
result = permutations[target - 1]
result_as_string = ''
for c in result:
    result_as_string += str(c)
print(result_as_string)
