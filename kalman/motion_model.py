# Implementation of various Motion Models

import math
import numpy as np
import sympy as sp

def constant_velocity_model():
    """
    Function to define constant velocity model in x and y directions

    The state vector is defined as:
    x = [[px],      Position in x-direction
         [py],      Position in y-direction
         [vx],      Velocity in x-direction
         [vy]]      Velocity in y-direction

    Parameters
    ----------
    None

    Returns
    -------
    A   : Discretized Constant Velocity Model
    """
    T = sp.symbols('T')
    A = sp.Matrix([[0, 0, 1, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]])
    A = sp.exp(A*T)

    return A

def constant_acceleration_model():
    """
    Function to define constant acceleration model in x and y directions

    The state vector is defined as:
    x = [[px],      Position in x-direction
         [py],      Position in y-direction
         [vx],      Velocity in x-direction
         [vy],      Velocity in y-direction
         [ax],      Acceleration in x-direction
         [ay]]      Acceleration in y-direction

    Parameters
    ----------
    None
    
    Returns
    -------
    A   : Discretized Constant Acceleration Model
    """
    T = sp.symbols('T')
    A = sp.Matrix([[0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]])
    A = sp.exp(A*T)

    return A


def coordinated_turn_model():
    """
    Function to define coordinated turn model

    The state vector is defined as:
    x = [[  x  ],      Position in x-direction
         [  y  ],      Position in y-direction
         [  v  ],      Velocity
         [theta],      Heading
         [omega]]      Yaw Rate 

    Parameters
    ----------
    None
    
    Returns
    -------
    A   : Discretized Constant Acceleration Model
    """
    x, y, v, th, om, T = sp.symbols('x y v theta omega T')
    F = sp.Matrix([[x + T*v*sp.cos(th)],
                   [y + T*v*sp.sin(th)],
                   [        v         ],
                   [    th + T*om     ],
                   [       om         ]])

    return F

"""
def constant_heading_and_velocity_model():
    print("Text")

def contant_turn_rate_and_acceleration_model():
    print("Text")

def linear_bicycle_model_single_track():
    print("Text")
"""