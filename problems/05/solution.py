from collections import Counter
# What is the smallest positive number that is evenly divisible (i.e. a multiple of)
# all the numbers from 1 to 20?

# Let's see.

# 1 * 2 * 3 * (4=> 2) * 5 * (6 is covered by 2*3) * 7 * (8=>2) * (9=>3) * ...

# The other way of thinking about this is to consider the prime factorizations of each number
# in [1,20] and take the max of each prime.

prime_numbers = [2,3,5,7,11,13,17,19]

prime_factorizations = []

def factorize(n):
    factors = Counter()
    for p in prime_numbers:
        while n % p == 0:
            factors[p] += 1
            n = n // p
    return factors

for k in range(2,21):
    prime_factorizations.append(factorize(k))

if __name__ == "__main__":
    product = 1
    for prime in prime_numbers:
        # print(prime, max(x[prime] for x in prime_factorizations))
        product *= prime**max(x[prime] for x in prime_factorizations)
    print(product)
