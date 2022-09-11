def second_largest(arr):
    large = arr[0]
    for num in arr:
        if num > large:
            large = num


    arr2 = []
    for num in arr:
        if num != large:
            arr2.append(num)
    
    if arr2:
        large2 = arr2[0]
        for num2 in arr2:
            if num2 > large2:
                large2 = num2

        return large2

    else:
        return -1



if __name__ == '__main__':
    arr = [20, 18 , 2, 1, 3]
    # arr2 = [123, 122]
    print(second_largest(arr))