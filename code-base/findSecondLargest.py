if __name__ == '__main__':
    n = int(input()) #length of the scoreboard
    arr = map(int, input().split()) #all the score separating by space
    scoreList= [x for x in arr]
    maxNumber = max(scoreList [0],scoreList[1])
    sMaxNumber = min(scoreList[0],scoreList[1])
    for i in range(2,n):
        if(maxNumber==sMaxNumber and scoreList[i]<maxNumber):
            sMaxNumber=scoreList[i]
        elif(scoreList[i]>maxNumber):
            sMaxNumber=maxNumber
            maxNumber = scoreList[i]
        elif(scoreList[i]>sMaxNumber and scoreList[i]!=maxNumber):
            sMaxNumber=scoreList[i]
    print(sMaxNumber)