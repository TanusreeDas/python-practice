if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append(list((name,score)))

#Code which will find out second highest number
    '''if(len(records)>1):
        if (records[0][1] > records[1][1]):
            maxNum=records[0][1]
            secondMaxNumber=records[1][1]
        else:
            maxNum=records[1][1]
            secondMaxNumber=records[0][1]

        for row in records:
            if (row[1] > maxNum):
                secondMaxNumber = maxNum
                maxNum = row[1]
            elif (row[1] > secondMaxNumber and row[1] != maxNum):
                secondMaxNumber = row[1]

        b=[row[0] for row in records if row[1]==secondMaxNumber]
        b.sort()
        for i in b:
            print(i)'''


#Code which will find out second lowest number
    if(len(records)>1):
        if (records[0][1] > records[1][1]):
            lowestNum=records[1][1]
            secondLowestNumber=records[0][1]
        else:
            lowestNum=records[0][1]
            secondLowestNumber=records[1][1]

        for row in records:
            if (row[1] < lowestNum):
                secondLowestNumber = lowestNum
                lowestNum = row[1]
            elif (secondLowestNumber==lowestNum and row[1] >lowestNum):
                secondLowestNumber=row[1]
            elif (row[1] < secondLowestNumber and row[1] != lowestNum):
                secondLowestNumber = row[1]

        b=[row[0] for row in records if row[1]==secondLowestNumber]
        b.sort()
        for i in b:
            print(i)