from itertools import chain

a = ["tht", "hgh", "nbn"]
b = [1, 3, 5]
c = ["4", "9", "12"]

d = list(chain(a, b, c))

print(d)


a = ["tht", "hgh", "nbn"]
b = range(3, 6)
c = ["4", "9", "12"]


d = list(chain.from_iterable([a, b, c]))

print(d)