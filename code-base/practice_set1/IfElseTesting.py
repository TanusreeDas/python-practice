def swap_case(s):
    return s.swapcase()

def reverse_order(s):
    last_index=len(s)
    p=''
    for i in range(last_index,0,-1) :
        p=p+s[i-1]
    return p



if __name__ == '__main__':
    s=input("Enter a string to swap and reverse it's case: ")
    print("Here is your swapped string: ")
    print(swap_case(s))
    print("Here is your reversed string: ")
    print(reverse_order(s))