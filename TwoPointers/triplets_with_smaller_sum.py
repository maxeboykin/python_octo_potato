import json

print('-------------------------------------------------------')
print('triple with smaller sum')
input = [-1, 0, 2, 3]
target = 3
print(f'Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + '
      f'arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such '
      f'triplets.Input: {input} Target: {target}')


# // this takes O(N * logN) to sprt
# // n^2 for the looping, one for first for loop and one for searchPair
# // asymptotically this makes it O^n2 and O(N) space

def triple_with_smaller_sum(arr, target):
    arr.sort()  # n(log(n))
    print(json.dumps(arr))
    count = 0
    for i in range(0, len(arr) - 2, 1):
        count += _two_sum_with_smaller_sum(arr, target - arr[i], i + 1)

    return count


def _two_sum_with_smaller_sum(arr, upper_bound, start_idx):
    inner_count = 0
    right = len(arr) - 1
    left = start_idx
    while left < right:  # dont double count indices
        current_sum = arr[left] + arr[right]
        if current_sum < upper_bound:
            inner_count += right - left  # major part of the question
            left += 1
        else:
            right -= 1
    return inner_count


print(triple_with_smaller_sum(input, 3))
