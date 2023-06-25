# We are tasked with finding the largest palindrome number
# which is a product of two 3-digit numbers

# We will brute force all products of two digit numbers and pick the largest one that is
# a palindrome. There are ~900 three digit numbers [100,999] which means that
# we will be checking 900*900 = 810_000 possibilities. This is computationally tenable.

def is_palindrome(s: str):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

if __name__ == '__main__':
    biggest_palindrome = 0
    for a in range(100,1000):
        for b in range(100,1000):
            if is_palindrome(str(a*b)):
                biggest_palindrome = max(biggest_palindrome, a*b)
    print(biggest_palindrome)


