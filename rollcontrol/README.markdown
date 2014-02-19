# Roll Control Theory

The first thing we need to do is create a model and validate it on past
launches.

`create_model_data.py` was written to take data from the succesful
[2010 roll control launch](https://github.com/psas/flight_data-2010.10.17)
and find the rocket's airspeed and angular acceleration for the duration of the
flight. These are imputs to the model.


### `model_data.csv` format:

Columns:

 1. time [s]
 1. velocity [m/s]
 1. angular acceleration [degrees/s/s]
 1. angular acceleration (filtered) [degrees/s/s]
 1. linear acceleration [m/s/s]
 1. roll rate (degrees/s)
