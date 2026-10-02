def flatten(n_in, l:list = None):
    if l is None:
        l = []
    if isinstance(n_in, list):
        for item in n_in:
            flatten(item, l)
    else:
        l.append(n_in)
        
    return l
            
n_flatten = ([1, [2, [3, 4], 5], 6, [7]])

print(flatten(n_flatten))

