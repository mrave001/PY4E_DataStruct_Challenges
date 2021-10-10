#Exercise 05_02 determine the min and max number from a list

largest = None
smallest = None
while True:
    num = input('Please enter a number (type "done" when finished): ')
    if num == 'done':
        if smallest is not None:
            print(f"Smallest is: {smallest}")
        print(f"Largest is: {largest}") 
        break
    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num   
        if smallest is None or smallest > num:
            smallest = num           
    except:
        print("Invalid Input")
