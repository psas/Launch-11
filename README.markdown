# PSAS Launch-11

![Mission Patch](http://psas.github.io/Launch-11/patch/L11_patch.svg)


## Objectives:

 1. **Launch** our LV2.3 airframe summer 2014
 1. **Successful flight** to at lest 75% of projected altitude; recover all hardware intact.
 1. **Telemetry**
   - get data from:
      - Inertial sensors
      - Events (e.g., 'launch')
      - Commands
   - Record telemetry on rocket
   - Live stream to ground
   - Record on ground
   - Real time display on ground 
   - Record on data creating device
 1. **Ground Support**
   - Remote, safe, digital ignition control
   - Effective recovery
      - Coordination between recovery teams and mission control
      - Know rocket location immediatly after landing
      - Easy transportation back to flight line
 1. **Experiments**
   - Roll control
      - Documented algorithm and analysis
      - Include control data in telemetry
   - Record raw GPS RF environment to SD card
   - Digital Video
      - Downward facing camera
      - Record locally
      - Live digital feed of camera to ground in integrated telemetry stream
      - Record on ground
      - Secondary upward facing camera
      - Real time ground display


Info about Arm State [arm-state.markdown](arm-state.markdown) and 
Programmable parts [programmable.markdown](programmable.markdown).


For a full program launch history see [psas.pdx.edu](http://psas.pdx.edu/).

![Rocket Overview](http://psas.github.io/Launch-11/rocket_overview.svg)


## Jargon and Projects:

 - **Elderberry**: A python package with a event model `c` code generator to compile the Flight Computer. Also called the FCF
 - **FC**: The **F**light **C**omputer
 - [**RNH**](https://github.com/psas/Launch-11/tree/gh-pages/RNH): **R**ocket **N**et **H**ub, the power and data distribution for the rocket
 - **FCF**: **F**light **C**omputer **F**ramework. _see: Elderberry_
 - **Telemetry Viewer**: A python backend for a web based viewer for arbitrary data
