def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


num_list = input('enter num:')
num_string = num_list.split()
numbers = []
for x in num_string:
    numbers.append(int(x))
prime_list = []
for a in numbers:
    if is_prime(a):
        prime_list.append(a)
print(prime_list)
# prime number is a number which is divided by itself and 1
# perfect number is a number that is equal to the sum of its divisors
# square number( perfect square) result of mutiplying itself(n is a square number if n**0,5 is an integer)
import math


def is_perfect_number(n):
    total = 0
    if n <= 1:
        return False
    for i in range(1, n):
        if n % i == 0:
            total +=i
    return total == n

prefect_num = []
num_list2 = input('enter num:')
num_string = num_list2.split()
for x in num_string:
    if is_perfect_number(int(x)):
        prefect_num.append(int(x))
print(prefect_num)

def is_square (b):
    if b < 0:
        return False
    root = int(math.sqrt(b))
    return root*root == b
square_num = []
num_list3 = input('enter num:')
num_string3 = num_list3.split()
for x in num_string3:
    if is_square(int(x)):
        square_num.append(int(x))
print(square_num)






