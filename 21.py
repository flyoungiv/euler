# https://projecteuler.net/problem=21
import math


def is_proper_divisor(divisor, n):
    if divisor >= n:
        return False
    if n % divisor == 0:
        return True
    return False


def sum_proper_divisors(n):
    divisor_sum = 1
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if is_proper_divisor(x, n):
            divisor_sum += x
            if n / x != x:  # don't "double count" perfect square root
                divisor_sum += n / x
    return divisor_sum


def divisor_sums_in_range(n):
    number_pairs = []
    for x in range(1, n + 1):
        number_pairs.append((x, sum_proper_divisors(x)))
    return number_pairs


def is_amicable_pair(p1, p2):
    if p1[0] == p2[1] and p1[1] == p2[0]:
        return True
    return False


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


print(sum_amicable_pairs(10000))
