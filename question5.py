# The inputs for this will be the starting node of a linked list and the mth
# numbered node from the end to find. The output is the data that the mth node
# holds. My thoughts are to set the first node as the mth node and update it
# to its next when it is m nodes away from the current node. This is O(n) because
# I may need to traverse every node to find the mth node.


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def makeList(n):
    root = Node(1)
    current = root
    if n > 1:
        for i in xrange(2, n + 1):
            current.next = Node(i)
            current = current.next
    return root


def question5(ll, m):
    if ll is None:
        return "Root does not exist"

    mth = ll
    current = ll
    count = 0

    while(current.next):
        count += 1
        # print current.data
        if count > m:
            mth = mth.next
            count = count - 1
        current = current.next

    count += 1
    #print("count: %s" % (count))
    if count > m:
        mth = mth.next

    if m > current.data:
        return "Not enough elements for mth to exist"
    return mth.data

size8 = makeList(8)
size1 = makeList(1)
size2 = makeList(2)
size3 = makeList(3)
print(question5(size8, 8))
print(question5(size8, 1))
print(question5(size1, 2))
print(question5(size2, 2))
print(question5(size3, 3))
print(question5(size3, 2))
