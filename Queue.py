list1 = []
print("Welcome To Stack Operation")
while True:
    print("For Enqueue type 1, for Dequeue type 2 and for exit type 3")
    choice = int(input("Enter the operation:"))
    if choice == 1:
        element = str(input("Enter Your Element:"))
        list1.append(element)
        print(list1)
    elif choice == 2:
        if not list1:
            print("Element Cant be Popped")
        else:
            element = str(list1.pop(0))
            print("You Have popped "+ element)
            print(list1)
    elif choice == 3:
        break
    else:
        print("Invalid Input type !")
