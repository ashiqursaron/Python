# stack is using list
# defining a list
# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         raise IndexError("Pop From Empty Stack")
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         raise IndexError("Peek From Empty Stack")
#     def is_empty(self):
#         return len(self.items) == 0
#     def size(self):
#         return len(self.items)
    
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack.pop())

list1 = []
print("Welcome To Stack Operation")
while True:
    print("For Push type 1, for Pop type 2 and for exit type 3")
    choice = int(input("Enter the operation:"))
    if choice == 1:
        element = str(input("Enter Your Element:"))
        list1.append(element)
    elif choice == 2:
        if not list1:
            print("Element Cant be Popped")
        else:
            element = str(list1.pop())
            print("You Have popped "+ element)
    elif choice == 3:
        break
    else:
        print("Invalid Input type !")



    #element = input("Enter the Element:")



    
