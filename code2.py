def count_bees(s, startIndex, endIndex):
    n = len(s)
    q = len(startIndex)
    
    # Step 1: Preprocessing
    prefix_bees = [0] * (n + 1)
    nearest_left_flower = [-1] * n
    nearest_right_flower = [-1] * n
    
    # Compute prefix_bees
    for i in range(n):
        prefix_bees[i + 1] = prefix_bees[i] + (1 if s[i] == '*' else 0)
    
    # Compute nearest_left_flower
    last_flower = -1
    for i in range(n):
        if s[i] == '|':
            last_flower = i
        nearest_left_flower[i] = last_flower
    
    # Compute nearest_right_flower
    last_flower = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_flower = i
        nearest_right_flower[i] = last_flower
    
    # Step 2: Process queries
    results = []
    for i in range(q):
        start = startIndex[i] - 1  # Convert to 0-indexed
        end = endIndex[i] - 1      # Convert to 0-indexed
        
        # Find the nearest flowers
        left = nearest_right_flower[start]
        right = nearest_left_flower[end]
        
        # Count bees if there is a valid range
        if left != -1 and right != -1 and left <= right:
            count_bees = prefix_bees[right + 1] - prefix_bees[left]
            results.append(count_bees)
        else:
            results.append(0)
    
    return results

# Input
s = input("Enter the string: ")
n = int(input("Enter number of queries: "))
startIndex = [int(input()) for _ in range(n)]
endIndex = [int(input()) for _ in range(n)]

# Output
results = count_bees(s, startIndex, endIndex)
for res in results:
    print(res)
