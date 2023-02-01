from itertools import compress


a = "qwertyu"
b = [True, False, True, False, True, False, True]


res = list(compress(a, b))
print(res)
