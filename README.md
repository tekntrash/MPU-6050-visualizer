# MPU-6050-visualizer
This repo is an introductory demo of the MPU-6050 Accelerometer &amp; Gyroscope Module using RVIZ and Matplotlib

The MPU6050 is a motion tracking device commonly used in robotic applications. It  detects changes in acceleration, rotation, and angular position. It's made up of a 3-axis accelerometer, a 3-axis gyroscope, a thermometer (in some models) and a Digital Motion Processor (DMP). This last module processes the data from the sensors and provides it in a simple format, which simplifies programming and reduces the computational load on the host proecssor. The MPU is often used attached to each of the moving parts of a robot such as legs, arms, torso, etc in order to provide data on the movement of those parts.

In this repo we offer 2 tools to visualize the data from the sensor: one using RVIZ which shows a robot in all angles, and another with Matploblib, which shows the raw data in a graph form. The RVIZ part of this repo was tested in ROS 2 Humble but it may work in other versions of ROS 2 too. The host used was a Nvidia Jetson Orin AGX 64 running Ubuntu 22.04.4 LTS Jammy, but it should run on similar Jetsons such as Xavier and Nano.

Install the required libraries with the command pip install -r requirements.txt
