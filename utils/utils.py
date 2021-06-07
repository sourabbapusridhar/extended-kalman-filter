# Implementation of random functionality

import os
import yaml

def read_yaml(yamlPath):
    """
    Function to read a YAML file.

    Parameters
    ----------
    yamlPath        : str
                      Path to the YAML file

    Returns
    -------
    yamlContents    : dict
                      Contents of the YAML file
    """
    with open(str(os.path.abspath(yamlPath)), "r") as yamlFile:
        yamlContents = yaml.safe_load(yamlFile)

    return yamlContents

def write_yaml(yamlPath, yamlContents):
    """
    Function to write into a YAML file.

    Parameters
    ----------
    yamlPath        : str
                      Path to the YAML file
    yamlContents    : str
                      Contents of the YAML file

    Returns
    -------
    None
    """
    with open(str(os.path.abspath(yamlPath)), "w") as yamlFile:
        yaml.dump(yamlContents, yamlFile)

