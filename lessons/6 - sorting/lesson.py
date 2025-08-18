import time
import random

# insertion sort
# O(n^2)
# memory O(1)
def insertion_sort(A):  
    l = len(A)

    if l <= 1:
        return A
    
    for i in range(1, l):
        value = A[i]
        j = i - 1
        
        while j >= 0 and value < A[j]:
            A[j + 1] = A[j]
            j -= 1
            
        A[j + 1] = value

    return A


# quick sort
# O(n log n) on average, O(n^2) in the worst case
# memory O(log n)
def quick_sort(A):  
    l = len(A)

    if l <= 1:
        return A
    
    pivot = A[l // 2]
    left = []
    mid = []
    right = []

    for value in A:
        if value < pivot:
            left.append(value)

        elif value > pivot:
            right.append(value)

        else:
            mid.append(value)

    return quick_sort(left) + mid + quick_sort(right)

# merge sort
# O(n log n)
# memory O(n)
def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1  
            
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def merge_sort(A):
    l = len(A)

    if l <= 1:
        return A
    
    mid = l // 2
    left_half = merge_sort(A[:mid])
    right_half = merge_sort(A[mid:])

    return merge(left_half, right_half)


random.seed(42)
n = 10000
values = [random.randint(1, 100) for _ in range(n)]

print("Insertion Sort:")
clock = time.time()
result = insertion_sort(values.copy())
print("Time:", time.time() - clock, "seconds")

print("Quick Sort:")
clock = time.time()
result = quick_sort(values.copy())
print("Time:", time.time() - clock, "seconds")

print("Merge Sort:")
clock = time.time()
result = merge_sort(values.copy())   
print("Time:", time.time() - clock, "seconds")
