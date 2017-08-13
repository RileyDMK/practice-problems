# For this question, the input is a tree matrix and the output is the
# value of the lowest common ancestor node. What I need to do is traverse
# in one direction from each node until I find one of the given end nodes
# and return either that node or the root of both given nodes. This is
# possible due to the properties of a binary search trees. Some good test1s
# cases are when the tree is empty, when the lowest common ancestor is
# n1 or n2, and when the lowest common ancestor is a root of n1 and n2.


def question4(T, r, n1, n2):
    if T == []:
        return "Tree is empty"
    if r is None:
        return "There is no root"
    if r < n1 and r < n2:
        for i, val in enumerate(T[r]):
            if val == 1:
                if r < i:
                    return question4(T, i, n1, n2)

    if r > n1 and r > n2:
        for i, val in enumerate(T[r]):
            if val == 1:
                if r > i:
                    return question4(T, i, n1, n2)

    return r
print(question4([], 0, 0, 0))
print(question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4))
print(question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                0,
                1))
print(question4([[0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                2,
                1))
