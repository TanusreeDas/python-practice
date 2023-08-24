from collections import namedtuple

def useOfNamedTuple(strings):
    namedtuple1= namedtuple('courses','name, importance')
    assignedNamedTuple1= namedtuple1('python','very Important')
    print(assignedNamedTuple1)

def sampleSet(strings):
    print("We are going to do some testing on a random set")
    newSet=set(strings)
    anotherSet= set([1,2,3])
    #sampleSet1={1,5,6,2,2}
    newSet.pop()
    newSet.add(6)
    newSet.update(anotherSet)
    newSet.discard(4) #will not throw error if it is not a member
    newSet.remove(6)#will throw error if you try to remove an non member
    print(newSet)
    print((anotherSet))

def sampleList(strings):
    print("We are going to do some testing on a random list")
    newList=list(strings)
    newList.reverse()
    print(newList.count("h"))
    print(newList)

def sampleTuple(strings):
    print("We are going to do some testing on a random list")
    newTuple = tuple(strings)
    print(newTuple.index('h',1,8)) #throws error if not found
    print(newTuple)

def sampleDict(strings):
    print("We are going to do some testing on a random list")
    sampleDict1={'book name':'python', 'book rating':5,'unique number':strings}
    print((sampleDict1))

if __name__=='__main__':
    #useOfNamedTuple()
    s='abcdefgh'
    print("real String= "+s)
    sampleSet(s)
    sampleList(s)
    sampleTuple(s)
    sampleDict(s)