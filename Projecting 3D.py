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

import camera
from numpy import *
from PIL import Image
from pylab import *
from scipy import *

# load points
points = loadtxt('house.p3d').T
points = vstack((points,ones(points.shape[1])))
# setup camera
P = hstack((eye(3),array([[0],[0],[-10]])))
cam = camera.Camera(P)
x = cam.project(points)
# plot projection
##figure()
##plot(x[0],x[1],'k.')
##show()

# create transformation
r = 0.05*random.rand(3)
rot = camera.rotation_matrix(r)
# rotate camera and project
figure()
for t in range(20):
    cam.P = dot(cam.P,rot)
    x = cam.project(points)
    plot(x[0],x[1],'k.')
show()

