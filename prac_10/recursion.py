def do_it(n):
    """Calculate the sum of remainders when dividing numbers from n down to 1 by 2."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return
    print(n ** 2)
    do_something(n - 1)

def do_something_backwards(n, current=0):
    """Print the squares of positive numbers from 0 up to n."""
    if current > n:
        return
    do_something_backwards(n, current + 1)
    if current >= 0:
        print(current ** 2)

def calculate_pyramid_blocks(rows):
    """Calculate blocks needed for a 2D pyramid with given rows."""
    if rows <= 0:
        return 0
    return rows + calculate_pyramid_blocks(rows - 1)

def print_outside_in(s, left=0, right=None):
    """Print string characters from outside in."""
    if right is None:
        right = len(s) - 1
    if left > right:
        return
    if left == right:
        print(s[left], end=' ')
    else:
        print(s[left], s[right], end=' ')
    print_outside_in(s, left + 1, right - 1)

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and non-alphabetic chars)."""
    s = ''.join(c.lower() for c in s if c.isalpha())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Test cases
print(do_it(5))  # Output: 3
do_something(4)  # Output: 16, 9, 4, 1, 0
do_something_backwards(4)  # Output: 0, 1, 4, 9, 16
print(calculate_pyramid_blocks(6))  # Output: 21
print_outside_in("Programming")  # Output: P g r n o i g m r m a
print(is_palindrome("Hannah"))  # Output: True
print(is_palindrome("Python"))  # Output: False