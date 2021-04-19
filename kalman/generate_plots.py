# Implementation of Plotting Functions

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

def plot_animation(x_true, x_est, z):
    plt.plot(x_true[0], x_true[1], '.r')
    plt.plot(x_est[0], x_est[1], '.b')
    plt.plot(z[0], z[1], '+g')
    plt.grid(True)
    plt.pause(0.001)
    

def plot_ellipse(x_est, p_est):
    phi = np.linspace(0, 2 * math.pi, 100)
    p_ellipse = np.array([[p_est[0, 0], p_est[0, 1]], [p_est[1, 0], p_est[1, 1]]])
    x0 = 3 * sqrtm(p_ellipse)
    xy_1 = np.array([])
    xy_2 = np.array([])
    for i in range(100):
        arr = np.array([[math.sin(phi[i])], [math.cos(phi[i])]])
        arr = x0 @ arr
        xy_1 = np.hstack([xy_1, arr[0]])
        xy_2 = np.hstack([xy_2, arr[1]])
    plt.plot(xy_1 + x_est[0], xy_2 + x_est[1], 'r')
    plt.pause(0.00001)


def plot_final(x_true_cat, x_est_cat, z_cat):
    fig = plt.figure()
    f = fig.add_subplot(111)
    f.plot(x_true_cat[0:, 0], x_true_cat[0:, 1], 'r', label='True Position')
    f.plot(x_est_cat[0:, 0], x_est_cat[0:, 1], 'b', label='Estimated Position')
    f.plot(z_cat[0:, 0], z_cat[0:, 1], '+g', label='Noisy Measurements')
    f.set_xlabel('x [m]')
    f.set_ylabel('y [m]')
    f.set_title('Linear Kalman Filter - Constant Acceleration Model')
    f.legend(loc='upper left', shadow=True, fontsize='large')
    plt.grid(True)
    plt.show()


def postpross(x_true, x_true_cat, x_est, p_est, x_est_cat, z, z_cat, show_animation, show_ellipse, show_final):
    if show_animation == 1:
        plot_animation(x_true, x_est, z)
        if show_ellipse == 1:
            plot_ellipse(x_est[0:2], p_est)
    if show_final == 1:
            plot_final(x_true_cat, x_est_cat, z_cat)
