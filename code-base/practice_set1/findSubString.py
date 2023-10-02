if __name__=="__main__":
    mainString=input()
    stringtoBeChecked=input()
    lenMainString=len(mainString)
    lenSmallString=len(stringtoBeChecked)
    flag=0

    newList=[mainString[i:i+lenSmallString] for i in range(lenMainString) if i+lenSmallString<=lenMainString]
    for i in newList:
            if(stringtoBeChecked == i):
                flag=flag+1

    print(newList)
    print(flag)

