'''This over - allocates proportional to the list size, making room for additional growth.
The over - allocation is mild, but is enough to give linear - time amortized behavior over a long
sequence of appends() in the presence of a poorly - performing system realloc().
The growth pattern is: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...     '''

if __name__ == "__main__":
    lst = []

    #when len=0 list it self need 40 bytes
    print(lst.__sizeof__())
    #when len=1 so increment will be 4 i.e.4*8=32 so size will be 40+32=72
    # and now we will have (4-0)=4 new slots, so same size will be for next four elements
    lst.append(4)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(6)
    print(lst.__sizeof__())
    lst.append(7)
    print(lst.__sizeof__())
    #now it has to create again so it will be 8 i.e. 8*(8-4)=32 so size will be 72+32=104
    # and now we will have (8-4)=4 new slots, so same size will be for next four elements
    lst.append(8)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    #now it has to create again so it will be 16 i.e. 8*(16-8)=64 so size will be 104+64=168
    # and now we will have (16-8)=8 new slots, so same size will be for next eight elements
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    lst.append(5)
    print(lst.__sizeof__())
    #now it has to create again so it will be 16 i.e. 8*(25-16)=72 so size will be 168+72=240
    # and now we will have (25-16)=9 new slots, so same size will be for next nine elements
    lst.append(5)
    print(lst.__sizeof__())



