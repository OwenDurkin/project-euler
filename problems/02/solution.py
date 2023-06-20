# The goal is to take the sum of the even Fibonacci numbers (starting 1,2,3,5,...)
# less than or equal to four million. Our approach will be to generate the Fibonacci numbers,
# and sum the ones that are even.

def fibgen():
    '''A generator function for producing the fibonacci numbers iteratively.'''
    # a=f[i], b=f[i+1], so a+b=f[i]+f[i+1]=f[i+2], by the definition of the Fibonacci numbers
    a = 1
    b = 2
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    total = 0
    for fibnum in fibgen():
        if fibnum > 4_000_000:
            break
        if fibnum % 2 == 0:
            total += fibnum
    print(total)
