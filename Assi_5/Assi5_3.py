
#print reverse no using recursion
def revno(no):
    if no !=0:
        print(no,end=" ")
        revno(no-1)

#print reverse no using normal iteration
def revnos(no):
    while no>0:
        print(no,end=" ")
        no=no-1

def main():
    no = int(input("Enter the number "))
    print("Using recusrion method :")
    revno(no)
    print()
    print("Using normal iteration method :")
    revnos(no)

if __name__ == "__main__":
    main()