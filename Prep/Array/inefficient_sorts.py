print("-------------------------------------------------------")
print("Insertion Sort")
input = [2, 8, 5, 3, 9, 4]

print(f'Sort the array via insertion sort {input}')
print("----------------------")


#
#
#
#

def selection_sort(arr):
    for left in range(0, len(arr), 1):
        cur_min_idx = left
        for right in range(left + 1, len(arr), 1):
            if arr[right] < arr[left]:
                cur_min_idx = right
        swap(arr, left, cur_min_idx)

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr), 1):
        j = i
        while j >= 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1

    return arr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print(insertion_sort(input))
print(selection_sort(input))