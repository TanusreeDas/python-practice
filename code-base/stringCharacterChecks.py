if __name__=="__main__":
    fAlphanumeric=False
    fAlpha=False
    fDigit=False
    fLowerCase=False
    fUpperCase=False
    s=input()
    for c in s:
        if(c.isalnum()==True and fAlphanumeric==False):
            fAlphanumeric=True
        if(c.isalpha()==True and fAlpha==False):
            fAlpha=True
        if(c.isdigit()==True and fDigit==False):
            fDigit=True
        if(c.islower()==True and fLowerCase==False):
            fLowerCase=True
        if(c.isupper()==True and fUpperCase==False):
            fUpperCase=True
    print(fAlphanumeric)
    print(fAlpha)
    print(fDigit)
    print(fLowerCase)
    print(fUpperCase)