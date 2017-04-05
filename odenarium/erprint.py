def erprint(x):
    if type(x) != str:
        x = str(x)
    print(len(x)*'-')
    print(x)
    print(len(x)*'-')
