#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      S.A
#
# Created:     16/04/2017
# Copyright:   (c) S.A 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def my_calibration(sz):
    row,col = sz
    fx = 2555*col/2592
    fy = 2586*row/1936
    K = diag([fx,fy,1])
    K[0,2] = 0.5*col
    K[1,2] = 0.5*row
    return K