import time
import board
import adafruit_mpu6050
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Initialize I2C and MPU6050
i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)

# Setup the plot
plt.ion()  # Turn on interactive mode
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(hspace=0.4)

# Data storage
acc_x, acc_y, acc_z = deque(maxlen=50), deque(maxlen=50), deque(maxlen=50)
gyro_x, gyro_y, gyro_z = deque(maxlen=50), deque(maxlen=50), deque(maxlen=50)
temp = deque(maxlen=50)

# Plotting loop
while True:
    # Read sensor data
    acceleration = mpu.acceleration
    gyro = mpu.gyro
    temperature = mpu.temperature

    # Update data queues
    acc_x.append(acceleration[0])
    acc_y.append(acceleration[1])
    acc_z.append(acceleration[2])
    gyro_x.append(gyro[0])
    gyro_y.append(gyro[1])
    gyro_z.append(gyro[2])
    temp.append(temperature)

    # Clear the axes for new data
    axs[0].cla()
    axs[1].cla()
    axs[2].cla()

    # Plot acceleration data
    axs[0].plot(acc_x, label='X Acceleration (m/s²)')
    axs[0].plot(acc_y, label='Y Acceleration (m/s²)')
    axs[0].plot(acc_z, label='Z Acceleration (m/s²)')
    axs[0].set_title('Acceleration Data')
    axs[0].set_ylabel('Acceleration (m/s²)')
    axs[0].legend()
    
    # Plot gyro data
    axs[1].plot(gyro_x, label='X Gyro (degrees/s)')
    axs[1].plot(gyro_y, label='Y Gyro (degrees/s)')
    axs[1].plot(gyro_z, label='Z Gyro (degrees/s)')
    axs[1].set_title('Gyro Data')
    axs[1].set_ylabel('Gyro (degrees/s)')
    axs[1].legend()
    
    # Plot temperature data
    axs[2].plot(temp, label='Temperature (°C)', color='orange')
    axs[2].set_title('Temperature Data')
    axs[2].set_ylabel('Temperature (°C)')
    axs[2].legend()

    # Refresh the plot
    plt.draw()
    plt.pause(0.1)  # pause to allow the plot to update

    time.sleep(0.1)  # delay before the next reading
