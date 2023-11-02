# Given square matrix return diagonal difference
# Time O(n)
# Space O(1)

def diagonalDifference(arr):
    ld = 0
    rd = 0
    
    for i in range(len(arr)):
        ld += arr[i][i]
        rd += arr[i][len(arr)-1-i]
    
    return abs(ld-rd)