# buuble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    arr = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    print(bubble_sort(arr))
