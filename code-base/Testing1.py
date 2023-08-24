'''class Testing1:
    def __init__(self, work=None, action=None):
        self.work=work
        self.action=action

    """def alarm(lists):
        match lists:
            case [('Morning'|'Evening'|'Night') as workTime, action]:"""

    def alarm(lists):
        if 'tannu' in lists :
            print ('here is my {} dear'.format(lists))
        else :
            print('here is my {} not so dear'.format(lists))

    alarm('tannu')'''


import datetime
import textwrap
if __name__ == "__main__":
    '''try:
        fname="Tanusree"
        lname="Das"
        weight="weight"
        ascii_checking="TanusreeDÁš"
        list1=[1,2,3]
        dt=datetime.datetime.now()
        d={"weight":50,":p":60}
        print("hello {fname} {lname} {0}".format("Singh",fname="fname",lname=lname)) #positional and keyword formatting
        print("Weight in tons {0[:p]}".format(d)) #get item formatting for dictionaries
        print(format(10,"7d")) #simple replacement field
        print("My name is {0:2}".format('Fred','ok'))
        print(open('out.txt','w').__dir__())
        print("new format is {forma[0]}".format(forma=list1))
        print("this one will show ascii value of->{fname} as {fname!a}".format(fname=ascii_checking))
        print("date time string format is {0!s}".format(dt))
        print("date time repr format is {0!r}".format(dt))
    except:
        print("error")
    else:
        print('I am just testing random formats {:.9f}'.format(1))'''
    list1=[1,2,3,4]
    tuple1=(1,2,3,4)
    dict1={"name":"Tanusree","surname":"Das","age":10}
    set1={1,2,3,4}
    #print("4th item in set is->",list(set1)[3])
    #show firstdata from list
    '''print("second data in the list is-> {0[1]}, first data in tuple is-> {1[0]},"
          "third data in the dict is-> {2[age]}".format(list1,tuple1,dict1))

    print("un packing complete dictionary-> name:{name},surname:{surname},age:{age}".format(**dict1))

    print (f"""first dictionary item is {dict1['name']}
first item in list is {list1[0]}""")

    print(f"first dictionary item is {dict1['name']}"
    f"first item in list is {list1[0]}")'''
    '''print('tannu'*-7)
    s="tanusreeDas"
    print(s[::-3])

    text1="""trying textwrap lets see how it works! there are ultiple ways
    but I will use only two ways, textwrap.wrap and textwrapper class on textwrap
    module. lets see. finger crossed"""
    s1=textwrap.wrap(text1,width=20)
    print(s1)
    wrapper=textwrap.TextWrapper(width=20)
    s2=wrapper.wrap(text1)
    print(s2)
    list2=list(['tanusreedas','another'])
    print(list2[0])'''

    set1=set({2,3})
    set2={2,3}
    print(set1)
    print(set2)
    print(set1 is set2)
