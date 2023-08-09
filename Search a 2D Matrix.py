# Matrix is sorted from low to high, from [0][0] to [m][n]
# each row starts with a higher number than the previous row ends with
# return True if "target" is in the matrix, in O(log(mn)) time.


def bsearch_iter(arr, target):
    low = 0
    high = len(arr) - 1
    while low != high:
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid
    return arr[low] == target
def bsearch_recur(arr, low, high, target):
    if low == high:
        return arr[low] == target
    mid = (low + high) // 2
    if target > arr[mid]:
        return bsearch_recur(arr, mid + 1, high, target)
    elif target < arr[mid]:
        return bsearch_recur(arr, low, mid - 1, target)
    else:
        return mid
test = [2, 4, 6, 8, 10, 12, 14]
print(bsearch_recur(test, 0, len(test) - 1, 4))
'''
def search(matrix, target):
    m, n = len(matrix) - 1, len(matrix[0]) - 1
    row_low, row_high = 0, m
    while not(matrix[row_low][0] <= target <= matrix[row_high][0]):
        if target < matrix[(row_low + row_high) // 2]:
            row_high = (row_low + row_high) // 2 - 1
        else:
            row_low = (row_low + row_high) // 2'''
