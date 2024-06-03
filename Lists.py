# Here you will find all the methods of list with examples
#Syntax for list list = [items...]. [] is mandatory for defining list.
#Defining non-nested list
non_nested_list = ["Saron","Tanim","Shithel"]
#Defining nested list
nested_list = [["Ashiqur","Rahman","Saron"],["Tanim","Hossain","Noor"],["Safiu","Shithel"]]
#Defining non-nested list (integer items)
number = [0,1,2,3]
###Methods for lists
##Append method
#Append method adds element end of the list
nested_list.append(["Robert","Drowney","Junior"])
non_nested_list.append("Robert")
print(nested_list)
print(non_nested_list)
##Extend method
#Extend method can add another list at the end of the list
nested_list.extend([["Tom","Cruise"],["Stephen","Colbert"]])
non_nested_list.extend(["Tom","Stephen"])
print(nested_list)
print(non_nested_list)
##Insert method
#Insert method can insert an element at a specified index
nested_list.insert(5,["Martin","King","Junior"])
nested_list[5].insert(1,"Luthor")#Inserting in the sub-list
non_nested_list.insert(5,"Martin")
print (nested_list)
print(non_nested_list)
##Remove method
#Remove method removes the item in the first occurance of a value that it takes as an argumemt
nested_list.remove(['Martin', 'Luthor', 'King', 'Junior'])
nested_list[0].remove("Saron")
non_nested_list.remove('Martin')
print(nested_list)
print(non_nested_list)
##Pop method
#Pop method returns the element of the given index and default is the last element
popped_item1 = nested_list.pop(-1)
popped_item2 = non_nested_list.pop(-1)
print("The popped Item is: "+str(popped_item1))
print("The popped Item is: "+str(popped_item2))
##Clear method
#Removes all the items from the list
import copy
nested_list_copy = copy.deepcopy(nested_list)
nested_list.clear()
non_nested_list_copy = non_nested_list.copy()
non_nested_list.clear()
print(nested_list)
print(non_nested_list)
nested_list = copy.deepcopy(nested_list_copy)
non_nested_list = non_nested_list_copy.copy()
print(nested_list)
print(non_nested_list)
##Index method
#Returns the index
print(nested_list[0].index("Rahman"))
print(non_nested_list.index("Saron",0,1))
##Count Method
#Count method returns the count of the occurances of the passed argument value
print(nested_list[0].count('Saron'))
print(non_nested_list.count("Saron"))
print(number.count(1))
##Sort method
#Sort method sorts all the elements in the list
nested_list.sort() # default sort (ascending order)
print(nested_list)
nested_list.sort(reverse = True)
print(nested_list)
nested_list.sort(key = len)
nested_list.sort( key = lambda i: i[0].lower())
##Reverse Method
#Reverse method reverses the element
nested_list.reverse()
print(nested_list)
### Built In Functions
##Length Function
print(len(nested_list))
print(len(non_nested_list))
##Max Function
print(max(nested_list))
print(max(non_nested_list))
##Min Function
print(min(nested_list))
print(min(non_nested_list))
##Sum Function
print(sum(number))
##Sorted Function
print(sorted(nested_list))
print(sorted(non_nested_list))
##Any Function
print(any(nested_list))
##All Function
print(all(nested_list)) # list has no empty value
##Enumerate Function
for i,n in enumerate(nested_list):
    print(i,n)
print(enumerate(nested_list[0][0]))
##Zip Function
#Cobines list to form tuples
print(list(zip(non_nested_list,nested_list)))
