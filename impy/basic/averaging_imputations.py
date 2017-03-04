""" Mean/mode/median imputation methods """

import numpy as np

def mean_imputation(data):
    """ Substitute missing values with the mean of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xy = np.argwhere(np.isnan(data))
    for x_i, y_i in null_xy:
        row_wo_nan = data[:, [y_i]][~np.isnan(data[:, [y_i]])]
        new_value = np.mean(row_wo_nan)
        data[x_i][y_i] = new_value
    return data

def median_imputation(data):
    """ Substitute missing values with the mode of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set(null_xy.T[1])
    medians = {}
    for y_i in cols_missing:
        cols_wo_nan = data[:, [y_i]][~np.isnan(data[:, [y_i]])]
        median_y = np.median(cols_wo_nan)
        medians[str(y_i)] = median_y
    for x_i, y_i in null_xy:
        data[x_i][y_i] = medians[str(y_i)]

def mode_imputation(data):
    """ Substitute missing values with the mode of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xy = np.argwhere(np.isnan(data))
    modes = []
    for y_i in range(np.shape(data)[1]):
        unique_counts = np.unique(data[:, [y_i]], return_counts=True)
        max_count = np.max(unique_counts[1])
        mode_y = [unique for unique, count in np.transpose(unique_counts) \
                if count == max_count and not np.isnan(unique)]
        modes.append(mode_y)  # Appends index of column and column modes
    for x_i, y_i in null_xy:
        data[x_i][y_i] = np.random.choice(modes[y_i])
    return data