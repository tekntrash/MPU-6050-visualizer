# MPU-6050-visualizer
This repo is an introductory demo of the MPU-6050 Accelerometer &amp; Gyroscope Module using RVIZ and Matplotlib

The MPU6050 is a motion tracking device commonly used in robotic applications. It  detects changes in acceleration, rotation, and angular position. It's made up of a 3-axis accelerometer, a 3-axis gyroscope, a thermometer (in some models) and a Digital Motion Processor (DMP). This last module processes the data from the sensors and provides it in a simple format, which simplifies programming and reduces the computational load on the host proecssor. The MPU is often used attached to each of the moving parts of a robot such as legs, arms, torso, etc in order to provide data on the movement of those parts.

In this repo we offer 2 tools to visualize the data from the sensor: one using RVIZ which shows a robot in all angles, and another with Matploblib, which shows the raw data in a graph form. The RVIZ part of this repo was tested in ROS 2 Humble but it may work in other versions of ROS 2 too. The host used was a Nvidia Jetson Orin AGX 64 running Ubuntu 22.04.4 LTS Jammy, but it should run on similar Jetsons such as Xavier and Nano.

Install the MPU6050 to the Orin's 40 pin header: the picture https://github.com/tekntrash/MPU-6050-visualizer/blob/main/orin-pin-1.jpeg shows where pin 1 and the picture https://github.com/tekntrash/MPU-6050-visualizer/blob/main/expansion-header-pinout.png shows each one of the pins. Connect:

MPU 6050 GND -> Pin 6 (GND) Orin

MPU 6050 VCC -> Pin 1 (3.3V) Orin

MPU 6050 SDA -> Pin 3 (I2C5-DAT) Orin

MPU 6050 SCL -> Pin 5 (I2C5-CLK) Orin

Install the required libraries with the command pip install -r requirements.txt

Now, for the robot model, we used this free one: https://sketchfab.com/3d-models/biped-robot-801d2a245e4a4405a0c2152b35b5e486](https://sketchfab.com/3d-models/biped-robot-801d2a245e4a4405a0c2152b35b5e486 , but any will do as long as it is in .glb format. Download the model and save it in the same folder where you saved the repo: if you downloaded another you will have to edit the file accordingly

Put the MPU-6050 flat on a table, ensuring that the face with label is upward and a dot on this surface is on the top left corner. Then the upright direction upward is the z-axis of the chip. The direction from left to right is regarded as the X-axis. Accordingly the direction from back to front is defined as the Y-axis (see picture https://github.com/tekntrash/MPU-6050-visualizer/blob/main/MPU6050-axis.jpg)

Run the RVIZ visualization with the commands python RVIZ-visualizer.py in one screen: you will see the X,Y,Z,W data being shown up. In another screen run the command RVIZ2. At the lower left of the RVIZ screen click on "Add", " By topic", and "Marker". Wait a few seconds and you will see a robot showing up in the screen: you can use the mouse to reduce it
