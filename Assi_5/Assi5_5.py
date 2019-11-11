
#Using the recursion
summ=1
def recustar(no):

    if no>0:
        global summ
        summ = summ * no
        #no = int(no - 1)
        recustar(no - 1)
        return(summ)



def main():
    no = int(input("Enter the number "))
    print("Using recusrion method :")
    res=recustar(no)
    print(res)


if __name__ == "__main__":
    main()
