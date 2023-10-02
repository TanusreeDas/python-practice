if __name__=="__main__":
    a,b,c,d=(1,2,3,4)
    print (a)
    e,f,g=[5,[6],7]
    print(type(e))
    print(e+g)
    print(f)
    *args,=4,5,6
    print(type(args))

    tuple1=(1,2,3)
    tuple2=(4,5,6)
    newTuple=(tuple1,tuple2)
    anyTuple=(*tuple1,*tuple2)
    print((newTuple))
    print((anyTuple))

    a,b,c=(i**4 for i in range(3))
    print(a)
    print(b)
    print(c)

    p=1,2,3,4
    print(type(p))

    gen=(2**x for x in range(3))
    print(gen)
    *g,=gen
    print(g)

    '''firsrtName,*middleName,lastName=input().split(" ")
    print(firsrtName)
    print(middleName)
    print(lastName)'''

    _="tn"
    print(_)

    dict1={'a':1,'b':2}
    dict2={'c':3,'d':4}
   # dict3={dict1,dict2}
    dict4={**dict1,**dict2}
   # print(dict3)
    print(dict4)


if __name__!="__main__":
    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

        # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

        # Bottom Cone
    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
            thickness * 6))