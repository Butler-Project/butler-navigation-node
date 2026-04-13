import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    turtlebot3_gazebo_share = get_package_share_directory("turtlebot3_gazebo")
    nav2_bringup_share = get_package_share_directory("nav2_bringup")
    navigation_share = get_package_share_directory("high_level_reasoning_navigation")

    default_model = os.environ.get("TURTLEBOT3_MODEL", "burger")
    default_map = "/home/operador/slam/map_v4.yaml"
    default_params = os.path.join(
        navigation_share,
        "config",
        "burger_nav2.yaml",
    )

    model_arg = DeclareLaunchArgument(
        "turtlebot3_model",
        default_value=default_model,
        description="TurtleBot3 model to use in Gazebo and Nav2.",
    )
    map_arg = DeclareLaunchArgument(
        "map",
        default_value=default_map,
        description="Absolute path to the map yaml file.",
    )
    params_arg = DeclareLaunchArgument(
        "params_file",
        default_value=default_params,
        description="Absolute path to the Nav2 params file.",
    )
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="true",
        description="Use Gazebo simulation clock.",
    )
    x_pose_arg = DeclareLaunchArgument(
        "x_pose",
        default_value="-2.0",
        description="Initial robot X position in the house world.",
    )
    y_pose_arg = DeclareLaunchArgument(
        "y_pose",
        default_value="-3.5",
        description="Initial robot Y position in the house world.",
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo_share, "launch", "turtlebot3_house.launch.py")
        ),
        launch_arguments={
            "use_sim_time": LaunchConfiguration("use_sim_time"),
            "x_pose": LaunchConfiguration("x_pose"),
            "y_pose": LaunchConfiguration("y_pose"),
        }.items(),
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_share, "launch", "bringup_launch.py")
        ),
        launch_arguments={
            "map": LaunchConfiguration("map"),
            "use_sim_time": LaunchConfiguration("use_sim_time"),
            "params_file": LaunchConfiguration("params_file"),
            "autostart": "true",
            "slam": "False",
            "use_localization": "True",
        }.items(),
    )

    return LaunchDescription([
        model_arg,
        map_arg,
        params_arg,
        use_sim_time_arg,
        x_pose_arg,
        y_pose_arg,
        SetEnvironmentVariable("TURTLEBOT3_MODEL", LaunchConfiguration("turtlebot3_model")),
        gazebo_launch,
        nav2_launch,
    ])
