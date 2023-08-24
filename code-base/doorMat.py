'''The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.'''

if __name__=="__main__":

    input1,input2=(input()).split(" ",1)
    n=int(input1)
    m=int(input2)
    flag=1
    mid_value = n // 2

    pattern1="-"
    pattern2=".|."
    pattern3="WELCOME"

    if(n*3==m and 5<n<101  and 15<m<303):
        for i in range(n):
            if (i < mid_value):
                print((pattern1 * int((m - ((flag) * len(pattern2))) / 2)) + (pattern2 * int((flag)))
                      + ((pattern1 * int((m - ((flag) * len(pattern2))) / 2))))
                flag = flag + 2
            elif (i == mid_value):
                print((pattern1 * int((m - len(pattern3)) / 2)) + pattern3 + (pattern1 * int((m - len(pattern3)) / 2)))
            else:
                flag = flag - 2
                print((pattern1 * int((m - ((flag) * len(pattern2))) / 2)) + (pattern2 * int((flag)))
                      + ((pattern1 * int((m - ((flag) * len(pattern2))) / 2))))
