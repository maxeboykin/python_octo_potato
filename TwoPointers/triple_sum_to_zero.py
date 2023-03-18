import json

print('-------------------------------------------------------')
print('triple sum to zero')
input = [-3, 0, 1, 2, -1, 1, -2]
print(f'input unsorted array:  [{input}]. ')


# move left all the way to the first negative integer in the array and right to the first non negative
# move left pointer left while right increases and asssess each value and move points accordingly
# time is O n and space is O n since we go through array once and have to construct new array of squares

def triple_sum_to_zero(arr):
    arr.sort()  # n(log(n))
    print(json.dumps(arr))
    triplets = []
    for i in range(0, len(arr), 1):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        _two_sum_to_zero(arr, -arr[i], i + 1, triplets)

    return triplets


def _two_sum_to_zero(arr, target, startIdx, triplets):
    right = len(arr) - 1
    left = startIdx
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1


print(triple_sum_to_zero(input))
