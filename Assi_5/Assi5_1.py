
#Print nth  no * using recursion

#Using normal function or iteration
def recstar(no):
    for i in range(no):
        print("*", end=" ")

#Using the recursion
def recustar(no):
    if no !=0:
        recustar(no-1)
        print("*", end=" ")


def main():
    no = int(input("Enter the number "))
    print("Using recusrion method :")
    recustar(no)
    print()
    print("Using normal iteration method :")
    recstar(no)

if __name__ == "__main__":
    main()