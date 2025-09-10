
import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    slam_params_file = LaunchConfiguration('slam_params_file')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation/Gazebo clock')
    declare_slam_params_file_cmd = DeclareLaunchArgument(
        'slam_params_file',
        default_value=os.path.join(get_package_share_directory("f112th_sim_2502_yankee"),
                                   'config', 'mapper_params_localization.yaml'),
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')

    # start_localization_slam_toolbox_node = Node(
    #     parameters=[
    #       slam_params_file,
    #       {'use_sim_time': use_sim_time}
    #     ],
    #     package='slam_toolbox',
    #     executable='localization_slam_toolbox_node',
    #     name='slam_toolbox',
    #     output='screen')
    start_localization_slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='localization_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[{
        'use_sim_time': use_sim_time,
        'mode': 'localization',
        'map_file_name': '/home/clip2004/ros2_ws_2502/src/f112th_sim_2502_yankee/map/race_track_serialize',
        'map_start_pose': [-5.5, 3.5, -1.57],
        # 'map_file_name': '/home/clip2004/ros2_ws_2502/src/f112th_sim_2502_yankee/map/my_map_serialize',
        # 'map_start_pose': [0.0, 0.0, 0.0],
        'map_frame': 'map',
        'odom_frame': 'odom',
        'base_frame': 'base_link',
        'scan_topic': '/scan',
        'publish_map': True
    }])
    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_slam_params_file_cmd)
    ld.add_action(start_localization_slam_toolbox_node)

    return ld
