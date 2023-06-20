# The approach is straightforward:
# we iterate over each number in the range below 1000,
# filter out the numbers that are multiples of 3 or 5, and take their sum.
if __name__ == "__main__":
    print(sum(x for x in range(1,1000) if x%3==0 or x%5==0))
