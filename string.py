# string are immutable and supports indexing (forward and reverse).
# string is iterable, means we can retrive simgle single values from string.

# Note:
# python does not contain char data type, it only store str datatype.

# String functions:


import imp
from itertools import count


s="Compilers"

# 1. Length: general function works for all types like str, tuple, list, range, dict, set or frozen set.
a=len(s)
print(a)


# 2. Reversing string: it is also general function works for all types -//-
b=s[::-1] #slicing
print(b)

# or

c= reversed(s) #it creates reversed class object.
d="".join(c)
print(d)

# or

e=list(reversed(s))
print(e)
f="".join(e)
print(f)


# 3. capetalize: convert 1st letter to capital.
g=s.capitalize()
print("Capetialized str :", g)

# 4. title: capetialize each new word in string:
h="hare krisHna"
i=h.title()
print(i)

# 5. istitle : check for first letter as upper case: boolean
j=h.istitle()
print(j)

# 6. upper: to uppercase
k=s.upper()
print(k)

# 7. isupper : check for all as upper: boolean
l=s.isupper()
print(l)

# how isupper() is used :
# if h.isupper():
#     print("in upper case")
# else:
#     print("not in upper case")


# 8. lower: converts to lower
# 9. islower(): boolean.
# 10. casefold(): converts to lower
# 11. swapcase(): converts to upper and lower to upper
# 12. isalpha(): boolean. returen true if all characters are alphabets. // Blank space is not considered as alphabet.
# 13. isdigit(): boolean. return true if all characters are digits.
# 14. isdecimal(): boolean. return true if all characters are decimal digits.
# 15. isnumerical(): boolean. return true if all characters are decimal or digits.
# 16. isalnum(): boolean. return true if all characters are alphabets or digits.
# 17. isspace(): boolean. return true if all characters are spaces.

m1="\t  " 
print(m1.isspace())


# 18. split(): splits the string into list of substrings.
import re
m2 = "split me in parts of me"
m3 = re.split("\s",m2) # or we can use symbols in space of \s to split.
print(m3)
print(m3[1])

# 19. split()
m4=m2.split('1') # it breaks the string into list of substrings of 2 elements.
print(m4)

# 20. rsplit(): splits the string into list of substrings from right side of string.

# 21. splitlines(): splits the string into list of substrings. by using \n or \r or \r\n.

# 22. count(): count the number of times a substring occurs in the string.
m5=m2.count("me",2)
print(m5)

# 23. endswith(): boolean. return true if the string ends with the specified value or string.
# 24. startswith(): boolean. return true if the string starts with the specified value or string.
# 25. strip(): removes all the leading and trailing characters/ blank spaces in the string.
# 26. lstrip(): removes all the leading characters/ blank spaces in the string.
# 27. rstrip(): removes all the trailing characters/ blank spaces in the string.
# 28. replace(): replaces the specified value or string with another value or string.
# 29. join(): joins the list of strings into a single string after iterable.
# 30. find(): returns the index of the first occurrence of the specified value or string.
# 31. rfind(): returns the index of the last occurrence of the specified value or string.
# 32. index(): returns the index of the first occurrence of the specified value or string.
# 33. rindex(): returns the index of the last occurrence of the specified value or string. from right to left.
# 34. center(): returns a centered string. with specified symbol or whitespace.
ui=m2.center(50,"*")
print(ui)
# 35. ljust(): returns a left justified string. with specified symbol or whitespace.
# 36. rjust(): returns a right justified string. with specified symbol or whitespace.








