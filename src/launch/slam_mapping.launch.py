import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    turtlebot3_gazebo_share = get_package_share_directory("turtlebot3_gazebo")

    default_model = os.environ.get("TURTLEBOT3_MODEL", "burger")

    # --- Argumentos ---
    model_arg = DeclareLaunchArgument(
        "turtlebot3_model",
        default_value=default_model,
    )
    x_pose_arg = DeclareLaunchArgument("x_pose", default_value="-2.0")
    y_pose_arg = DeclareLaunchArgument("y_pose", default_value="-0.5")

    # --- Gazebo con la casa ---
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo_share, "launch", "turtlebot3_house.launch.py")
        ),
        launch_arguments={
            "use_sim_time": "true",
            "x_pose": LaunchConfiguration("x_pose"),
            "y_pose": LaunchConfiguration("y_pose"),
        }.items(),
    )

    return LaunchDescription([
        model_arg,
        x_pose_arg,
        y_pose_arg,
        SetEnvironmentVariable("TURTLEBOT3_MODEL", LaunchConfiguration("turtlebot3_model")),
        gazebo_launch,
    ])
