def merge(arr, l, m, r, key):
    n1 = m - l + 1
    n2 = r - m

    L = list()
    R = list()

    for i in range(n1):
        L.append(arr[l + i])
    for i in range(n2):
        R.append(arr[m + 1 + i])

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if key(L[i]) <= key(R[j]):
            arr[k] = L[i]
            i += 1
        elif key(L[i]) > key(R[j]):
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        k += 1
        i += 1

    while j < n2:
        arr[k] = R[j]
        k += 1
        j += 1


def MergeSort(arr, l, r, key):
    if l < r:
        m = l + (r - l) // 2

        MergeSort(arr, l, m, key)
        MergeSort(arr, m + 1, r, key)
        merge(arr, l, m, r, key)


def BingoSort(arr):
    pass


def _sorted(arr, key=None, reverse=False, sortingAlgorithm="MergeSort"):
    if sortingAlgorithm == "MergeSort":
        l = 0
        r = len(arr) - 1
        MergeSort(arr, l, r, key)
    elif sortingAlgorithm == "BingoSort":
        pass
    else:
        raise ValueError("Choose between MergeSort and BingoSort!")

    if reverse:
        arr.reverse()

    return arr


class MyClass:
    def __init__(self, id, nume):
        self.__id = id
        self.__nume = nume

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def __str__(self):
        return str(self.__id) + ", " + self.__nume

    def __eq__(self, other):
        if self.__id == other.get_id() and self.__nume == other.get_nume():
            return True
        return False


p1 = MyClass(1, "Vali")
p2 = MyClass(2, "Serban")
p3 = MyClass(3, "Vasile")
l = list()
l += [p1, p2, p3]
for i in l:
    print(i)
sorted_arr = _sorted(l, key=lambda x: x.get_nume(), reverse=True)
for i in sorted_arr:
    print(i)
