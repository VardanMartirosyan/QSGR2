myList = [1, 2, 3, 4]
print(id(myList))
myList1 = myList
print(id(myList1))
myList.append(5)
print(myList)
print(myList1)
myListCopy = myList.copy()
print(id(myListCopy))
print(id(myList))
print("________________________")
print("MyListCopy: ", myListCopy)
print("myList: ", myList)
print("myList1: ", myList1)
myListCopy.append(6)
print("After appending 6 to myListCopy")
print("MyListCopy: ", myListCopy)
print("myList: ", myList)
print("myList1: ", myList1)
myList.append(7)
print("After appending 7 to myList")
print("MyListCopy: ", myListCopy)
print("myList: ", myList)
print("myList1: ", myList1)

