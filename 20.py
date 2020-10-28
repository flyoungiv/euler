# https://projecteuler.net/problem=20
# python makes this easy, challenging myself by writing on one line

import math

print(sum(list(map(int, str(math.prod(list(range(1, 101))))))))
