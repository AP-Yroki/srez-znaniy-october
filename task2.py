ref_list = [0, 1, 2, 3, 4, 5]
start = 4
num = 40
rep = 2

print(ref_list[start:])
def list_insert(ref_list, start, num, rep):
    return ref_list[:start] + [num] * rep + ref_list[start:] if len(ref_list) >= start else -1

print(list_insert(ref_list, start, num, rep))