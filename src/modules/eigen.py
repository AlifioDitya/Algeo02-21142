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

def main():
    A = np.array([[3, 0], [8, -1]])
    print(qr_algorithm(A))
    
if __name__ == "__main__":
    main()