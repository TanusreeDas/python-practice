from collections import OrderedDict
def merge_the_tools_sol1(string, k):
    #print(string+str(k))
    splitedList=list(string)

    def remove_duplicate(smallString):
        uniqueList=OrderedDict()
        for c in smallString:
            if c not in uniqueList:
                uniqueList[c]=0
            else:
                uniqueList[c]=uniqueList[c]+1
        print(''.join([str(item) for item in (list(uniqueList.keys()))]))

    for j in range(0,len(string),k):
        tempList=list()
        for i in range(j,j+k,1):
            tempList.append(splitedList[i])
        remove_duplicate(tempList)

def merge_the_tool_sol2(string,k):

    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([d.setdefault(c, c) for c in part if c not in d]))

def merge_the_tools_sol3(string,k):
    num_subsegments = int(len(string) / k)
    for index in range(num_subsegments):
        t = string[index * k: (index + 1) * k]
        u = ""
        for c in t:
            if c not in u:
                u+=c
        print(u)

def remove_all_duplicate():
    string="bbabcaaccdbaabababc"
    s=""
    for c in string:
        if c not in s:
            s+=c
    print(s)

if __name__ == '__main__':
    #remove_all_duplicate()
    string, k = input(), int(input())
    merge_the_tool_sol2(string, k)

