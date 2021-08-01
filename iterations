# computing the sum of the squares of the integers beginning with 5 and ending with 9, using a while loop

def sum_squares1(n):
    result = 0
    while n < 9:
        n = n+1
        if n >= 4:
            result = result + n**2
    return result
sum_squares1(4)

# same task but with a for loop using range(10)
# Used coditional execution within the loop to control which integers are used

def sum_squares2(n):
    result = 0
    for n in range(10):
        if n >= 5:
            result = result + n**2
    return result
sum_squares2(5)

# same task but with range() instead of conditional execution
def sum_squares3(n):
    result = 0
    for n in range(5,10):
            result = result + n**2
    return result
sum_squares3(5)

# skips integer 7
def sum_squares4(n):
    result = 0
    for n in range(5,10):
        if n ==7:
            continue
        result = result + n**2
    return result
sum_squares4(5)

# Set the end argument of range to 100.
# Use break to avoid going beyond 9.
def sum_squares5(n):
    result = 0
    for n in range(5,100):
        if n > 9:
            break
        result = result + n**2
    return result
sum_squares5(5)
