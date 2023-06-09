import json

print('-------------------------------------------------------')
print('triple sum to zero')
input = [-3, 0, 1, 2, -1, 1, -2]
print(f'input unsorted array:  [{input}]. ')


# sort the array so its easier to find duplicates its not like binary search since we are moving the pointers
# incrementally or decrementally by 1 not saying left = mid + 1 etc
# sorting the array is O (n * logN) and we are searching the entire array for two sum to zero for each
# n so that would be n^2. so for time its O(nlogn) + n^2 which is just n^2 and that is way better than n^3
# space complexity would be O(n)

def triple_sum_to_zero(arr):
    arr.sort()  # n(log(n))
    print(json.dumps(arr))
    triplets = []
    for i in range(0, len(arr) - 2, 1):
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
