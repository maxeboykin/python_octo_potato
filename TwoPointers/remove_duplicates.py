print('-------------------------------------------------------')
print('remove Duplicates')
input = [1, 1, 2, 3, 5, 6, 7, 7, 10]
print(f'input array:  [{input}]. Please remove duplicates. Algo Monster')


def remove_duplicates(arr):
    left = 0
    for right in range(0, len(arr), 1):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]

    return left + 1


print(remove_duplicates(input))
