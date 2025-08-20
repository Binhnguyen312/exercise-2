#  Python String 113 exercises
#  1. Write a Python program to calculate the length of a string.
import textwrap

print(len('hello world'))
#  2. Write a Python program to count the number of characters (character frequency) in a string.
#  Sample String : google.com'
#  Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
text = 'google.com'
char_count = {}
for char in text:
     if char in char_count :
         char_count[char] += 1
     else:
        char_count[char] = 1
print(char_count)
 # 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given
 # string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
 # Sample String : 'w3'
 # Expected Result : 'w3w3'
 # Sample String : ' w'
#  Expected Result : Empty String
txt = str(input('Enter text: '))
if len(txt) < 2:
    result = ''
else:
     result = (txt[:2]) +(txt[-2:])
     print(result)

 # 4. Write a Python program to get a string from a given string where all occurrences of its first
 # char have been changed to '$', except the first char itself.
 # Sample String : 'restart'
# Expected Result : 'resta$t'
a = 'restart'
first_char = a[0]
the_rest = a[1:]
rest = the_rest.replace( first_char,'$')
outcome = first_char + rest
print(outcome)
 # 5. Write a Python program to get a single string from two given strings, separated by a space and
 # swap the first two characters of each string.
 # Sample String : 'abc', 'xyz'
 # Expected Result : 'xyc abz'
b = 'abc'
c = 'xyz'
b_new = c[0] + b[1:]
c_new = b[0] + c[1:]
print(b_new)
print(c_new)
consequence = b_new + ' ' + c_new
print(consequence)

 # 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
# less than 3, leave it unchanged.
 # Sample String : 'abc'
 # Expected Result : 'abcing'
 # Sample String : 'string'
 # Expected Result : 'stringly'
d = str(input('Enter text: '))
if len(d) >= 3:
     if 'ing'in d:
         print(d + 'ly')
     else :
         print(d + 'ing')
else:
     print(d)

 # 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given
 # string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
 # resulting string.
 # Sample String : 'The lyrics is not that poor!'
 # 'The lyrics is poor!'
 # Expected Result : 'The lyrics is good!'
 # 'The lyrics is poor!'
e = str(input('Enter text: '))
p_not = e.find('not')
print(p_not)
p_poor = e.find('poor')
print(p_poor)
if p_not != -1 and p_poor != -1 and p_poor > p_not:
     result = e[:p_not] + 'good' + e[p_poor+4:]
     print(result)
else:
     print(e)

 # 8. Write a Python function that takes a list of words and return the longest word and the length
 # of the longest one.
 # Sample Output:
 # Longest word: Exercises#
# Length of the longest word: 9
def longest_word(words):
    longest = ''
    for word in words:
         if len(word) > len(longest):
             longest = word
    return longest, len(longest)
words = input("Enter some words: ").split()
print(words)
word , length = longest_word(words)
print(word)
print(length)

 # 9. Write a Python program to remove the nth index character from a nonempty string
def remove_chars(string, n):
     return string[:n] + string[n+1:]
word = str(input('Enter word:'))
n = int(input('Enter value:'))
print(remove_chars(word, n))
 # 10. Write a Python program to change a given string to a newly string where the first and last
 # chars have been exchanged.
e = str(input('Enter text: '))
new_e = e[-1] + e[1:-1] + e[0]
print(new_e)
 # 11. Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_index_value(string):
     result = ''
     for i in range(len(string)):
         if i % 2 == 0:
             result += string[i]
     return result
f = str(input('Enter text: '))
f_new = remove_odd_index_value(f)
print(f_new)
 # 12. Write a Python program to count the occurrences of each word in a given sentence.
def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
         if word in count:
             count[word] += 1
         else:
            count[word] = 1
    return count
sentence = input('Enter sentence: ')
print(word_count(sentence))

 # 13. Write a Python script that takes input from the user and displays that input back in upper
 # and lower cases.
g = str(input('Enter text: '))
print(g.upper())
print(g.lower())
 # 14. Write a Python program that accepts a comma-separated sequence of words as input and
 # prints the distinct words in sorted form (alphanumerically).
 # Sample Words : red, white, black, red, green, black
 # Expected Result : black, green, red, white,red
