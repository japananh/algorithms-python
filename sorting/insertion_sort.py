arr = [66, -83, -24, 95, 105, -44, -111, -121, 125, 6, -74, 193, 23, -104, -26, 32, 72, 65, 0, 186, 131, -120, -87, 122, 163, 49, -11, 52, -113, 108, 17, 135, -4, 30, -91, 123, 117, -109, 27, 90, -33, 88, -107, 113, -38, -58, -43, 99, -63, 146, 170, -8, 14, 149, 26, 54, -68, 180, 53, 87, 118, -16, 127, 197, 109, 35, 4, 64, 178, -114, 21, -17, 174, 177, 187, 78, 158, -115, 145, 68, -20, 39, 44, 115, 37, 98, -102, -127, 154, 86, -125, -77, 94, -133, 16, -56, -86, 12, 140, -
       90, -69, 3, 141, -128, 199, -29, 156, 164, -21, 15, -67, -42, -3, -84, -22, -13, -7, 175, 41, 107, 157, -37, 56, -28, 77, 97, 165, -49, -130, 63, 67, -31, 73, -78, 24, 200, 198, -5, -72, 2, 20, -12, 8, -2, 191, 50, 101, 58, -89, 70, 13, 120, 152, -103, 184, 104, 10, 103, 151, 75, -110, 40, 166, 195, -19, 60, 69, 47, 22, -117, 19, -85, -64, -71, -100, 38, 185, 153, -126, -54, 171, 100, 168, -112, 160, 57, -116, 155, -79, 169, 114, 176, 188, 79, -23, -55, 18, 82, 132, -101]

'''
    Best-case: O(n)
    Worst-case: O(n2)
    Avarage-case: O(n2)
'''


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if (arr[j - 1] > arr[j]):
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
            else:
                continue
    return arr


def binary_search(arr, num, low, high):
    if low >= high:
        return low + 1 if num > arr[low] else low

    mid = round((low + high) / 2)

    if num == arr[mid]:
        return mid + 1

    if num > arr[mid]:
        return binary_search(arr, num, mid + 1, high)

    return binary_search(arr, num, low, mid - 1)


'''
    Best-case: O(n)
    Worst-case: O(nlogn)
    Avarage-case: O(nlogn)
'''


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        location = binary_search(arr, key, 0, i - 1)

        if location < i:
            for j in range(i, location, -1):
                arr[j] = arr[j - 1]
            arr[location] = key

    return arr


result1 = insertion_sort(arr)
result2 = binary_insertion_sort(arr)

# print('result1 =', result1)
# print('result2 =', result2)
