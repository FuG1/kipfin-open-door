import numpy as np
arrey = np.random.randint (0, 2, (4, 4))
def transposeMatrix(inputMatrix, t, rows):
    for p in range(rows):
        for q in range(rows):
            t[p][q] = inputMatrix[q][p]
def checkingSymmetric(inputMatrix, rows):
    t = [[0 for q in range(len(inputMatrix[0]))]
         for p in range(len(inputMatrix))]
    transposeMatrix(inputMatrix, t, rows)
    for p in range(rows):
        for q in range(rows):
            if (inputMatrix[p][q] != t[p][q]):
                return False
    return True
inputMatrix = arrey
if (checkingSymmetric(inputMatrix, 3)):
    print("Симметричная")
else:
    print("не симметричная")
print(arrey)



