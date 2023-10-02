def add_to_list(val, list=[]):
    list.append(val)
    return list


def reverse_string(str):
    return str[::-1]


def testing_done():
    tuple1 = 5
    tuple2 = (5,)
    list1 = [1, 2, 3]
    list2 = list1
    print(list1, list2, sep=", ")
    list1[0] = [1, 4, 3]
    print(list1, list2, sep=", ")

def testing_required():
    text='Python'
    print(f"{text:#>10}")
    print(f"{text:!<11}")
    print(f"{text:<10}")  # Left-align in a field of width 10
    print(f"{text:^10}")  # Center-align in a field of width 10

    # Floating-Point Formatting
    value = 3.14159265359
    print(f"{value:.2f}")  # Format with 2 decimal places

    # Integer Formatting
    number = 42
    print(f"{number:05d}")  # Format as a 5-digit zero-padded integer

    # Alternate Form
    hex_value = 255
    print(f"{hex_value:#x}")  # Format as a hexadecimal number with "0x" prefix

    print(f"{number:+}")  # Include a plus sign for positive numbers
    print(f"{number:-}")  # redundant previous format will work for every scenarios

    # Other
    large_number = 1234567891011
    print(f"{large_number:,.2f}")  # Add thousands separators and format with 2 decimal places

if __name__ == "__main__":
    testing_required()
