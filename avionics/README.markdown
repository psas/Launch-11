# L-11 Avionics (AV4)

This flight features a very sophisicated multi-part avionics stack.

**AV4** is roughly the 5th iteration of our rocket avionics.

![FC Stack](http://psas.github.io/Launch-11/avionics/photos/FC-stack.jpg)


# AV4 Overview

![AV4 Overview](http://psas.github.io/Launch-11/avionics/AV4_overview.svg)

# Hardware Mapping

 1. **Launch** our LV2.3 airframe summer 2014
 1. **Successful flight** to at least 75% of projected altitude; recover all hardware intact.
    - _RNH_
 1. **Telemetry**
   - get data from:
      - Inertial sensors
         - _IMU node_
      - Health Data
         - _RNH_
         - _FC_
         - _Gas Gauge_
      - Non Periodic Events (e.g., 'launch')
         - _All MPA_
      - Error Events
         - _All MPA_
      - Commands
         - _Ground umbilical_
   - Record telemetry on rocket
      - _FC HDD_
   - Live stream to ground
      - _WiFi and PA_
   - Record on ground
      - _Telemetry Server_
   - Real time display on ground
      - _Telemetry Server_
   - Record on data creating device
      - _local SD cards_
 1. **Ground Support**
   - Remote, safe, digital ignition control
      - _LTC_
   - Effective recovery
      - Coordination between recovery teams and mission control
         - _HAM Radio and Telemetry server_
      - Know rocket location immediately after landing
         - _Telemetry server_
      - Easy transportation back to flight line
         - _Carrier_
 1. **Experiments**
   - Roll control
      - _Roll Board_
      - Documented algorithm and analysis
      - Include control data in telemetry
         - _Roll Board_
   - Record raw GPS RF environment to SD card
      - _GPS Board_
      - Record COTS GPS fixes
         - _GPS Carrier_
   - Digital Video
      - _Camera Pi_
      - _Downward facing camera_
      - Record locally
         - _Camera Pi_
      - Live digital feed of camera to ground in integrated telemetry stream
         - _Camera Pi_
      - Record on ground
         - _?_
      - Secondary upward facing camera
         - _Camera Pi 2_
      - Real time ground display
         - _Telemetry Server_

AV4 stackup:

 - **Main Flight Computer**
   - Intel Atom N455 PCI-104, 1.6 GHz
 - **Rocket Net Hub**
   - STM32 + KSZ8999
 - **IMU**
   - ADIS16405 (9DOF IMU)
   - MPU9150 (6DOF IMU)
   - MPL3115A2 (Baro)
 - **Roll Control**
   - JR Servo DS8717
 - **GPS**
   - GPS RF Front end recorder
   - Hemisphere Crescent OEM
 - **Battery**
   - 4 cell LiPo
   - BQ3060 SBS management chip
 - **Cameras**
   - Raspberry Pi Model B
   - Omnivision 5647 sensor


Info about Arm State [arm-state.markdown](arm-state.markdown) and
Programmable parts [programmable.markdown](programmable.markdown).


# Rocket Net Hub

The **R**ocket **N**et **H**ub is the central power and data distribution node
for the rocket. It contains an 8 port Ethernet switch and an STM32
microcontroller.

![RNH Overview](http://psas.github.io/Launch-11/avionics/RNH_overview.svg)


# Network

The ground and rocket has a significant network infrastructure:

![Network Diagram](http://psas.github.io/Launch-11/avionics/network_diagram.svg)


# Radio Spectrum Allocation 

![Radio Spectrum](http://psas.github.io/Launch-11/avionics/spectrum.svg)

