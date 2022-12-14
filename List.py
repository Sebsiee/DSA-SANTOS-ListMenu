def display():
    list1 = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
    print("Menu:")
    print("1 -> Add an element")
    print("2 -> Insert an element")
    print("3 -> Modify an element")
    print("4 -> Delete an element")
    print("5 -> Arrange in ascending order")
    print("6 -> Arrage in descending order")
    print("7 -> Count elements")
    print("8 -> Smallest element")
    print("9 -> Largest element\n")
    print(f"List: {list1}")
    whatToDo = input("What do you want to do? (1-9): ")

    if whatToDo == "1":
        appendElement = int(input("Enter the element you want to append: "))
        list1.append(appendElement)
        print("The element has been appended.\n")
        print(f"This is the new array: {list1}")

    elif whatToDo == "2":
        insertElement = int(input("Enter the element you want to insert: "))
        positionInsert = int(input("Enter the position: "))
        list1.insert(positionInsert, insertElement)
        print("The element has been inserted.\n")
        print(f"This is the new array: {list1}")
    
    elif whatToDo == "3":
        modifyElement = int(input("Enter the element you want to modify: "))
        positionModify = int(input("Enter the position: "))
        list1[positionModify] = modifyElement
        print("The element has been modified.\n")
        print(f"This is the new array: {list1}")

    elif whatToDo == "4":
        deleteElement = int(input("Enter the element you want to delete: "))
        list1.remove(deleteElement)
        print("The element has been deleted.\n")
        print(f"This is the new array: {list1}")

    elif whatToDo == "5":
        print("The array has been sorted.\n")
        list1.sort()
        print(f"This is the new array: {list1}")

    elif whatToDo == "6":
        print("The array has been sorted.\n")
        list1.sort(reverse = True)
        print(f"Updated List: {list1}")

    elif whatToDo == "7":
        countElement = int(input("Enter the element you want to count: "))
        counted = list1.count(countElement)
        print(f"The element {countElement} appeared {counted} time/s.")

    elif whatToDo == "8":
        smallest = min(list1)
        print(f"The element '{smallest}' is the smallest.")

    elif whatToDo == "9":
        largest = max(list1)
        print(f"The element '{largest}' is the largest.")

    else:
        print("Input not recognized.")

display()
