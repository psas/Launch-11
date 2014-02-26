#!/usr/bin/env python
from scipy.signal import resample
from scipy.signal import correlate
import numpy
import os

accels = []
alphas = []

# raw data see https://github.com/psas/flight_data-2010.10.17 
with open('../../../data/flight_data-2010.10.17/roll/raw/output_trim.csv', 'r') as f_in:
    for line in f_in:
        li = line.split(',')
        accel = float(li[1])
        angle = int(li[3].strip())

        accels.append(-accel+34570)
        alphas.append(angle)


# original sample rate (roll sample rate)
r_in = 1000  # Hz

#desired sample rate (sample for IMU data)
r_out = 128 #hz

# find numnber of desired samples
nsamples = (len(alphas) * r_out)/r_in

# resample
accels
alphas_resampled = resample(alphas, nsamples)
accels_resampled = resample(accels, nsamples)


opal_accels = []
# get opal data
with open('model_data.csv', 'r') as f_in:

    for line in f_in:
        li = line.split(',')
        opal_accels.append(float(li[4]))


opal_accels = numpy.array(opal_accels)
z = correlate(accels_resampled, opal_accels)

offset =  (len(z)/2) - numpy.argmax(z)

print offset
