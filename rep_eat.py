import operator
from itertools import repeat
from itertools import accumulate

for i in repeat("some text", 5):
    print(i)



print(*list(accumulate(range(1, 12))))
print(*list(accumulate(range(1, 12), operator.mul)))
print(*list(accumulate(range(2, 10), operator.pow)))