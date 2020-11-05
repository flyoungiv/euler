# https://projecteuler.net/problem=21
import math
import timeit


count = 0

def is_proper_divisor(divisor, n):
    if divisor >= n:
        return False
    if n % divisor == 0:
        return True
    return False


def sum_proper_divisors(n):
    global count
    count += 1
    divisor_sum = 1
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if is_proper_divisor(x, n):
            divisor_sum += x
            if n // x != x:  # don't "double count" perfect square root
                divisor_sum += n // x
    return divisor_sum


def divisor_sums_in_range(n):
    number_pairs = []
    for x in range(1, n + 1):
        number_pairs.append((x, sum_proper_divisors(x)))
    return number_pairs


def has_amicable_pair(t):
    if t[0] == t[1]:  # ignore numbers like 6 or 28 where sum of proper divisors is itself
        return False
    possible_pair = (t[1], sum_proper_divisors(t[1]))
    if t[0] == possible_pair[1]:
        return True
    return False


def sum_amicable_pairs(n):
    sum_of_pairs = 0
    divisor_sums = divisor_sums_in_range(n)
    for x in divisor_sums:
        if has_amicable_pair(x):
            sum_of_pairs += x[0]
    return sum_of_pairs

def has_amicable_pair_2(t, all_sums, n):
    a = all_sums[t-1]
    if a[1] > n: return False
    b = all_sums[a[1]-1]

    if a[0] == a[1]:  # ignore numbers like 6 or 28 where sum of proper divisors is itself
        return False
    
    return a[0] == b[1]


def sum_amicable_pairs_2(n):
    sum_of_pairs = 0
    divisor_sums = divisor_sums_in_range(n)
    
    for x in range(1,n-1):
        if has_amicable_pair_2(x, divisor_sums, n):
            sum_of_pairs += x

    return sum_of_pairs

def sum_amicable_pairs_3(n):
    sum_of_pairs = 0
    divisor_sums = divisor_sums_in_range(n)
    
    for x in range(1,n-1):
        a = divisor_sums[x-1]
        if a[1] > n: continue
        if a[0] == a[1]: continue
        b = divisor_sums[a[1]-1]

        if a[0] == b[1]:
            sum_of_pairs += x

    return sum_of_pairs

def sum_amicable_pairs_4(n):
    sum_of_pairs = 0
    
    for x in range(1,n-1):
        a = sum_proper_divisors(x)
        if a < x: continue
        if a == x: continue
        if a > n: continue
        b = sum_proper_divisors(a)

        if b == x:
            sum_of_pairs += a + b

    return sum_of_pairs


count = 0
print(sum_amicable_pairs_2(10000))
print(count)
count = 0
print(sum_amicable_pairs_3(10000))
print(count)
count = 0
print(sum_amicable_pairs_4(10000))
print(count)


# before
t = timeit.timeit('sum_amicable_pairs(10000)', setup='from __main__ import sum_amicable_pairs', number=100)
print(t)

# after using the cached results instead
t2 = timeit.timeit('sum_amicable_pairs_2(10000)', setup='from __main__ import sum_amicable_pairs_2', number=100)
print(t2)

# eliminating 10000 function calls
t3 = timeit.timeit('sum_amicable_pairs_3(10000)', setup='from __main__ import sum_amicable_pairs_3', number=100)
print(t3)

# add 10,000 function calls but dont cache whole list
# looks like caching the list actually saves time
t4 = timeit.timeit('sum_amicable_pairs_4(10000)', setup='from __main__ import sum_amicable_pairs_4', number=100)
print(t4)

