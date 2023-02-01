from itertools import product
from itertools import permutations

data = [(-1, 1), (-2, 2), (-3, 3)]

res = list(product(*data))

print(res)


res = [item for item in permutations("XYZ", 2)]

print(res)