# A simple way to solve this problem is to iterate through s for every
# letter in t and produce a new string of the matched characters. This is
# O(n^2) efficiency in the worst case becuase this approach uses a nested for loop.
# In order to handle duplicate letters working properly, I create a copy of s
# and slice off letters I have already used from the copy whenever a match is made.
# If I don't do this, my function will give me false false matches. I then break
# the for loop to try and match the next letter in t. If the new temp string
# matches t then t is a substring of s and returns True. Otherwiswe return
# False.


def question1(s, t):
    temp = ""
    sCopy = s
    for i in t:
        for j in sCopy:
            if i == j:
                temp += j
                sCopy = sCopy[:sCopy.index(j)] + sCopy[sCopy.index(j) + 1:]
                # print(sCopy)
                break
    if t == temp:
        return True
    else:
        return False

test1s = ""
test1t = ""
test2s = "a"
test2t = "b"
test3s = "udacity"
test3t = "ad"
test4s = "udacity"
test4t = "add"

print(question1(test1s, test1t))
print(question1(test2s, test2t))
print(question1(test3s, test3t))
print(question1(test4s, test4t))
