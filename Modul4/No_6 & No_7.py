Data1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

#Nomer. 6
def binSe(target):
    low = 0
    high = len(A)

    while low < high:
        mid = (high + low) // 2
        if Data1[mid] == target:
            return "Target pada indeks " + str(mid)
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

#Nomer. 7
Data2 = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binSe2(target):
    low = 0
    high = len(B)
    x = []

    while low < high:
        if Data2[low] == target:
            x.append(low)
            low+=1
        else:
            low+=1
    return x
