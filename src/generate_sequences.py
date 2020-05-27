# Implementation for Sequence Generation Functions

import numpy as np
from scipy.linalg import sqrtm

def generate_linear_state_sequence(x0, P0, A, B, u0, Q0):
    """
    Function to generate linear state sequence

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    A   : Motion Model
    B   : Control Matrix
    u0  : Input
    Q0  : Motion Model Noise

    Returns
    -------
    x   : Generated State Sequence
    """
    x = A @ np.random.normal(x0, sqrtm(P0), (len(x0), 1)) + np.random.normal(np.zeros((len(Q0), 1)), sqrtm(Q0), (len(Q0), 1)) + B @ u0

    return x

def generate_linear_measurement_sequence(x0, P0, H, R):
    """
    Function to generate linear measurement sequence

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    H   : Measurement Model
    R   : Measurement Noise

    Returns
    -------
    y   : Generated Measurement Sequence
    """
    y = H @ np.random.normal(x0, sqrtm(P0), (len(x0), 1)) + np.random.normal(np.zeros((len(R), 1)), sqrtm(R), (len(R), 1))

    return y

def generate_nonlinear_state_sequence(x0, P0, F, B, u0, Q0):
    """
    Function to generate non-linear state sequence

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    F   : Motion Model
    B   : Control Matrix
    u0  : Input
    Q0  : Motion Model Noise

    Returns
    -------
    x   : Generated State Sequence
    """
    x = F(x0) + np.random.normal(np.zeros((len(Q0), 1)), sqrtm(Q0), (len(Q0), 1)) + B(u0)

    return x


def generate_nonlinear_measurement_sequence(x0, P0, H, R):
    """
    Function to generate linear measurement sequence

    Parameters
    ----------
    x0  : Prior Mean
    P0  : Prior Covariance
    H   : Measurement Model
    R   : Measurement Noise

    Returns
    -------
    y   : Generated Measurement Sequence
    """
    y = H(x0) + np.random.normal(np.zeros((len(R), 1)), sqrtm(R), (len(R), 1))

    return y
