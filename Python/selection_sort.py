#selection sort 

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    print(selection_sort(arr))