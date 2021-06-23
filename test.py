# Implementation of Testing

import os
import argparse
import numpy as np
from kalman import state_estimator
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
    overallConfiguration = userDefinedConfiguration.copy()

    for key in ["measurement_configuration", "data_configuration", "output_configuration"]:
        if key in defaultConfiguration:
            overallConfiguration.update({key: defaultConfiguration[key]})

    overallModels = overallConfiguration["model_configuration"]["motion_model"].replace(","," ").split()
    for modelId, model in enumerate(overallModels):
        
        overallConfiguration["model_configuration"]["motion_model"] = model
        overallConfiguration["model_configuration"]["covariance_matrix"] = np.array(userDefinedConfiguration["model_configuration"]["covariance_matrix"], dtype=float)
        #assert (overallConfiguration["measurement_configuration"]["covariance_matrix"].shape == (overallConfiguration["measurement_configuration"]["measurement_variables"], overallConfiguration["measurement_configuration"]["measurement_variables"])), ("[ERROR] Measurement Covariance Matrix Dimensions are Incorrect!!")

        overallConfiguration["measurement_configuration"]["measurement_variables"] = int(overallConfiguration["measurement_configuration"]["measurement_variables"])
        overallConfiguration["measurement_configuration"]["covariance_matrix"] = np.array(userDefinedConfiguration["measurement_configuration"]["covariance_matrix"], dtype=float)
        #assert (overallConfiguration["measurement_configuration"]["covariance_matrix"].shape == (overallConfiguration["measurement_configuration"]["measurement_variables"], overallConfiguration["measurement_configuration"]["measurement_variables"])), ("[ERROR] Measurement Covariance Matrix Dimensions are Incorrect!!")

        overallConfiguration["data_configuration"]["data_directory"] = str(os.path.abspath(overallConfiguration["data_configuration"]["data_directory"]))
        overallConfiguration["data_configuration"]["data_file_type"] = "CSV" if defaultConfiguration["data_configuration"]["data_file_type"] == "CSV" else None
        overallConfiguration["data_configuration"]["data_variables"] = int(overallConfiguration["data_configuration"]["data_variables"])
        #assert (overallConfiguration["measurement_configuration"]["measurement_variables"] == overallConfiguration["data_configuration"]["data_variables"]), ("[ERROR] Mistmatch in number of measurement variables and number of data points")

        overallConfiguration["output_configuration"]["animation"] = True if userDefinedConfiguration["output_configuration"]["animation"] == True else False
        overallConfiguration["output_configuration"]["save_output"] = True if userDefinedConfiguration["output_configuration"]["save_output"] == True else False
        overallConfiguration["output_configuration"]["output_directory"] = str(os.path.abspath(overallConfiguration["output_configuration"]["output_directory"]))

        print("***********************************************")
        print("Current Configuration is as follows: ")
        for key, value in overallConfiguration.items():
            print("{}: {}".format(key,value))
        print("***********************************************")

        vehicleStateEstimator = state_estimator(overallConfiguration["model_configuration"]["motion_model"])

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Implementation to test various vehicle state estimators")
    parser.add_argument("-c", "--configFilePath", type=str, default="config\\default.yml", help="Path to the configuration file (Default Value: config/default.yml)")
    args = parser.parse_args()

    test_vehicle_estimator(configurationFilePath=args.configFilePath)
