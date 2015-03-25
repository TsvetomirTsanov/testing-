def factorial (n):
    result = 1

    for x in range(1, n+1):
        result *=x

    return result


def fibonacci(n):
    result = []

    a = 1
    b = 1

    while len(result) < n:
        result.append(a)

        next_fib = a+b
        a = b
        b = next_rib

    return result


def sum_of_digits(n):
    return sum(to_digits(n))

def to_digits(n):
    return [int(x) for x in str(n)]

def factorial_digits(n):
    return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):
    return str(obj)[::-1] == str(obj)

def count_digits(n):
    sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result*(10**digits_count) + digit

    return result

def fibonacci_number(n):
    return to_number(fibonacci(n))

def count_vowels(string):
    vowels = "sdadSDADdgher"
    count = 0
    for ch in string:
        if ch in vowels:
            count+=1
    return count

def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] +=1
        else:
            result[ch] = 1
    return result

def p_score(n):
    if(palindrome(n)):
        return 1

    s = n + int(str(n)[::-1])

    return 1 + p_score(s)

def is_even(n):
    return n%2 == 0

def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n +=1
    while not is_hack(n):
        n+=1

    return n

def sum_of_divisors(n):
    a = 1
    sum = 0
    while a <= n:
        if n%a == 0:
            sum += a
        a+=1
    return sum

def is_prime(n):
    a = 1
    count = 0
    if n == 1:
        count = 2
    else:
        while a <= n:
            if n%a == 0:
                count +=1
            a +=1
    
    if count == 2:
        return True
    else:
        return False

def contains_digit(number, digit):
    return str(digit) in str(number)

def contains_digits(number, digits):
    for n in digits:
        if n not in to_digits(number):
            return False

    return True

def is_number_balanced(n):
    a = to_digits(n)
    sum1 = 0
    sum2 = 0
    if(is_even(n)):
        for num in a:
            if num < len(n)/2:
                sum1 += num
            else:
                sum2 += num


def count_substrings(haystack, needle):
    count = 0
    for ch in len(haystack):
        if needle in haystack[ch:]:
            count += 1
    return count