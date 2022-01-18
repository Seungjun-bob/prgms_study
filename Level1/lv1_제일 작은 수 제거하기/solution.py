def solution(arr):
    idx_m = arr.index(min(arr))
    del arr[idx_m]
    if len(arr) == 0 :
        return [-1]
    else:
        return arr