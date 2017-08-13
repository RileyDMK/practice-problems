# I need to take an input string and return its longest palindrome substring.
# My initial thought on an algorithm is to traverse the string forward while
# traversing the string in reverse to automatically find the largest palindrome
# the first time one is detected. However, the issue I run into is that when
# this algorithm finds a small palindrome in the middle it returns the wrong
# answer. Therefore, I decided to go with a more brute force method of comparing
# substrings and updating a palindrom variable to contain the longest one found
# so far. This has a complexity of O(n^2) which is a bit less effecient then my
# first thought could have been but I think this way of doing it is okay. The
# code is also much shorter this way. I iterate through the string and compare
# every substring to its reverse to find each palindrome. If the palindrome is
# larger than the currently stored one, I set the "pal" variable to be the new
# palindrome. When the loop is finished, return "pal". Testing for an empty
# string just prints a blank line as expected. Strings with palindromes in them
# print the first of the largest size palindromes that they yeild.


def question2(a):
    pal = ""
    for i in xrange(len(a)):
        for j in xrange(0, i):
            temp = a[j:i + 1]
            if temp == temp[::-1] and len(temp) > len(pal):
                pal = temp
    return pal

a = "racecard"
b = ""
c = "sdfffaffdkfa"

print(question2(a))
print(question2(b))
print(question2(c))
