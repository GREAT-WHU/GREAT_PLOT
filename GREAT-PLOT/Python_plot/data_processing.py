'''
this script defines some functions for data process
'''
import math
import numpy as np


# define some consts
Aell = 6378137.000  # semi major axes [m]
G_PI = math.pi  # pi
R2D = 180.0 / G_PI  # rad to deg
D2R = G_PI / 180.0  # deg to rad
Finv = 298.257223563  # inverse flattening [-]

#data processing pare
def dataLoad(filepath: str):
    '''
    data load
    :param filepath: file path
    :return: lines
    '''
    file = open(filepath, 'r', errors='ignore')
    filedata = file.readlines()
    file.close()
    return filedata


def rms(series: list):
    """
    input a series and calculate the rms
    :param series
    :return: rms value
    """
    rms_val = 0
    for item in series:
        rms_val = rms_val + item * item
    rms_val = math.sqrt(rms_val / len(series))
    return rms_val


def convergence(series: list, lim, epochs):
    """
    input a series and calculate the convergence based on the designated lim and num
    :param series:
    :param lim: threshold to judge convergence
    :param num: consecutive epochs
    :return: index
    """
    for i in range(len(series) - epochs + 1):
        sub_list = []
        for ele in series[i: i + epochs]:
            sub_list.append(abs(ele))
        if max(sub_list) < lim:
            return i
    return len(series) - 1


def xyz2blh(xyz: list, is_degree=False):
    """
    from xyz to blh
    :param xyz:
    :param is_degree: whether to output b, l in degree
    :return: [b, l, h]
    """
    ell = [0, 0, 0]
    bell = Aell * (1.0 - 1.0 / Finv)
    e2 = (Aell * Aell - bell * bell) / (Aell * Aell)
    e2c = (Aell * Aell - bell * bell) / (bell * bell)
    ss = math.sqrt(xyz[0] * xyz[0] + xyz[1] * xyz[1])
    if ss == 0.0:
        ell[0] = -999
        ell[1] = -999
        ell[2] = -999
        return ell
    zps = xyz[2] / ss
    theta = math.atan((xyz[2] * Aell) / (ss * bell))
    sin3 = math.sin(theta) * math.sin(theta) * math.sin(theta)
    cos3 = math.cos(theta) * math.cos(theta) * math.cos(theta)
    ell[0] = math.atan((xyz[2] + e2c * bell * sin3) / (ss - e2 * Aell * cos3))
    ell[1] = math.atan2(xyz[1], xyz[0])
    nn = Aell / math.sqrt(1.0 - e2 * math.sin(ell[0]) * math.sin(ell[0]))
    ell[2] = ss / math.cos(ell[0]) - nn
    for i in range(100):
        nn = Aell / math.sqrt(1.0 - e2 * math.sin(ell[0]) * math.sin(ell[0]))
        hOld = ell[2]
        phiOld = ell[0]
        ell[2] = ss / math.cos(ell[0]) - nn
        ell[0] = math.atan(zps / (1.0 - e2 * nn / (nn + ell[2])))
        if math.fabs(phiOld - ell[0]) <= 1.0e-11 and math.fabs(hOld - ell[2]) <= 1.0e-5:
            if ell[1] < 0.0:
                ell[1] += 2 * G_PI
            if is_degree:
                ell[0] *= R2D
                ell[1] *= R2D
            return ell
    return ell


def xyz2neu(xyz: list, xyz_ref: list):
    """
    from xyz to neu
    :param xyz:
    :param xyz_ref: coordinate of ref site
    :return: [n, e, u]
    """
    neu = [0, 0, 0]
    ell = xyz2blh(xyz_ref)
    r = [xyz[0] - xyz_ref[0], xyz[1] - xyz_ref[1], xyz[2] - xyz_ref[2]]
    sinPhi = math.sin(ell[0])
    cosPhi = math.cos(ell[0])
    sinLam = math.sin(ell[1])
    cosLam = math.cos(ell[1])
    neu[0] = -sinPhi * cosLam * r[0] - sinPhi * sinLam * r[1] + cosPhi * r[2]
    neu[1] = -sinLam * r[0] + cosLam * r[1]
    neu[2] = +cosPhi * cosLam * r[0] + cosPhi * sinLam * r[1] + sinPhi * r[2]
    return neu


def exclude_outliers(series: list):
    """
    excluding outliers based on 3 std criterion
    :param series:
    :return:
    """
    result = series
    for i in range(10):
        new_list = []
        exclude = []
        _mean = np.mean(result)
        _std = np.std(result)
        for ele in result:
            if abs(ele - _mean) > 3 * _std:
                exclude.append(ele)
            else:
                new_list.append(ele)
        if len(exclude) == 0:
            return result
        result = new_list
    return result

