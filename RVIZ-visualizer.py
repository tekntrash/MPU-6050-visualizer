import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from transforms3d.euler import euler2quat
import time
import board
import adafruit_mpu6050

# Initialize the MPU6050 sensor
i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

# Track accumulated rotation for the robot
roll, pitch, yaw = 0.0, 0.0, 0.0
previous_time = time.time()

class RobotMarkerPublisher(Node):
    def __init__(self):
        super().__init__('robot_marker_publisher')
        self.broadcaster = TransformBroadcaster(self)
        self.publisher = self.create_publisher(Marker, '/visualization_marker', 10)
        self.timer = self.create_timer(0.1, self.publish_markers)
        self.robot_marker = self.create_marker("robot", 0, 0.0, 0.0, 0.0)

    def create_marker(self, ns, marker_id, x, y, z):
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = ns
        marker.id = marker_id
        marker.type = Marker.MESH_RESOURCE
        marker.action = Marker.ADD
        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = z
        marker.pose.orientation.w = 1.0  # Initial orientation
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 1.0
        marker.color.a = 1.0
        marker.mesh_resource = "file:///root/biped_robot.glb"  # Use absolute path
        return marker

    def publish_markers(self):
        global roll, pitch, yaw, previous_time

        # Get current sensor data
        gyro = mpu.gyro
        current_time = time.time()
        delta_time = current_time - previous_time
        previous_time = current_time

        # Accumulate gyroscope data to update roll, pitch, and yaw (angular velocities in rad/s)
        roll += gyro[0] * delta_time
        pitch += gyro[1] * delta_time
        yaw += gyro[2] * delta_time

        # Convert accumulated roll, pitch, yaw to quaternion
        qx, qy, qz, qw = euler2quat(roll, pitch, yaw, axes='sxyz')

        # Update robot marker's orientation based on gyro data
        self.robot_marker.pose.orientation.x = qx
        self.robot_marker.pose.orientation.y = qy
        self.robot_marker.pose.orientation.z = qz
        self.robot_marker.pose.orientation.w = qw
        
        print ("X=",qx," Y=",qy," Z=",qz," W=",qw)

        # Update timestamp for the marker
        self.robot_marker.header.stamp = self.get_clock().now().to_msg()

        # Publish the robot marker
        self.publisher.publish(self.robot_marker)

        # Create and publish transform for the robot
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "map"  # Parent frame
        t.child_frame_id = 'robot_frame'  # Child frame for the robot marker
        t.transform.translation.x = self.robot_marker.pose.position.x
        t.transform.translation.y = self.robot_marker.pose.position.y
        t.transform.translation.z = self.robot_marker.pose.position.z
        t.transform.rotation.x = qx
        t.transform.rotation.y = qy
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        # Broadcast the transform
        self.broadcaster.sendTransform(t)


def main(args=None):
    rclpy.init(args=args)
    robot_marker_publisher = RobotMarkerPublisher()
    print("Robot is running...")
    rclpy.spin(robot_marker_publisher)
    robot_marker_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
