import copy  #importing the copy module 

spam = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
print(spam)
##################################################################################
newList = copy.copy(spam)
print(newList)
##################################################################################
newList[6] = "Fuck ABCD"
print(newList)
