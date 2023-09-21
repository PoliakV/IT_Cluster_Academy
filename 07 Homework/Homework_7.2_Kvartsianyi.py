def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


data = [10, 2, 8, 5, 25, 30, 100, 9, 1]

print("Несортовано: ", data)

print("Сортовано: ", quick_sort(data))
