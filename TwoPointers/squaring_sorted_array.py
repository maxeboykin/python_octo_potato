print('-------------------------------------------------------')
print('squaring a sorted array')
input = [-2, -1, 0, 2, 3]
print(f'input array:  [{input}]. Please create a new array containing squares of all the numbers of the input array')
# move left all the way to the first negative integer in the array and right to the first non negative
# move left pointer left while right increases and asssess each value and move points accordingly
# time is O n and space is O n since we go through array once and have to construct new array of squares
def squaring_sorted_array(arr):
    results = []
    left = 0
    right = 0
    while right < len(arr) or left >= 0:
        while arr[right] < 0:
            right += 1
            left = right - 1
        if abs(arr[left]) < abs(arr[right]):
            insert = arr[left] * arr[left]
            results.append(insert)
            left -= 1
        else:
            insert = arr[right] * arr[right]
            results.append(insert)
            right += 1

    return results


print(squaring_sorted_array(input))
