lst = [None, None, 1, [], (), {}, None]
i = 0
test = 0

def de_none(lst):
    test = 0
    for i in lst:
        if i == None:
            test += 1

    for i in range(test):
        lst.remove(None)
    return lst

print(de_none(lst))
