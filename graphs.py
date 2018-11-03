def partition_maker(func, mod):
    sets = [set([i,func(i) % mod]) for i in range(mod)]
    completion = True
    while completion:
        completion = False
        for s in sets:
            for d in sets:
                if not s == d and not s & d == set([]) and not completion:
                    s.update(d)
                    sets.remove(d)
                    completion = True
    return sets

def get_part_of(partition, value):
    for part in partition:
        if value in part:
            return part
    return -1

def graph_maker(func, mod):
    graph = [(val, func(val) % mod) for val in range(mod)]
    return graph
