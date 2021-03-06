# encoding= utf-8
# 排序算法
# (1)冒泡排序；
# (2)选择排序；
# (3)插入排序；
# (4)希尔排序；
# (5)归并排序；
# (6)快速排序；
# (7)基数排序；
# (8)堆排序；
# (9)计数排序；
# (10)桶排序。


# 选择排序法  O(n^2)
# array[i...n) 未排序 array[0...i) 已排序
# array[i...n) 中最小值要放到 array[i] 的位置
def chooseSort(list):
    for i in range(len(list)):
        minIndex = i

        for j in range(i + 1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        
        # swap value
        list[i], list[minIndex] = list[minIndex], list[i]

    print('选择排序：', list)



# 插入排序 O(n) ~ O(n^2)
# array[0, i) 已排序 array[i...n) 未排序
# 把 arr[i] 放到合适的位置

def insertSort(list):
    for i in range(len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        
        list[j+1] = key

    print('插入排序', list)



list = [64, 25, 12, 22, 11]

insertSort(list)