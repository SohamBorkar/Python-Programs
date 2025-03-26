#insert()
l=[10,20,30,20]
l.insert(-5,40)#-5 is index where you want to insert element and 40 is element.
l.insert(-10,(1.1,2.2,3.3))
# positive index adds element at the ending of list and 
# negative index adds element from the beginning of the list.
print(l)



#extend()
#it will add all the elements from the given iterable at the end of current
#list object.
#it cannot accept int or float as argument.
# d={"a":33,"3":22}
# l.extend(d) #it will add keys of 'd' at the end.
# print(l)




#count()
# x=l.count(20)
# print(x)



#index(element,[start_index,[end_index]])
#it finds and returns first occurance of element.
#if not found then it will cause value error.
# z=l.index(10,2)
# print(z)



#sort()
#to sort list all elements should be of same or similer data type.
u=[20,30,10,25.23]
u.sort() # or : u.sort(reverse=True)
print(u)



#reverse()  #it simply reversese
m=[10,50,5,50]
m.reverse()
print(m)




#pop(index_is_optional)     #delets the last element of given list.
m=[10,50,5,50]
q=m.pop()
print(m)



#remove(element_to_remove_from_list)
#it delets first element (if have duplicates of elements) when element is found.
i=[1,2,3,4,4]
i.remove(4)
print("list i: ",i)


#clear(): to empty the list.\


#copy(): to create copy insted of using aliasing(refersing to same address.)
l1=i.copy()
