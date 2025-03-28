from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ros_tcp_endpoint",
                executable="default_server_endpoint",
                emulate_tty=True,
                parameters=[{"ROS_IP": "192.168.192.128"}, {"ROS_TCP_PORT": 10000}],
            )
        ]
    )
