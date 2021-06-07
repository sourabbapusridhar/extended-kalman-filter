# Implementation of Testing

import os
import argparse
import numpy as np
from utils import read_yaml, write_yaml

def test_vehicle_estimator(configurationFilePath):
    """
    Entry point for testing vehicle state estimators.

    Parameters
    ----------
    configurationFilePath   : str
                              Path to the user defined configuration file

    Returns
    -------
    None
    """
    defaultConfigurationFilePath = str(os.path.abspath("config\\default.yml"))
    configurationFilePath = str(os.path.abspath(configurationFilePath))
    print("Path to the configuration file is: {}".format(configurationFilePath))

    defaultConfiguration = read_yaml(defaultConfigurationFilePath)
    userDefinedConfiguration = read_yaml(configurationFilePath)

    print("Default Configuration is as follows: {}".format(defaultConfiguration))
    print("User defined Configuration is as follows: {}".format(userDefinedConfiguration))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Implementation to test various vehicle state estimators")
    parser.add_argument("-c", "--configFilePath", type=str, default="config\\default.yml", help="Path to the configuration file (Default Value: config/default.yml)")
    args = parser.parse_args()

    test_vehicle_estimator(configurationFilePath=args.configFilePath)
