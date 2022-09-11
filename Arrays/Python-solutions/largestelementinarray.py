def largest_element(arr, n):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    return largest

if __name__ == '__main__':
    arr = [10, 2, 30 ,4, 3]
    n = len(arr)
    print(largest_element(arr, n))
