# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

N = int(input("Enter total number: "))

myList = input("Enter list of numbers separated with space: ")
myList = myList.split(" ")
L = list(map(lambda item: int(item), myList))

N = len(L)


def mean(n, l):
    sums = 0
    for i in l:
        sums += i
    return round(sums/n, 1)


def median(n, l):
    l.sort()

    if n % 2 == 0:
        index2 = int(n / 2)
        index1 = index2 - 1
        index = (l[index1] + l[index2]) / 2
        return round(index*1.0, 1)
    else:
        index = int((n-1) / 2)
        return round(l[index]*1.0, 1)


def mode(l):
    l.sort()
    myDict = {}
    resultant = {}
    for i in l:
        if i not in myDict:
            myDict[i] = 0

        myDict[i] += 1

        if myDict[i] > 1:
            resultant[i] = myDict[i]

    resultant_keys = list(resultant.keys())
    resultant_values = list(resultant.values())

    if len(resultant_keys) == 0:
        return l[0]
    else:
        duplicate_found = []
        MAX = resultant_values[0]
        MAX_INDEX = 0
        for i in range(len(resultant_values)):
            if resultant_values[i] > MAX:
                MAX = resultant_values[i]
                MAX_INDEX = i
            elif resultant_values[i] == MAX and i != 0:
                duplicate_found.append(i)
                duplicate_found.append(MAX_INDEX)

        if len(duplicate_found) > 0:
            duplicate_found = list(dict.fromkeys(duplicate_found))
            answer_list = list(map(lambda x : resultant_keys[x], duplicate_found))
            return min(answer_list)
        else:
            return resultant_keys[MAX_INDEX]


# L = []
# a = [10, 12, 18, 6, 3, 1]
# b = [list(range(36, 41)), list(range(41, 46)), list(range(46, 51)),list(range(51, 56)),list(range(56, 61)), list(range(61, 66))]
# for i in range(len(b)):
#     for j in range(a[i]):
#         L += b[i]

#
print("Mean", mean(len(L), L))
print("Median", median(len(L), L))
print("Mode", mode(L))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
