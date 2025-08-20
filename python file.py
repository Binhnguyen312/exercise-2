# # 1.Write a program that prompts the user to enter base and height of the triangle
# # and calculate an area of this triangle (area = 0.5 x b x h).
# import math
#
# b = float(input("Enter b: "))
# h = float(input("Enter h: "))
# triangle_area = 0.5 * b * h
# print(triangle_area)
# # 2.Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# a = float(input("Enter a:"))
# b = float(input("Enter b:"))
# c = float(input("Enter c:"))
#
# # Calculate the perimeter, area of the triangle (perimeter = a + b + c).
# triangle_perimeter = a + b + c
# print(triangle_perimeter)
# p = triangle_perimeter /2
# print(p)
# area_of_triangle = math.sqrt( p*(p-a)*(p-b)*(p-c) )
# print(area_of_triangle)
#
# # 3.Get length and width of a rectangle using prompt. Calculate its area
# # (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# rectangle_area = length * width
# print(rectangle_area)
# rectangle_perimeter = 2*(length + width)
# print(rectangle_perimeter)
#
# # 4.Get radius of a circle using prompt. Calculate the area (area = pi x r x r)
# # and circumference (c = 2 x pi x r) where pi = 3.14.
# r = float(input("Enter radius: "))
# circumference = 2 * math.pi * r
# print(circumference)
# circle_area = math.pi * r **2
# print(circle_area)
# # 10.Use and operator to check if 'on' is found in both 'python' and 'dragon’
# print('on' in 'python'and 'on' in 'dragon')
#
# # 11.“I hope this course is not full of jargon.” Use in operator to check if jargon is in the sentence.
# print ('jargon'in 'i hope this course is not full of jargon')
# # 13.Find the length of the text ‘python’ and convert the value to float and convert it to string
# l = len('python')
# print(l)
# n = float(l)
# print(n)
# j = str(n)
# print(j)
# # 14.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# k = int(input("Enter number: "))
# print(k)
# q = k%2
# print(q==0)
#
# # 15.Writs a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours = float(input("Enter hours: "))
# rate_per_hour = float(input("Enter value: "))
# pay_of_person = hours * rate_per_hour
# print(pay_of_person)
#
# # 16.Write a script that prompts the user to enter number of years.
# # Calculate the number of seconds a person can live. Assume a person can live hundred years
# years = float(input("Enter years: "))
# seconds_per_year = 365 *24*60*60
# print(seconds_per_year)
# seconds_person_live = seconds_per_year * years
# print(seconds_person_live)
a = 'i have a dream'
print(a[0])