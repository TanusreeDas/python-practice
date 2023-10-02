if __name__ == '__main__':
    n = int(input("Enter a number").strip())
    if (n%2 != 0): #it is an odd number
        print ("Weird1")
    elif (n%2 == 0 and 2<=n<=5 ):
        print ("Not Weird")
    elif (n%2 == 0 and 6<=n<=20) :
        print("Weird")
    else:
        print("Not Weird")