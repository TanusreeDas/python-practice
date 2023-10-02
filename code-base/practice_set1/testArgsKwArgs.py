if __name__=="__main__":
    def argument_function(a,*names,**details):
        counter=0;
        print("we will show name and details for {} students".format(a))
        print("student names are :")
        for name in names:
            counter+=1
            print(str(counter)+".",name)
        age,home,school,status = details.values()
        print("they are from",home+"'s",school,"school")

    argument_function(4,"tanusree","Kamolika","Dipesh","Rajesh",
                      age="23",home="barasat",school="govt",status="poor")

    def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
        print("kwarg_1:", kwarg_1)
        print("kwarg_2:", kwarg_2)
        print("kwarg_3:", kwarg_3)


    kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
    #some_kwargs(**kwargs)