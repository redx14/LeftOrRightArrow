#Andrey Ilkiv midterm exam question 2


direction = input("Please enter a direction ( l / r ): ")
cols = int(input("Please enter an integer (>=0): "))

while(direction != "l" and direction != "r"):
    print("Invalid Entry! Try Again!")
    direction = input("Please enter a direction ( l / r ): ")

while(cols < 0):
    print("Invalid Entry! Try Again!")
    cols = int(input("Please enter an integer (>=0): "))
    
cols = cols - 1
if cols != 0:
    if direction == "r" :
        #upper
        for i in range(0 , cols):
            for j in range(0 , i):
                print(" ", end="")
            for k in range(1 , 2):
                print("*" , end="")
            print()
        #lower
        for i in range(0 , cols + 1):
            for j in range(0 , cols - i):
                print(" " , end="")
            for k in range(1 , 2):
                print("*" , end="")
            print()

    if direction == "l" :
        #lower
        for i in range(0 , cols + 1):
            for j in range(0 , cols - i):
                print(" " , end="")
            for k in range(1 , 2):
                print("*" , end="")
            print()
        #upper
        for i in range(1 , cols+1):
            for j in range(0 , i):
                print(" ", end="")
            for k in range(1 , 2):
                print("*" , end="")
            print()

        
