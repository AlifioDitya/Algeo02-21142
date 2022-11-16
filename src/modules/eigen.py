import numpy as np

def qrDecomp(mCov):
    N, M = mCov.shape
    Q = np.empty((N, N))
    u = np.empty((N, N))
    u[:, 0] = mCov[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    i = 1
    while (i < N):
        u[:, i] = mCov[:, i]
        for j in range(i):
            u[:, i] -= (mCov[:, i] @ Q[:, j]) * Q[:, j]
        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i])
        i += 1

    R = np.zeros((N, M))
    for i in range(N):
        for j in range(i, M):
            R[i, j] = mCov[:, j] @ Q[:, i]

    return Q, R

def eig(mCov):
    X = np.eye(mCov.shape[0])

    # loop sebanyak n matrixnya
    i = 0
    while (i < 120):
        Q,R = qrDecomp(mCov)
        X = X @ Q
        mCov = R @ Q   
        i += 1
    return np.diag(mCov), X     # Tuple of (eigenvalue, eigenvector)