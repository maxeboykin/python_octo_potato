print("-------------------------------------------------------")
print("Subsets")
input1 = [1, 3]
input2 = [1, 5, 3, 2]
print(f'Given a set with distinct elements, find all of its distinct subsets. Input: [{input}]')
print("----------------------")


def find_subsets(arr):
    subsets = [[]]
    for i in range(0, len(arr), 1):
        n = len(subsets)
        for j in range(0, n, 1):
            cur_elem = subsets[j]
            replicated_elem = list(cur_elem)  # returns a new reference to a new array (similar to slice)
            replicated_elem.append(arr[i])
            subsets.append(replicated_elem)

    return subsets


print(find_subsets(input1))
print("----------------------")
print(find_subsets(input2))