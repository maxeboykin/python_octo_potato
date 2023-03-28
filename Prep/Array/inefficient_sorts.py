print("-------------------------------------------------------")
print("Insertion Sort")
input = [2, 8, 5, 3, 9, 4]

print(f'Sort the array via insertion sort {input}')
print("----------------------")


# all are O(N)^2 for different reasons
# selection sort: for selecting the remaining items that have not been sorted + find the min and switch with left ptr
# insertion sort is worst case when an array starts in decreasing order, we need to swap each item
# insertion sort is like i, picking an idx and swapping as you go to first index I for idx
# bubble sort is like taking an element and bubbling it up until its not higher than the element to the right of it

def bubble_sort(arr):
    for left in range(0, len(arr), 1):
        for right in range(left, len(arr) - 1, 1):
            if arr[right] > arr[right + 1]:
                swap(arr, right, right + 1)

    return arr


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


print("----------------------")
print("Bubble Sort")
print(bubble_sort(input))
print("----------------------")
print("Selection Sort")
print(selection_sort(input))
print("----------------------")
print("Insertion Sort")
print(insertion_sort(input))
