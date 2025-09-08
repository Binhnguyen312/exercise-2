# 1.Write a Python function to find the maximum of three numbers.
import math


def max_of_three(a, b, c):
    return max(a, b, c)


a = 1
b = 2
c = 3
print(max_of_three(a, b, c))


# 2.Write a Python function to sum all the numbers in a list.
def sum_num_list(lst):
    return sum(lst)


lst = [1, 2, 3, 4]
print(sum_num_list(lst))


# 3.Write a Python program to reverse a string.
def reverse_string(stri):
    return stri[::-1]


stri = 'hello world'
print(reverse_string(stri))


# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


print(calculate_factorial(4))


# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(3))


# 6.Write a Python function to print
# 1.all prime numbers that less than a number (enter prompt keyboard).
def print_primes_less_than(i):
    print(f' Prime number less than{i}')
    for num in range(2, i):
        if is_prime(num):
            print(num, end=' ')
        print()


print_primes_less_than(4)


# 2.the first N prime numbers
def print_first_n_primes(N):
    print(f'The first {N} prime numbers:')
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1
    print()


print_first_n_primes(5)


# 7.Write a Python function to check whether a number is "Perfect" or not.
# Then print all perfect number that less than 1000.
def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n


def print_perfect_numbers(limit):
    print(f'Perfect numbers less than {limit}:')
    for num in range(2, limit):
        if is_perfect(num):
            print(num, end=' ')
    print()


print_perfect_numbers(1000)
# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
def is_pagram(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwsyz'
    for letter in alphabet:
        if letter not in sentence:
            return False
        return True
text = 'The quick brown fox jumps over the lazy dog'
if is_pagram(text):
    print('It is a pagram')
else:
    print('It is not a pagram')

