d = {'a': 1, 'b': None, 'c': [1, 2]}
k = 'c'

def get_elen(d, k):
    for i in d:
        if i in k:
            return d[k]

print(get_elen(d, k))