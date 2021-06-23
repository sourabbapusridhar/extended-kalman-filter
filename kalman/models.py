# Implementation of Kalman Filter Models

class StateEstimator:
    def __init__(self):
        pass

class CV(StateEstimator):
    def __init__(self):
        pass

class CA(StateEstimator):
    def __init__(self):
        pass

class CT(StateEstimator):
    def __init__(self):
        pass

class CTRV(StateEstimator):
    def __init__(self):
        pass

class CTRA(StateEstimator):
    def __init__(self):
        pass

def state_estimator(motionModel):
    """
    Function to return a state estimator class based on motion model input.

    Parameters
    ----------
    motionModel     : str
                      Name of the motion model for which the corresponding state estimator is required

    Returns
    -------
    cls             : StateEstimator
                      State estimator class corresponding to the motion model input
    """
    for cls in StateEstimator.__subclasses__():
        if cls.__name__ == motionModel:
            return cls

    raise Exception("[ERROR] Motion Model {} is not vallid!".format(motionModel))