def distinct_sorted ():
    word_list = input('Enter words separated by commas: ')
    words= [word.strip() for word in word_list.split(',')]
distinct_words = sorted(set(words))
print(','.join(distinct_words))
distinct_sorted()
 # 15. Write a Python function to create an HTML string with tags around the word(s).
 # Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
#  add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, text):
     return f'<{tag}>{text}</{tag}>'
tag = input('Enter tag: ')
text = input('Enter text: ')
print(add_tags(tag, text))
 # 16. Write a Python function to insert a string in the middle of a string.
 # Sample function and result :
 # insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
 # insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_middle (base, word):
     middle_index = len(base)//2
     return base[:middle_index] + word + base[middle_index:]
word = input('Enter word: ')
base = input('Enter base: ')
print(insert_middle(base, word))
 # 17. Write a Python function to get a string made of 4 copies of the last two characters of a
# # specified string (length must be at least 2).
# # Sample function and result :
# # insert_end('Python') -> onononon
# # insert_end('Exercises') -> eseseses
def string_4_copies (string):
     if len(string) >=2:
         last_two= string[-2:]
         return last_two * 4
string = input('Enter string: ')
print(string_4_copies(string))

 # 18. Write a Python function to get a string made of the first three characters of a specified string.
# # If the length of the string is less than 3, return the original string.
# # Sample function and result :
# # first_three('ipy') -> ipy
# # first_three(' python') -> pyt
def string_3_char (s):
     for char in s:
         if len(s) >=3:
             return s[:3]
         else:
             return s
s = input('Enter string: ')
print(string_3_char(s))

# # 19. Write a Python program to get the last part of a string before a specified character.
# # https://www.w3resource.com/python-exercises
# # https://www.w3resource.com/python
def before_first_char (text, char):
     return text.split(char)[0]
text = input('Enter text: ')
char = input('Enter char: ')
print(before_first_char(text, char))
 # 20. Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_string (text):
    if len(text) % 4 ==0:
        return text[::-1]
text = input('Enter text: ')
print(reverse_string(text))
 # 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
 # uppercase characters in the first 4 characters.
def convert_to_upper (text):
     first_4_char = text[:4]
     upper_count = 0
     for char in first_4_char:
         if char.isupper():
             upper_count +=1
     if upper_count >=2:
          return text.upper()
     else:
         return text
text = input('Enter text: ')
print(convert_to_upper(text))

 # 22.Write a Python program to sort a string lexicographically.
def sort_string_lexicographically(text):
     sorted_char = sorted(text)
     return ''.join(sorted_char)
text = input('Enter text: ')
print(sort_string_lexicographically(text))
 #23. Write a Python program to remove a newline in Python.
def remove_newline(text):
     return text.replace('\n', '')
text = input('Enter text2: ')
print(remove_newline(text))
 # 24. Write a Python program to check whether a string starts with specified characters.
h = str(input('Enter text: '))
char_check = input('Enter char: ')
def check_char (h, char):
     if char in h:
         return True
     else:
         return False
print(check_char(h, char_check))
 # 25. Write a Python program to create a Caesar encryption.
# # Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# # code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# # type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# # number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# # by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# # private correspondence.
def caesar_encrypt (text, shift):
     encrypted_text = ''
     for char in text:
         if char.isalpha():
             if char.isupper():
                 encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
             else:
                 encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
         else:
             encrypted_text += char
     return encrypted_text
text = input('Enter text: ')
shift = int(input('Enter shift: '))
print(caesar_encrypt(text, shift))
 # 26. Write a Python program to display formatted text (width=50) as output.
text = input('Enter text: ')
formatted_text = textwrap.fill(text,width = 50)
print(formatted_text)
 # 27. Write a Python program to remove existing indentation from all of the lines in a given text.
text = input('Enter text: ')
print(textwrap.dedent(text))
 #28. Write a Python program to add prefix text to all of the lines in a string.
def add_string (text,prefix):
     lines = text.splitlines()
     prefixed_lines = [prefix + line for line in lines]
     return '\n'.join(prefixed_lines)
print ('Enter your paragraph(press enter twice to finish):')
lines = []
while True:
     line = input()
     if line == '':
         break
     lines.append(line)
