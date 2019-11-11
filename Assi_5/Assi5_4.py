
#Using normal function or iteration
def recstar(no):
    sum=0
    for i in range(no):
        rem=no%10
        sum=sum+rem
        no= int(no/10)
    print(sum)
summ=0
#Using the recursion
def recustar(no):
    if no!=0:
        rem = no % 10
        global summ
        summ = summ + rem
        recustar(int(no / 10))
        return(summ)

def main():
    no = int(input("Enter the number "))
    print("Using recusrion method :")
    res=recustar(no)
    print(res)
    print("Using normal iteration method :")
    recstar(no)

if __name__ == '__main__':
    main()