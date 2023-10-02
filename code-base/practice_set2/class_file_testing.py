class Whatever:
    ...


def get_whatever():
    x = 40

    def g():
        nonlocal x
        x = 20

    g()
    print("x=", x)


if __name__ == "__main__":
    get_whatever()
    print(type(Whatever))
