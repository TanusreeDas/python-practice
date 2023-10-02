'''insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.'''

if __name__ == '__main__':
    arr=list()
    mainList=list()
    N = int(input())
    for i in range(N):
        arr.append(input())
    for i in arr:
        itemList=i.split(" ")
        firstItem=itemList[0]
        if(firstItem=='insert'):
            index = int(i.split(" ")[1])
            e = int(i.split(" ")[2])
            mainList.insert(index,e)
        elif(firstItem=='print'):
            print(mainList)
        elif (firstItem == 'remove'):
            e = int(i.split(" ")[1])
            mainList.remove(e)
        elif (firstItem == 'append'):
            e = int(i.split(" ")[1])
            mainList.append(e)
        elif(firstItem=='sort'):
            mainList.sort()
        elif (firstItem == 'pop'):
            mainList.pop()
        elif(firstItem=='reverse'):
            mainList.reverse()


