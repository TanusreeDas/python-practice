def my_func(val):
    return val[0]

if __name__=="__main__":
    a={1,2,4,3,3,7,5,2,6,100,1000,34,56}
    print("original set-> ")
    print(a)
    lis=list((1,2,3,7,0,100,32,56,24))
    lis[len(lis):]=[5]
    print("original list-> ")
    print(lis)
    print("reversed list-> ")
    lis.reverse()
    print(lis)
    print("sorted set-> ")
    print(sorted(a,reverse=True))
    lis.sort(reverse=True)
    print("sorted list by sort method->")
    print(lis)

    lis1=[(1,2),(2,3),(2,4,7,2),(9,5),(8,6),(8,6,7)]
    print("*****************************************")
    lis1.sort(key=len)
    print(lis1)

    tup1=(1,2,3,8,4)
    print(tup1)
    print(sorted(tup1))

    print("*****************************************")
    lis2=[(1,2),(2,3),(2,4,7,2),(9,5),(8,6),(8,6,7)]
    print("original list->")
    print(lis2)
    lis2.sort(key=my_func)
    print("new list")
    print(lis2)

