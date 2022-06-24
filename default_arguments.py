def appendItem(itemName,itemList=[]):
    itemList.append(itemName)
    return itemList
    
for i in range(0,3):
    inp=input()
    print(appendItem(inp))



def addItemToDictionary(itemName, quantity, itemList = {}):
    itemList[itemName] = quantity
    return itemList
 
 
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))   