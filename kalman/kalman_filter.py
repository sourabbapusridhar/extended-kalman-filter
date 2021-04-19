# Implementation of Kalman Filter Functions

import math
import numpy as np
from scipy.linalg import sqrtm

def linear_kalman_predict(x0, P0, A, B, u0, Q0):
    """
    Function to perform linear Kalman Prediction Step

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    A   : Linear Motion Model 
    B   : Control Matrix
    u0  : Prior Input
    Q0  : Motion Model Noise Covariance

    Returns
    -------
    x   : Predicted State Mean
    P   : Predicted State Covariance
    """
    x = A @ x0 + B @ u0
    P = A @ P0 @ np.transpose(A) + Q0

    return x, P

def linear_kalman_update(x0, P0, y, H, R):
    """
    Function to perform linear Kalman Update Step

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    y   : Measurement
    H   : Measurement Model
    R   : Measurement Noise Covariance

    Returns
    x   : Updated State Mean
    P   : Updated State Covariance
    -------
    """
    S = H @ P0 @ np.transpose(H) + R
    K = P0 @ np.transpose(H) @ np.linalg.inv(S)
    v = y - H @ x0

    x = x0 + K @ v
    P = P0 - K @ S @ np.transpose(K)

    return x, P


def linear_kalman_filter(x0, P0, A, B, u0, Q0, y, H, R):
    """
    Function to perform linear Kalman Filtering

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    A   : Linear Motion Model 
    B   : Control Matrix
    u0  : Prior Input
    Q0  : Motion Model Noise Covariance
    y   : Measurement
    H   : Measurement Model
    R   : Measurement Noise Covariance

    Returns
    -------
    x   : Filtered State Mean
    P   : Filtered State Covariance
    """

    xPred, PPred =  linear_kalman_predict(x0, P0, A, B, u0, Q0)
    x, P = linear_kalman_update(xPred, PPred, y, H, R)

    return x, P

def calculate_sigma_points(x0, P0, type):
    """
    Function to calculate sigma points

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    type: Type of non-linear filter (EKF, UKF, CKF)

    Returns
    -------
    SP  : Sigma Points
    W   : Weights
    """
    n = len(x0)
    if (type == 'UKF'):

        SP_XY = np.zeros((n, 2*n+1))
        SP_W0 = 1-n/3
        SP_XY[:,1] = x0              
        SqrtP = sqrtm(P0)
        SP_W = SP_W0

        for i in range(len(P0[0])):   
            SP_XY[:,i+1] = x0 + math.sqrt((n)/(1-SP_W0)) @ SqrtP[:,i]
            SP_XY[:,i+n+1] = x0 - math.sqrt((n)/(1-SP_W0)) @ SqrtP[:,i]

        for i in range(2*len(x0)):
            SP_Wi = (1-SP_W0)/(2*n)       
            SP_W = np.hstack((SP_W, SP_Wi))


    elif(type == 'CKF'):

        SP_XY = np.zeros((n, 2*n))
        SqrtP = sqrtm(P0)
        SP_W = np.empty([n,1])

        for i in range(len(P0[0])):   
            SP_XY[:,i+1] = x0 + math.sqrt(n) @ SqrtP[:,i]
            SP_XY[:,i+n+1] = x0 - math.sqrt(n) @ SqrtP[:,i]

        for i in range(2*len(x0)):
            SP_Wi = (1-SP_W0)/(2*n)       
            SP_W = np.hstack((SP_W, SP_Wi))
        
    else:
        raise ValueError('Wrong Kalman Filter Used!')

    return SP_XY, SP_W