text = '\n'.join(lines)
prefix = input('Enter prefix:')
print (add_string(text, prefix))

# # 29. Write a Python program to set the indentation of the first line.
def set_first_line_indent(text,indent_spaces):
     lines = text.splitlines()
     if lines:
         lines[0] = ' '* indent_spaces + lines[0]
         return'\n'.join(lines)
print ('Enter your paragraph(press enter twice to finish):')
lines = []
while True:
     line = input()
     if line == '':
         break
     lines.append(line)
text = '\n'.join(lines)
print ('\nIndented paragraph:')
print(set_first_line_indent(text, 4))
# # 30. Write a Python program to print the following numbers up to 2 decimal places.
num = float(input('Enter value: '))
print('print number up to 2 decimal places:')
print(f"{num:.2f}")

 #31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
i = float(input('enter value:'))
print('Number with 2 decimals and sign:')
print(f'{i:+.2f}')
# 32. Write a Python program to print the following positive and negative numbers with no
# # decimal places.
h = float(input('Enter value:'))
print('number with no decimal places:')
print(f"{h:+.0f}")

 # 33. Write a Python program to print the following integers with zeros to the left of the specified
 # width.
j = int(input('Enter value:'))
print('number with zero to the left:')
print(f"{j:05d}")

# # 34. Write a Python program to print the following integers with '*' to the right of the specified
# # width.
k = int(input('Enter value:'))
print(str(k).ljust(2,'*'))

# # 35. Write a Python program to display a number with a comma separator.
m = int(input("Enter a number: "))
print(f'formatted number:{m:,}')
# # 36. Write a Python program to format a number with a percentage.
l = int(input('Enter value:'))
print(str(l).ljust(2,'%'))
# # 37. Write a Python program to display a number in left, right, and center aligned with a width of
# 10.
n = int(input('Enter a number: '))
print(f'left aligned: {n:<10}')
print(f'right aligned: {n:>10}')
print(f'Center aligned: {n:^10}')
 # 38. Write a Python program to count occurrences of a substring in a string.
o = input("Enter a string: ")
sub = input('enter a substring: ')
count = o.count(sub)
print(f'The substring "{sub}" appears {count} times in total.')

#  39. Write a Python program to reverse a string.
p = str(input('Enter a string: '))
print(p[::-1])
# 40. Write a Python program to reverse words in a string.
text = input('Enter a string: ')
reversed_text =' '.join(text.split()[::-1])
print(reversed_text)
 #41. Write a Python program to strip a set of characters from a string.
txt = input('enter a string:')
char_to_strip = input('enter char to strip:')
stripped = txt.strip(char_to_strip)
print(stripped)
## 42. Write a Python program to count repeated characters in a string.
## Sample string: 'thequickbrownfoxjumpsoverthelazydog'
## Expected output :
# # o 4
# # e 3
# # u 2
# # h 2
# # r 2
# # t 2
def count_repeated_characters(text):
    counted_characters = {}
    for character in text:
         if character in counted_characters:
             counted_characters[character] += 1
         else:
             counted_characters[character] = 1
             repeated = {ch: count for ch, count in counted_characters.items() if count > 1}
    return repeated
text = input("Enter a text: ")
print(count_repeated_characters(text))
# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
area = float(input("Enter value of area: "))
volume = float(input("Enter a volume: "))
print(f'The area of rectangle is {area:.2f}cm\u00b2')
print(f'The volume of the cylinder is {volume:.2f}cm\u00b3')
 # 44. Write a Python program to print the index of a character in a string.
 # Sample string: w3resource
 # Expected output:
 # Current character w position at 0
 # Current character 3 position at 1
 # Current character r position at 2
 # - - - - - - - - - - - - - - - - - - - - - - - - -
# # Current character c position at 8
# # Current character e position at 9
q = str(input("Enter a string: "))
for index, char in enumerate(q):
    print(f'current character {char} position at {index}')

## 45. Write a Python program to check whether a string contains all letters of the alphabet.
import string
def is_pangram (text):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(text.lower())
text = input("Enter a sentence: ")
if is_pangram(text):
     print('the string contains all letters of the alphabet')
else:
     print('the string does not contain all letters of the alphabet')
# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
r = str(input("Enter a string: "))
r2 = r.split()
print(r2)
#47. Write a Python program to lowercase the first n characters in a string.
def lowercase_first_n(s,n):
    n = min(n,len(s))
    return s[:n].lower() +s[n:]
text = input("Enter a sentence: ")
n= int(input("Enter a number: "))
result = lowercase_first_n(text,n)
print(result)
 # 48. Write a Python program to swap commas and dots in a string.
# # Sample string: "32.054,23"
# # Expected Output: "32,054.23"
s =(input('Enter a number: '))
s_new = s.replace ('.', ',')
print(s_new)
# 49. Write a Python program to count and display vowels in text.
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    for char in text :
        if char in vowels:
            vowel_count[char] = vowel_count.get(char,0) + 1
    return vowel_count
text = input('Enter a text: ')
vowel_counts = count_vowels(text)
print(vowel_counts)
for vowel, count in vowel_counts.items():
    print(f'{vowel}:{count}')

# 50. Write a Python program to split a string on the last occurrence of the delimiter.
text = input('Enter a text: ')
delimiter = input('Enter a delimiter: ')
parts = text.rsplit(delimiter,1)
print("Before last delimiter:", parts[0])
if len(parts) > 1:
    print("After last delimiter:", parts[1])
else:
    print("Delimiter not found in the string.")
