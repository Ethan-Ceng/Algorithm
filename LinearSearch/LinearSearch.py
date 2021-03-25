# encoding= utf-8
# 线性查找

def search(list, target):
    for index, item in enumerate(list):
        if item == target:
            return index

    return -1


searchList = [3, 100, 5, 13, 43, 45, 11, 8]
target = 11

targetIndex = search(searchList, target)

print(target, targetIndex)
