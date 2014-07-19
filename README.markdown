# PSAS Launch-11

![Mission Patch](http://psas.github.io/Launch-11/patch/L11_patch.svg)

**L-11** is the 12th launch in Portland State Aerospace Society history. For a
full program launch history see [psas.pdx.edu](http://psas.pdx.edu/).

## Scheduled Launch: July 20th, 2014!

We hope to launch in Central Oregon July 20th. This will mostly be a checkout
and data gathering flight for our upgraded avionics stack and still-in-development
rocket software stack.

# L-11 Objectives

 1. **Launch** our LV2.3 airframe summer 2014
 1. **Successful flight** to at least 75% of projected altitude; recover all hardware intact.
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
      - Know rocket location immediately after landing
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


--------------------------------------------------------------------------------

## Major Projects:

 - Primary Flight Computer Softawre: [psas/av3fc](https://github.com/psas/av3-fc)
 - Microcontroller firmware: [psas/stm32](https://github.com/psas/stm32)
 - Electronics CAD files: [psas/avionics-cad](https://github.com/psas/avionics-cad)
 - Data format spec: [psas/psas_packet](https://github.com/psas/psas_packet)
 - Telemetry viewer: [psas/telemetry](https://github.com/psas/telemetry)


## Rocket Overview

![Rocket Overview](http://psas.github.io/Launch-11/rocket_overview.svg)


## Jargon and Projects:

 - **Elderberry**: A python package with a event model C code generator to compile the Flight Computer. Also called the FCF
 - **FC**: The <b>F</b>light <b>C</b>omputer
 - **RNH**: <b>R</b>ocket <b>N</b>et <b>H</b>ub, the power and data distribution for the rocket
 - **FCF**: <b>F</b>light <b>C</b>omputer <b>F</b>ramework. _see: Elderberry_
 - **Telemetry Viewer**: A python backend for a web based viewer for arbitrary data
