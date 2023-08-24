import array as arr

if __name__ == "__main__":
    newArray = arr.array("i", [1, 2, 3, 4])
    newList = [5, 6, 7, 8]
    print(newArray)
    print(newList)
    anotherList = [10, 11]
    print(newList + anotherList)
    print(sum(newArray))
    for i in newArray:
        print(i)
