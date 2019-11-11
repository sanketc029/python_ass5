#Print 1-5 no using recursion


#Using the recursion
def recuno(no):
    if no !=0:
        no=no-1
        recuno(no)
        print(no+1, end=" ")

#Using normal function or iteration
def recstar(no):
    for i in range(1,no+1):
        print(i, end=" ")

def main():
    no = int(input("Enter the number "))
    print("Using recusrion method :")
    recuno(no)
    print()
    print("Using normal iteration method :")
    recstar(no)

if __name__ == "__main__":
    main()




