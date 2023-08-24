def print_formatted(number):
    #your code goes here
    #first findout the length of binary number of n
    #gap between two print is "that length"+1-length(current number)
    #decimal is that number
    #octal is oct(that number)
    #hexadecimal is hex(that number)
    #binary is bin(that number)
    gap=len(bin(number))-2
    length_number=len(str(number))
    for i in range(1,number+1,1):
        decimal_version=str(i).rjust(gap,' ')
        octal_version=str(oct(i))[2:].rjust(gap+1,' ')
        hexa_version=(str(hex(i))[2:]).upper().rjust(gap+1,' ')
        binary_version=str(bin(i))[2:].rjust(gap+1,' ')
        print(decimal_version+octal_version+hexa_version+binary_version)

def another_way(number):
    for i in range(1, number+1):
        lens = len(str(bin(number)))-2
        pad = ' '
        a = str(i)
        b = str(oct(i))
        c = str(hex(i)).upper()
        d = str(bin(i))
        print(f'{a.rjust(lens,pad)} {b[2:].rjust(lens,pad)} {c[2:].rjust(lens,pad)} {d[2:].rjust(lens,pad)}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    another_way(n)