def nonlinear_kalman_predict(x0, P0, F, B, u0, Q0, type):
    """
    Function to perform non-linear Kalman Prediction Step

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    F   : Nonlinear Motion Model 
    B   : Control Matrix
    u0  : Prior Input
    Q0  : Motion Model Noise Covariance
    type: Type of non-linear filter (EKF, UKF, CKF)

    Returns
    -------
    x   : Predicted State Mean
    P   : Predicted State Covariance
    """
    n = len(x0)    
    if(type == 'EKF'):

        fx, dfx = F(x0, u0)
        x = fx
        P = dfx @ P0 @ np.transpose(dfx) + Q0
        
    elif(type == 'UKF'):

        SP, W = calculate_sigma_points(x0, P0, type)

        x = np.zeros((n,1))
        for i in range(len(W[0])):
            x = x + F(SP[:,i]) @ W[i]

        P = Q0
        for i in range(len(W[0])):
            P = P + (F(SP[:,i]) - x) @ np.transpose(F(SP[:,i]) - x) @ W[i]

    elif(type == 'CKF'):

        SP, W = calculate_sigma_points(x0, P0, type)

        x = np.zeros((n,1))
        for i in range(len(W[0])):
            x = x + F(SP[:,i]) @ W[i]

        P = Q0
        for i in range(len(W[0])):
            P = P + (F(SP[:,i]) - x) @ np.transpose(F(SP[:,i]) - x) @ W[i]

    else:
        raise ValueError('Wrong Kalman Filter Used!')
    
    return x, P


def nonlinear_kalman_update(x0, P0, y, H, R, type):
    """
    Function to perform non-linear Kalman Update Step

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    y   : Measurement
    H   : Measurement Model
    R   : Measurement Noise Covariance
    type: Type of non-linear filter (EKF, UKF, CKF)

    Returns
    x   : Updated State Mean
    P   : Updated State Covariance
    -------
    """
    if(type == 'EKF'):

        hx, dhx = H(x0)
        S = dhx @ P0 @ np.transpose(dhx) + R
        K = P0 @ dhx @ np.linalg.inv(S)
        x = x + K @ (y - hx)
        P = P - K @ S @ np.transpose(K)

    elif(type == 'UKF'):

        [SP, W] = calculate_sigma_points(x0, P0, type)
        yhat = np.zeros(np.shape(y))

        for i in range(len(W[0])):
            yhat = yhat + H(SP[:,i]) @ W[i]

        Pxy = np.zeros(len(P), len(R))
        for i in range(len(W[0])):
            Pxy = Pxy + (SP[:,i] - x0) @ np.transpose(H(SP[:,i]) - yhat) @ W[i]

        S = R
        for i in range(len(W[0])):
            S = S + (H(SP[:,i]) - yhat) @ np.transpose(H(SP[:,i]) - yhat) @ W[i]

        x = x + Pxy @ np.linalg.inv(S) @ (y - yhat)
        P = P - Pxy @ np.linalg.inv(S) @ np.transpose(Pxy)


    elif(type == 'CKF'):

        [SP, W] = calculate_sigma_points(x0, P0, type)
        yhat = np.zeros(np.shape(y))

        for i in range(len(W[0])):
            yhat = yhat + H(SP[:,i]) @ W[i]

        Pxy = np.zeros(len(P), len(R))
        for i in range(len(W[0])):
            Pxy = Pxy + (SP[:,i] - x0) @ np.transpose(H(SP[:,i]) - yhat) @ W[i]

        S = R
        for i in range(len(W[0])):
            S = S + (H(SP[:,i]) - yhat) @ np.transpose(H(SP[:,i]) - yhat) @ W[i]

        x = x + Pxy @ np.linalg.inv(S) @ (y - yhat)
        P = P - Pxy @ np.linalg.inv(S) @ np.transpose(Pxy)

    else:
        raise ValueError('Wrong Kalman Filter Used!')

    return x, P


def nonlinear_kalman_filter(x0, P0, F, B, u0, Q0, y, H, R, type):
    """
    Function to perform non-linear Kalman Filtering

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    F   : Nonlinear Motion Model 
    B   : Control Matrix
    u0  : Prior Input
    Q0  : Motion Model Noise Covariance
    y   : Measurement
    H   : Measurement Model
    R   : Measurement Noise Covariance

    Returns
    -------
    x   : Filtered State Mean
    P   : Filtered State Covariance
    """
    xPred, PPred =  nonlinear_kalman_predict(x0, P0, F, B, u0, Q0, type)
    x, P = nonlinear_kalman_update(xPred, PPred, y, H, R, type)

    return x, P