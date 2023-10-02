if __name__ == "__main__":
    d = dict()
    l = ["apples", "oranges", "kiwi", "pears", "grapes", "banana", "cherry", "apples"]
    # d.setdefault(fruits,fruits) for fruits in l if fruits not in d
    [d.setdefault(c, c) for c in l if c not in d]
