"""This is a question from AoC 2024"""

A = ""
B = ""

rules = [tuple(map(int, i.split('|'))) for i in A.splitlines()]
updates = [tuple(map(int, i.split(','))) for i in B.splitlines()]

TOTAL = 0

def make_graph(adj_list) :
    """Function to make a graph from a list of edges"""
    graph = {}
    for src, dest in adj_list :
        if src in graph :
            graph[src].append(dest)
        else :
            graph[src] = [dest]
    return graph

rules = make_graph(rules)

for u in updates :
    FLAG = True
    for i in range(len(u)-1) :
        if not FLAG :
            break
        for j in range(i+1, len(u)) :
            A, B = u[i], u[j]
            if A in rules[B] :
                FLAG = False
                break
    if not FLAG :
        pass

print(TOTAL)
