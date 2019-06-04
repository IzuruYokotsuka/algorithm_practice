import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
    return arr


if __name__ == '__main__':
    num_list = [random.randrange(10) for i in range(10)]
    print("before bubble sort")
    print(num_list)
    print("after bubble sort")
    print(bubble_sort(num_list))


# bubble sortの由来
# 泡が浮かびあがってくるかのごとく
# 小さいデータが徐々に集まってくる
