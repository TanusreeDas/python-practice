def split_and_join(line):
    line=line.split(" ")    #this will split the words and separator is " "
    line="-".join(line)     #now this will add "-" between all the splitted words
    print ('Hello ' + line  + '! You just delved into python')
    return line

if __name__ == '__main__':
    line = input()
    i, c=input().split()
    print(i)
    print(c)
    result = split_and_join(line)
    print(result)