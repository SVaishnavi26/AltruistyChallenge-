from collections import deque

def min_of_max_in_subarrays(arr, k):
    n = len(arr)
    if k > n:
        return -1  # Invalid case
    
    dq = deque()
    max_in_windows = []

    for i in range(k):
        # Remove elements smaller than the current from the back of the deque
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
    
    for i in range(k, n):
        # Add the maximum of the previous window
        max_in_windows.append(arr[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
    
  
    max_in_windows.append(arr[dq[0]])

    # Return the minimum of all maximums
    return min(max_in_windows)

k = int(input("Enter segment length (k): "))
n = int(input("Enter size of array (n): "))
arr = [int(input()) for _ in range(n)]

print(min_of_max_in_subarrays(arr, k))
