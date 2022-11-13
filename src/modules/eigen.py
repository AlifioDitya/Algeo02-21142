import numpy as np

def qr_algorithm(A, tol=0.0001):
    Q, R = np.linalg.qr(A)
    previous = np.empty(shape=Q.shape)
    for i in range(500):
        previous[:] = Q
        X = R @ Q
        Q, R = np.linalg.qr(X)
        if np.allclose(X, np.triu(X), atol=tol): 
            break
    return R @ Q

def isDiagonal(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i != j:
                if abs(arr[i][j]) > 0.001:
                    return False
    return True

def qrFactorization(arr):
    temp = arr
    i = 0
    while(True):
        Q,R = np.linalg.qr(temp)
        temp = np.dot(R, Q)
        if(isDiagonal(temp)):
            break
        else:
            i += 1
    return temp

def EigVal(arr):
    nEigVal = 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i == j):
                temp = arr[i][j]
                if(abs(temp) <0):
                    temp = 0
                print("Eigen Value"+str(nEigVal) +": " + str(temp))
                nEigVal += 1
    


def main():
    A = np.array([[3, 0], [8, -1]])
    print(qr_algorithm(A))
    EigVal(qrFactorization(A))
    
if __name__ == "__main__":
    main()