from math import sqrt

# The question is to find the largest prime factor of some large number, call it N.
# If we try brute forcing every potential divisor in the range(1,N),
# then we will run into a performance issue.
# Our approach will be to enumerate sufficiently many prime numbers to
# check the relevant factors of the large number.

# Important idea! We only need to compute prime numbers less than or equal to the square root of N
# since this is sufficient to determine N's factors (and check if they are prime as well).

def calculate_primes(prime_cap: int):
    '''Returns an array of all prime numbers less than prime_cap.
    Use a sieve to generate the primes:
     - initialize the pool of potential primes to be all numbers in the range(2,prime_cap)
     - for each still valid potential prime number
       - confirm the next smallest one as being prime
       - eliminate its multiples from the pool of potential primes'''
    primes = []
    is_prime = [True for _ in range(prime_cap)] # ignore indices 0 and 1
    for k in range(2,prime_cap):
        if is_prime[k]:
            primes.append(k)
            # We have determined k is prime- remove all multiples from the list of potential primes
            for i in range(2,prime_cap):
                if k*i >= prime_cap:
                    break
                is_prime[k*i] = False # k*i must not be prime since k*i is a factorization
    return primes

def largest_prime_factor(n: int):
    '''Returns the largest prime factor of n.
    Requires that primes is the list of all primes less than the square root of n.'''
    # first, calculate the relevant primes
    primes = calculate_primes(int(sqrt(N))+1)
    def is_prime(k: int):
        ''' Returns whether k is prime for k in [2,n)'''
        nonlocal primes
        for p in primes:
            if p > sqrt(k):
                return True
            if k % p == 0:
                return False
        raise 'This should never execute!'
    # Collect all prime factors by iterating over the factors and checking if they are prime
    prime_factors = []
    for p in range(2,int(sqrt(N))+1):
        if n % p == 0:
            q = n // p
            if is_prime(p):
                prime_factors.append(p)
            if is_prime(q):
                prime_factors.append(q)
    return max(prime_factors)

if __name__ == '__main__':
    N = 600_851_475_143
    print(largest_prime_factor(N))
