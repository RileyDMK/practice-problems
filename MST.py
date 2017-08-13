# The input and output is an adjacency list. Some good test cases would be an empty list,
# a list containing a circuit, and a list with multiple routes that could be used.
# First I want to put every edge into a sorted list. After that, I want to iterate
# through the sorted edge list and a node when it isn't in the new output adjacency
# list and add previous connections. This method is a greedy lowest weight first
# algorithm. Complexity is O(n^2)


def question3(G):
    if G == {}:
        return "Empty list"

    F = {}
    edges = []
    seen = []

    for key, value in G.iteritems():
        for v in value:
            edges.append(((key, v[0]), v[1]))
    sEdges = sorted(edges, key=lambda x: x[1])
    vert = sEdges.pop(0)

    # Use the first item in sEdges as the start and add it to F and seen
    if vert[0][0] not in F:
        F[vert[0][0]] = [(vert[0][1], vert[1])]
        seen.append(vert[0][0])
        if vert[0][1] not in F:
            F[vert[0][1]] = [(vert[0][0], vert[1])]
            seen.append(vert[0][1])

    while(len(F) < len(G)):
        if vert[0][0] not in F:
            F[vert[0][0]] = [(vert[0][1], vert[1])]
            seen.append(vert[0][0])
            if vert[0][1] in seen:
                F[vert[0][1]].append((vert[0][0], vert[1]))
        vert = sEdges.pop(0)
    return F

test1 = {'A': [('B', 2), ('D', 1)],
         'B': [('A', 2), ('C', 5)],
         'C': [('B', 5)],
         'D': [('A', 1)]}

test2 = {'A': [('B', 1), ('C', 3)],
         'B': [('A', 1), ('C', 2)],
         'C': [('A', 3), ('B', 2)]}
test3 = {}
test4 = {'A': [('B', 1), ('C', 1)],
         'B': [('A', 1), ('C', 2), ('E', 3)],
         'C': [('B', 2), ('A', 1), ('D', 2)],
         'D': [('C', 2), ('E', 3)],
         'E': [('D', 3), ('B', 3)]}

print(question3(test1))
print(question3(test2))
print(question3(test3))
print(question3(test4))
