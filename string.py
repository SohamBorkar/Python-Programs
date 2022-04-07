# string are immutable and supports indexing (forward and reverse).
# string is iterable, means we can retrive simgle single values from string.

# Note:
# python does not contain char data type, it only store str datatype.

# String functions:


from xmlrpc.client import boolean


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

