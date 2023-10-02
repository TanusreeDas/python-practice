x= 5
y=10
for i in range(5,10):
    print(i)
    if(i==7):
        print("i=7")
        continue
else:
    print("whatever")
print ("now it will show error = "+str(sum(range(5,10))))