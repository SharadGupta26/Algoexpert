def min_efforts_to_collect_books(A, B):
    A.sort(reverse=True)
    n = len(A)
    merge_count = [0] * n
    efforts = 0

    for i in range(1, n):
        j = i - 1
        while j >= 0 and merge_count[j] == B:
            j -= 1

        if j >= 0:
            efforts += A[i] * (merge_count[j] + 1)  # Efforts required to merge the current stack with the previous one
            A[j] += A[i]  # Merge the stacks by updating the size of the previous stack
            merge_count[j] += 1  # Update the merge_count for the previous stack

    return efforts

# Example usage:
A = [1,2,3]
B = 1
result = min_efforts_to_collect_books(A, B)
print(result)
