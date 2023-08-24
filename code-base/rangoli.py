
def print_rangoli_tannu(size):
    row=size*2-1
    column=size*4-3

    for i in range(row):
        list1 = []
        for j in range(row):
            if (i >= j):
                if (size > j):
                    list1.append(chr(96 + size - j))
                else:
                    list1.append(chr(98 + j - size))
            else:
                list1.append("-")
        print("-".join(list1))

alphabet = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli1(size):
    snip = alphabet[:size][::-1]
    width = (((size * 2) - 1) * 2) - 1
    rows = []
    for i in range(size):
        row_letters = snip[:i+1]
        row_letters += row_letters[::-1][1:]
        rows.append("-".join(row_letters).center(width, "-"))
    rows = rows + rows[:size-1][::-1]
    print("\n".join(rows))

def print_rangoli2(size):
    sc = int(size - 1)
    top = top_l = mid_l = str()
    if (sc) == 0: print("a")
    else:
        for i in range(sc):
            top_l += (chr(98+sc-i) + "-" if i != 0 else "")
            top += ("-"*2*(sc-i) + top_l + chr(97+sc-i)+ top_l[::-1] + "-"*2*(sc-i)+ "\n")
            mid_l += (chr(97+sc-i)+ "-")
        print(top + mid_l + "a" + mid_l[::-1] + top[::-1])


if __name__ == '__main__':
    n = int(input())
    print_rangoli1(n)