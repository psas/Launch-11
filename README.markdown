# PSAS Launch-11

![Mission Patch](http://psas.github.io/Launch-11/patch/L11_patch.svg)


## Objectives:
 - Fly
 - Dont Crash
 - Safety Third
 - Recover Telemetry
   - Create data
     - Sensors
     - Events
     - Commands
   - Record on Telemetry Endpoint
   - Live feed to ground
   - Record on ground
   - Ground display
   - Record on data creating device
 - Roll control
   - Algorithm 
   - Sensor Data
   - Actuator
 - Raw GPS
   - Record locally
 - Video
   - Up and Down
   - Record Locally
   - Live feed of Down to ground
   - Record on ground
   - Ground Display
 - Ground Support
   - Launch Tower Computer
   - Ignition Control

Data about PSAS's 12th official flight.

Info about Arm State [arm-state.markdown](arm-state.markdown)

Programmable parts [programmable.markdown](programmable.markdown)


For a full program launch history see [psas.pdx.edu](http://psas.pdx.edu/).

![Rocket Overview](http://psas.github.io/Launch-11/rocket_overview.svg)


## Jargon and Projects:

 - **Elderberry**: A python package with a event model `c` code generator to compile the Flight Computer. Also called the FCF
 - **FC**: The **F**light **C**omputer
 - [**RNH**](https://github.com/psas/Launch-11/tree/gh-pages/RNH): **R**ocket **N**et **H**ub, the power and data distribution for the rocket
 - **FCF**: **F**light **C**omputer **F**ramework. _see: Elderberry_
 - **Telemetry Viewer**: A python backend for a web based viewer for arbitrary data
