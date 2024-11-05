def rotate(mat):
    arr1 = []
    for i in range(len(mat)):
        arr2 = []
        for j in range(len(mat) - 1, -1, -1):
            arr2.append(mat[j][i])
        arr1.append(arr2)
    mat[:] = arr1
