#!/usr/bin/env python
import numpy
import os.path
from scipy.integrate import simps
from scipy.signal import resample, correlate
import sys

data_dir = sys.argv[1]

# original data. See: <https://github.com/psas/flight_data-2010.10.17>
opal_file = os.path.join(data_dir, 'opal/Opal_launch_rotated.csv')
roll_file = os.path.join(data_dir, 'roll/raw/output_trim.csv')

opal_sample_rate =  128     # Hz
roll_sample_rate = 1000     # Hz



################################################################################
''' Opal '''

# read in opal data
columns = numpy.loadtxt(opal_file, delimiter=',', unpack=True)

opal_time  = columns[0]
opal_accel = columns[3]
opal_rate  = columns[6]

# calculate velocity and angular acceleration
velocity = [0]
altitude = [0]
angular_accel = [0]
for i in range(1, len(opal_accel)):
    altitude.append(simps(velocity, opal_time[:i]))
    velocity.append(simps(opal_accel[:i], opal_time[:i]))
    angular_accel.append(opal_rate[i] - opal_rate[i-1])
velocity = numpy.array(velocity)
angular_accel = numpy.array(angular_accel)



################################################################################
''' Roll '''

# read in roll data
columns = numpy.loadtxt(roll_file, delimiter=',', unpack=True, usecols=(0,1,2,3))

roll_accel = columns[1]
fin_angle  = columns[3]

# fix sign
roll_accel = numpy.multiply(roll_accel, -1)

# offset and normalize fin
fin_angle = numpy.subtract(fin_angle, 2**14 + 2**13)
fin_angle = numpy.multiply(fin_angle, 0.00003)


# find number of desired samples for file
nsamples = (len(roll_accel) * opal_sample_rate)/roll_sample_rate

# resample data to same timebase
roll_accel = resample(roll_accel, nsamples)
fin_angle  = resample(fin_angle, nsamples)

# subtract off the mean to de-bias for correlation
roll_accel_meaned = numpy.subtract(roll_accel, roll_accel.mean())
opal_accel_meaned = numpy.subtract(opal_accel, opal_accel.mean())

# correlate
z = correlate(roll_accel_meaned, opal_accel_meaned)
offset =  (len(z)/2) - numpy.argmax(z)

################################################################################
''' Output '''

# append data right amount
opal_time = opal_time[offset:]
opal_accel = opal_accel[offset:]
opal_rate = opal_rate[offset:]
angular_accel = angular_accel[offset:]
velocity = velocity[offset:]

length = min(len(opal_time), len(fin_angle))


output = [
    opal_time,
    angular_accel,
    velocity,
    altitude,
    fin_angle,
    opal_rate,
    opal_accel,
    roll_accel_meaned,
]

with open('model_data.csv', 'w') as f_out:
    for i in range(length):
        f_out.write(','.join('%f' % data[i] for data in output)+'\n')
