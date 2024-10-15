
# MPU-6050-visualizer

This repo is an introductory demo of the MPU-6050 Accelerometer & Gyroscope Module using RVIZ and Matplotlib.

The MPU6050 is a motion tracking device commonly used in robotic applications. It detects changes in acceleration, rotation, and angular position. It's made up of a 3-axis accelerometer, a 3-axis gyroscope, a thermometer (in some models), and a Digital Motion Processor (DMP). This module processes the data from the sensors and provides it in a simple format, which simplifies programming and reduces the computational load on the host processor. The MPU is often used attached to the moving parts of a robot (such as legs, arms, torso, etc.) to provide data on their movement.

In this repo, we offer two tools to visualize data from the sensor:
- **RVIZ**: Displays a robot model with real-time orientation data.
- **Matplotlib**: Displays raw data in a graphical form.

The RVIZ visualization was tested on **ROS 2 Humble**, but it may work on other ROS 2 versions as well. The hardware used was an **NVIDIA Jetson Orin AGX 64** running **Ubuntu 22.04.4 LTS Jammy**, though it should work on other Jetsons like Xavier and Nano.

## Setup Instructions

### Hardware Connections
Install the MPU6050 to the Orin's 40-pin header. Refer to the following images for pin connections:
- [Pin 1](https://github.com/tekntrash/MPU-6050-visualizer/blob/main/orin-pin-1.jpeg)
- [Expansion header pinout](https://github.com/tekntrash/MPU-6050-visualizer/blob/main/expansion-header-pinout.png)

Connect the pins as follows:
- **MPU 6050 GND** → **Pin 6 (GND)** Orin
- **MPU 6050 VCC** → **Pin 1 (3.3V)** Orin
- **MPU 6050 SDA** → **Pin 3 (I2C5-DAT)** Orin
- **MPU 6050 SCL** → **Pin 5 (I2C5-CLK)** Orin

### Software Installation
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Verify the connection:
   ```bash
   python quicktest.py
   ```
   If the message `"I2C 1 ok!"` is shown, the connection is working. If not, ensure the MPU6050 LED is lit and try switching the VCC and SDA cables (don't worry, this won’t damage the module).

3. Place the MPU-6050 flat on a table, ensuring that the side with the label is facing up and the dot is in the top-left corner. This orientation defines the axes:
   - **Z-axis**: Upward direction.
   - **X-axis**: Left to right.
   - **Y-axis**: Back to front.
   Refer to the [axis diagram](https://github.com/tekntrash/MPU-6050-visualizer/blob/main/MPU6050-axis.jpg).

## Running the Visualizers

### Matplotlib Visualizer
Run the Matplotlib visualizer with:
```bash
python matplotlib-data-visualizer.py
```
You should see a graph similar to `matplotlib-data.jpg`.

### RVIZ Visualizer
1. Download a 3D robot model in `.glb` format. We used a [free model](https://sketchfab.com/3d-models/biped-robot-801d2a245e4a4405a0c2152b35b5e486), but any `.glb` model will work. Save it in the same folder as this repo. If you use a different model, you will need to update the file paths in the code.

2. Install RVIZ for ROS 2 Humble:
   ```bash
   sudo apt update && sudo apt install curl gnupg lsb-release
   sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo tee /etc/apt/trusted.gpg.d/ros.asc
   sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
   sudo apt update
   sudo apt install ros-humble-rviz2
   source /opt/ros/humble/setup.bash
   ```

3. Run the RVIZ visualizer:
   ```bash
   python RVIZ-visualizer.py
   ```
   In another terminal window, run:
   ```bash
   rviz2
   ```
   In RVIZ, click **"Add"**, then **"By topic"**, and select **"Marker"**. After a few seconds, you should see the robot model appear. You can scale it using the mouse. A sample view is shown in `RVIZ-visualization.mp4`.

## To Do
1. Update the RVIZ visualizer to initialize the robot in an upright position.
