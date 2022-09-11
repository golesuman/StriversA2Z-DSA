def sorted_or_not(arr, n):
    flag = 0
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            flag = 1
    if flag == 1:
        return 0

    else:
        return 1

if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)

    print(sorted_or_not(arr, n))