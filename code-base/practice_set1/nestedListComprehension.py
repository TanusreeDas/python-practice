import time

if __name__=="__main__":
    a=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    '''create a pivot list where row will be converted to colum 
    and columns will be converted to rows, here the o/p will be
    [
        [1,5,9],
        [2,6,10],
        [3,7,11],
        [4,8,12]
    ]'''

    #my logic
    '''b= [
            [row[0][0],row[1][0],row[2][0]],
            [row[0][1],row[1][1],row[2][1]],
            [row[0][2],row[1][2],row[2][2]],
            [row[0][3],row[1][3],row[2][3]]
        ]
        for i in range(0,column-1,1)
            for j in range(0,row-1,1)
                row[j][i]
    '''

    start_time=time.time()
    b=list()
    for i in range(0, len(a[0]) , 1):
        row=list()
        for j in range(0, len(a) , 1):
            row.append(a[j][i])
        b.append(row)
    print(b)
    total_time=time.time()-start_time
    print("total time taken by method1 is->")
    print(total_time)

    #now using comprehension
    start_time=time.time()
    b1=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))] #first method
    print(b1)
    total_time=time.time()-start_time
    print("total time taken by method2 is->")
    print(total_time)

    start_time=time.time()
    b2=[[row[i] for row in a] for i in range(len(a[0]))]#simpler method
    print(b2)
    total_time=time.time()-start_time
    print("total time taken by method3 is->")
    print(total_time)

    #From the performance it is clear that the last method is the fastest