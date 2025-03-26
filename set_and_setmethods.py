# set object is used if we want to store unique element and 
#get the elements in random sequence.
# it doesn't support indexing and slicing.
# it cannot maintain elements in specific order.
# it cannot store duplicate objects.
# set object is mutable, but element must be immutable like int, float
#tuple, float, stirng or frozenset.

# frozenset is just like set but it is immutable.

# s={13, 4.3,99,'b',99}
# print(s)
# #you have to use for in loop to access elements from set
# for x in s:
#     print(x,end=" ")

# print()
# # frozenset example:
# t=(10,10.10,'c')
# f=frozenset(t) # frozenset will take only one value as parameter.
# print(f,end=" ")


# instance method is that method which we call with object.

# isdisjoint : return true if any element doesn't mathc.
# s1={1,2,3,4}
# s2={4,5,6,7}
# s3=s1.isdisjoint(s2)
# # or
# # s3=set.isdisjoint(s1,s2)
# print(s3)

#issubset :


# a1={1,2,3,4}
# a2={1,2,3,4,5,6,7,8,9,0}
# a3=a1.issubset(a2)
# #or
# #a3=set.issubset(a1,a2)
# print(a3)


#add :
# b1={10,20,30}
# b1.add(100)
# #or
# #set.add(b1,40)
# print(b1)

# updater :
# c1={1,2,3}
# c2={3,4,2,5}
# c1.update(c2)
# #or
# #set.update(c1,c2)
# print(c1)

# if error occurs in below that error will be named as keyerror.
# pop: x=c1.pop : pops random element.
# remove : removes speicified element. s.remove(30) or set.remove(s,30)
# discard : same as remove. but dont raise keyerror exception when element will not found, then it will return all the elements as it is.
# clear : s1.clear() or set.clear(s1)

# We can't use = sign to copy elements, bcz python will alise it.

#copy : s2=s1.copy() or s2=set.copy(s1)

#union:
d1={1,3,6}
d2={9,5,6,7}
d3={2,4,6,8,0,9}
# d4=set.union(d1,d2,d3)
# print(d4)
#you can also use | to union sets. means d4=d1|d2|d3

# #intersection:
# d4=set.intersection(d1,d2,d3) # or d4= d1.intersection(d2,d3) or d4 = d1 & d2 & d3
# print(d4)


# intersection update:
# d4=set.intersection_update(d1,d2,d3) # or s1.intersection_update(d2,d3)
# print(d1)


# difference: it removes common elements.
# means shows the sort of unique element of set 1 by comparing with another 2.
# d4= set.difference(d1,d2,d3) # or d4=d1.difference(d2,d3) or d4=d1-d2-d3
# print(d4)


# symmetric difference: returns uncommon elements from the set.
# d4 = d1.symmetric_difference(d2) # or d4 = set.symmentric_difference(d1,d2,d3)

