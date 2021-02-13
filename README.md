# Vehicle State Estimation

The goal of this project is to design and implement a vehicle state estimator using a linear Kalman Filter, an extended Kalman filter, an Unscented Kalman Filter, and a Cubature Kalman Filter.

The vehicle state estimation and localization is calculated using two [Intertial Measurement Units](https://cdn-shop.adafruit.com/datasheets/BST_BNO055_DS000_12.pdf) and one [GPS sensor](https://www.swiftnav.com/latest/piksi-multi-hw-specification). 

## Requirements
The code is based on Python3 (>=3.7). There are a few dependencies to run the code. The major libraries are listed as follows:
* Numpy (>=1.18.5)
* Matplotlib (>=3.3.3)

## Installation Guide
To install the anaconda environment, navigate to the repository folder, and run the following command in the command prompt:

`conda env create -f environment.yml`

## Execution Guide
1. To activate the Conda environment, please run the following command in the command prompt:

`conda activate kalman`

2. *To be added*

3. To deactivate the Conda environment, please run the following command in the command prompt:

`conda deactivate`

## Clean-up Guide
To remove the anaconda environment, navigate to the repository folder, and run the following command in the command prompt:

`conda remove --name kalman --all`

## References

- [Velocity estimation in land vehicle applications](https://pdfs.semanticscholar.org/d301/5a6f939b8ac4563d8c2b23da3457106e2c33.pdf)
- [The Extended Kalman Filter: An Interactive Tutorial for Non-Experts](https://simondlevy.academic.wlu.edu/kalman-tutorial/)
- [Kalman Filters: A step by step implementation guide in python](https://towardsdatascience.com/kalman-filters-a-step-by-step-implementation-guide-in-python-91e7e123b968)

## Authors
* Sourab Bapu Sridhar

## License

This project is released under the terms of [MIT License](LICENSE).