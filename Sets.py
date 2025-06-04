# from List import names_lists
#
# myset = {"apple", "banana", "cherry"}
# print(myset)
#
# #Unordered -Unordered means that the items in a set do not have a defined order.
# #          -Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# # Unchangeable
# # Duplicates Not Allowed - Sets cannot have two items with the same value.
# myset = {"apple", "banana", "cherry","cherry"}
# print(myset)
# thisset = {"apple", "banana", "cherry", False, True, 0,1 }
# # # False and 0 is considered the same value & 1 ie True.
# print(thisset)
# print(len(thisset))
#
# set1 = {"abc", 34, True, 40, "male"}
# print(type(set1))
# print(set(set1))
#
# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)
#
# fruit = {"Apple","sitaphal","Banana"}
# fruit.add("Tarbuj")
# print(fruit)
# x = fruit.difference(fruits)
# print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)
# y.remove("google")
# print(y)
x.update(y)
print(x)