# 51. Write a Python program to find the first non-repeating character in a given string.
# 52. Write a Python program to print all permutations with a given repetition number of characters
# of a given string.
# 53. Write a Python program to find the first repeated character in a given string.
# 54. Write a Python program to find the first repeated character in a given string where the index
# of the first occurrence is smallest.
# 55.Write a Python program to find the first repeated word in a given string.
# 56. Write a Python program to find the second most repeated word in a given string.
# 57.Write a Python program to remove spaces from a given string.
# 58. Write a Python program to move spaces to the front of a given string.
# 59. Write a Python program to find the maximum number of characters in a given string.
# 60. Write a Python program to capitalize the first and last letters of each word in a given string.
# 61. Write a Python program to remove duplicate characters from a given string.
# 62. Write a Python program to compute the sum of the digits in a given string.
# 63. Write a Python program to remove leading zeros from an IP address.
# 64. Write a Python program to find the maximum length of consecutive 0's in a given binary
# string.
# 65. Write a Python program to find all the common characters in lexicographical order from two
# given lower case strings. If there are no similar letters print "No common characters".
# 66. Write a Python program to make two given strings (lower case, may or may not be of the
# same length) anagrams without removing any characters from any of the strings.
# 67. Write a Python program to remove all consecutive duplicates of a given string.
# 68. Write a Python program to generate two strings from a given string. For the first string, use
# the characters that occur only once, and for the second, use the characters that occur multiple
# times in the said string.
# 69. Write a Python program to find the longest common sub-string from two given strings.
# 70. Write a Python program that concatenates uncommon characters from two strings.
# 71. Write a Python program to move all spaces to the front of a given string in a single traversal.
# 72. Write a Python program to remove all characters except a specified character from a given
# string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee
# 73. Write a Python program to count Uppercase, Lowercase, special characters and numeric
# values in a given string.
# 74. Write a Python program to find the minimum window in a given string that will contain all
# the characters of another given string.
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "OERIUS"
# 75. Write a Python program to find the smallest window that contains all characters in a given
# string.
# 76. Write a Python program to count the number of substrings from a given string of lowercase
# alphabets with exactly k distinct (given) characters.
# 77. Write a Python program to count the number of non-empty substrings of a given string.
# 78. Write a Python program to count characters at the same position in a given string (lower and
# uppercase characters) as in the English alphabet.
# 79. Write a Python program to find the smallest and largest words in a given string.
# 80. Write a Python program to count the number of substrings with the same first and last
# characters in a given string.
# 81. Write a Python program to determine the index of a given string at which a certain substring
# starts. If the substring is not found in the given string return 'Not found'.
# 82. Write a Python program to wrap a given string into a paragraph with a given width.
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.
# 83. Write a Python program to print four integer values - decimal, octal, hexadecimal
# (capitalized), binary - in a single line.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001
# 84. Write a Python program to swap cases in a given string.
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY
# 85. Write a Python program to convert a given Bytearray to a Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d
# 86. Write a Python program to delete all occurrences of a specified character in a given string.
# Sample Output:
# Original string:
# Delete all occurrences of a specified character in a given string
# Modified string:
# Delete ll occurrences of specified chrcter in given string
# 87. Write a Python program to find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python
# 88. Write a Python program to check whether a given string contains a capital letter, a lower case
# letter, a number and a minimum length.
# Sample Output:
# Input the string: W3resource
# ['Valid string.']
# 89. Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD
# 90. Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution
# 91. Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False
# 92. Write a Python program to find string similarity between two given strings.
# Sample Output:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871
# Original string:
# Python Exercises
# Python Ex.
# Similarity between two said strings:
# 0.6923076923076923
# Original string:
# Python Exercises
# Python
# Similarity between two said strings:
# 0.5454545454545454
# Original string:
# Java Exercises
# Python
# Similarity between two said strings:
# 0.0
# 93. Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]
# 94. Write a Python program to convert a hexadecimal color code to a tuple of integers
# corresponding to its RGB components.
# Sample Output:
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)
# 95. Write a Python program to convert the values of RGB components to a hexadecimal color
# code.
# Sample Output:
# FFA501
# FFFFFF
# 000000
# 000080
# C0C0C0
# 96. Write a Python program to convert a given string to Camelcase.
# Sample Output:
# javascript
# fooBar
# fooBar
# foo.Bar
# fooBar
# foobar
# fooBar
# 97. Write a Python program to convert a given string to Snake case.
# Sample Output:
# java_script
# foo_bar
# foo_bar
# foo.bar
# foo_bar
# foo_bar
# foo_bar
# 98. Write a Python program to decapitalize the first letter of a given string.
# Sample Output:
# java Script
# python
# 99. Write a Python program to split a multi-line string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']
# 100. Write a Python program to check whether any word in a given string contains duplicate
# characters or not. Return True or False.
# Sample Output:
# Original text:
# Filter out the factorials of the said list.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True
# 101. Write a Python program to add two strings as if they were numbers (positive integer values).
# Return a message if the numbers are strings.
# Sample Output:
# 42
# Error in input!
# Error in input!
# 102. Write a Python program to remove punctuation from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation
# 103. Write a Python program to replace each character of a word of length five and more with a
# hash character (#).
# Sample Output:
# Original string: Count the lowercase letters in the said list of words:
# Replace words (length five or more) with hash characters in the said string:
# ##### the ######### ####### in the said list of ######
# Original string: Python - Remove punctuations from a string:
# Replace words (length five or more) with hash characters in the said string:
# ###### - ###### ############ from a #######
# 104. Write a Python program that capitalizes the first letter and lowercases the remaining letters
# in a given string.
# Sample Data:
# ("Red Green WHITE") -> "Red Green White"
# ("w3resource") -> "W3resource"
# ("dow jones industrial average") -> "Dow Jones Industrial Average"
# 105. Write a Python program to extract and display the name from a given Email address.
# Sample Data:
# ("john@example.com") -> ("john")
# ("john.smith@example.com") -> ("johnsmith")
# ("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")
# 106. Write a Python program to remove repeated consecutive characters and replace them with
# single letters and print a updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"
# 107. Write a Python program that takes two strings. Count the number of times each string
# contains the same three letters at the same index.
# Sample Data:
# ("Red RedGreen") -> 1
# ("Red White Red White) -> 7
# ("Red White White Red") -> 0
# 108. Write a Python program that takes a string and returns # on both sides of each element,
# which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"
# 109. Write a Python program that counts the number of leap years within the range of years.
# Ranges of years should be accepted as strings.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6
# 110. Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
# 111. Write a Python program that takes a string and replaces all the characters with their
# respective numbers.
# Sample Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"
# 112. Write a Python program to calculate the sum of two numbers given as strings. Return the
# result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"
# 113. Write a Python program that returns a string sorted alphabetically by the first character of a
# given string of words.
# Sample Data:
# ("Red Green Black White Pink") -> "Black Green Pink Red White"
# ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of
# sum said strings. the two")
# ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over
# quick the")