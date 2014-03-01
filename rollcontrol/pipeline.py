#!/usr/bin/env python
import numpy
from scipy.integrate import simps
from scipy.signal import firwin, lfilter, resample, correlate

# original data. See: <https://github.com/psas/flight_data-2010.10.17>
opal_file = '../../../data/flight_data-2010.10.17/opal/Opal_launch_rotated.csv'
roll_file = '../../../data/flight_data-2010.10.17/roll/raw/output_trim.csv'

opal_sample_rate =  128     # Hz
roll_sample_rate = 1000     # Hz

# filter design
freq_cuttoff = 10  # Hz, low pass
window = firwin(numtaps=20, cutoff=freq_cuttoff, nyq=opal_sample_rate/2)



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
for i in range(len(opal_accel)):
    if i < len(opal_accel)-1:
        velocity.append(simps(opal_accel[:i+1], opal_time[:i+1]))
        altitude.append(simps(velocity[:-1], opal_time[:i+1]))
    if i > 0:
        angular_accel.append(opal_rate[i] - opal_rate[i-1])
velocity = numpy.array(velocity)
angular_accel = numpy.array(angular_accel)


# filter angular acceleation
angular_accel_filtered = lfilter(window, 1.0, angular_accel)



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


# find numnber of desired samples for file
nsamples = (len(roll_accel) * opal_sample_rate)/roll_sample_rate

# resample data to same timebase
roll_accel = resample(roll_accel, nsamples)
fin_angle  = resample(fin_angle, nsamples)

# divide by mean to normalaize for correlation
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
angular_accel_filtered = angular_accel_filtered[offset:]
velocity = velocity[offset:]

length = min(len(opal_time), len(fin_angle))


output = [
    opal_time,
    angular_accel,
    angular_accel_filtered,
    velocity,
    altitude,
    fin_angle,
    opal_accel,
    roll_accel_meaned,
]

with open('model_data.csv', 'w') as f_out:
    for i in range(length):
        f_out.write(','.join('%f' % data[i] for data in output)+'\n')
