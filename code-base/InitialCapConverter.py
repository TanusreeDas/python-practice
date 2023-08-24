import os

def solve(s):
    *splited_names,=s.split(" ")
    new_name=""
    for modified_names in splited_names:
        new_name=new_name+str(modified_names).capitalize()+" "
    modified_name = new_name.rstrip(" ")
    return modified_name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()