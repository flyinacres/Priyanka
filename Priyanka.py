__author__ = 'rfischer'


def findSegment(l, index):

    """

    :rtype : object
    """
    test_val = l[index]
    while index < len(l) and l[index] <= test_val + 4:
        index += 1

    return index


N = input()

W = [int(x) for x in raw_input().split(' ')]

W.sort()

#Need to change this so that she gets _all_ the toys
#answer should be her total cost
min_total_segments = 0
i = 0
while i < N:
    i = findSegment(W, i)
    min_total_segments += 1


print min_total_segments