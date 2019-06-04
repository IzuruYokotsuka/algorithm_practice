import random


def quick_sort(arr):
    if len(arr) == 0:
        return []
    small = quick_sort([a for a in arr[1:] if a <= arr[0]])
    large = quick_sort([a for a in arr[1:] if a > arr[0]])

    return small + [arr[0]] + large


if __name__ == '__main__':
    num_list = [random.randrange(10) for i in range(10)]
    print("before quick sort")
    print(num_list)
    print("after quick sort")
    print(quick_sort(num_list))
