# n is the original, unsorted list. These are sample numbers:

n = [3, 3, 323, 324, 65657678, 23334555555, 4, 23, 2, 1, 45, 7, 56, 2]
iA, jB = 0, 1
emplist = []
reflst = []
lenlst = []
D = []
E = []

# This function uses recursion to break the original list into pairs, which are sorted


def sort(lst):
    global emplist, reflst
    lstref = len(list(lst[:]))
    reflst.append(lstref)
    # Base case, when list has been split into 2 numbers
    if len(lst) == 2:
        if lst[0] > lst[1]:
            lst = lst[::-1]
        emplist.append(lst)
        if len(emplist)*2 == reflst[0]:
            return True
    # Alternate base case, incase of an odd number end case.
    elif len(lst) == 3:
        lst1 = list(lst)
        lst2 = []
        lst1.remove(max(lst))
        lst1.remove(min(lst))
        lst2.append(min(lst))
        lst2.append(lst1[0])
        lst2.append(max(lst))
        emplist.append(lst2)
    else:
        listA = lst[::2]
        listB = lst[1::2]
        sort(listA)
        sort(listB)
# The sort() function returns a nested list of sorted pairs of the original unsorted list

# The purpose of this function is to merge by order until it is the length of the original unsorted list, but sorted


def mergesort(list_):
    global iA, jB, D, E, reflst, lenlst
    i, j = 0, 0
    lenlst.append(len(list_))
    # basecase, if only one merge is left
    if reflst[0] == 2 or reflst[0] == 3:
        print(list_[0])
    elif len(D) == 2:
        iA, jB = 0, 1
        A = list_[iA]
        B = list_[jB]
        nlen = len(A) + len(B)
        iA += 2
        jB += 2
        C = []
        for k in range(0, nlen):
            if j+1 > len(B) and i+1 > len(A):
                continue
            elif i+1 > len(A):
                C.append(B[j])
                j += 1
            elif j+1 > len(B):
                C.append(A[i])
                i += 1
            elif A[i] < B[j]:
                C.append(A[i])
                i += 1
            elif B[j] < A[i]:
                C.append(B[j])
                j += 1
            elif B[j] == A[i]:
                C.append(B[j])
                j += 1
        print(C)
    else:
        if lenlst[0] == 3 and len(list_[iA]) == 3:
            A = list_[iA]
            B = D[0]
            D.pop(0)

        else:
            A = list_[iA]
            B = list_[jB]
        nlen = len(A) + len(B)
        iA += 2
        jB += 2
        C = []
        for k in range(0, nlen):
            if j+1 > len(B) and i+1 > len(A):
                continue
            elif i+1 > len(A):
                C.append(B[j])
                j += 1
            elif j+1 > len(B):
                C.append(A[i])
                i += 1
            elif A[i] < B[j]:
                C.append(A[i])
                i += 1
            elif B[j] < A[i]:
                C.append(B[j])
                j += 1
            elif B[j] == A[i]:
                C.append(B[j])
                j += 1
        D.append(C)
        if len(D) == 2:
            mergesort(D)
        elif nlen == reflst[0]:
            print(D[0])
        else:
            mergesort(list_)


sort(n)
mergesort(emplist)
