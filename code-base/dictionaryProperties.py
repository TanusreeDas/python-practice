#check some dictionary datastructure properties
if __name__== "__main__":
    mutable_list=[4,5,6]
    immutable_tuple=(4,5,6)
    a={1:"amar naam",
       2:"amar boyosh",
       4:"amar address",
       3: 3,
       3:6,
       "sobar details":"janina cholbe kina",
       #mutable_list:"you know it wont work, keys has to be immutable",  #error got= TypeError: unhashable type: 'list'
       immutable_tuple:"this one should works, tuples are immutable"}
    a.update({1:"sobar naam"})
    print(list(a))
    print(a.keys())
    print(a.values())
    print(a.get("sobar details"))
    #print(sorted(a))   # not possible because keys has different datatypes
    a.pop(immutable_tuple)
    a.pop("sobar details")
    print(a.setdefault(9,5)) #If the key does not exist, insert the key, with the specified value, else do nothing
    a[10]="notun value add korchi"
    print(a.get(3))
    print(sorted(a))