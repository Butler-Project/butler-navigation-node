# High Level Reasoning Navigation

This package launches the TurtleBot3 Gazebo house simulation together with Nav2 localization and navigation using the map:

- `resources/slam/map_v4.yaml`

## Build

```bash
source /opt/ros/jazzy/setup.bash &&
cd /home/operador/Documents/kamerdyner-dev/ros_workspace &&
colcon build --packages-select high_level_reasoning_navigation &&
source install/setup.bash
```

## Run

```bash
source /opt/ros/jazzy/setup.bash &&
cd /home/operador/Documents/kamerdyner-dev/ros_workspace &&
source install/setup.bash &&
ros2 launch high_level_reasoning_navigation navigation.launch.py
```

## Optional arguments

```bash
ros2 launch high_level_reasoning_navigation navigation.launch.py \
  turtlebot3_model:=burger \
  map:=/home/operador/slam/map_v4.yaml \
  params_file:=/opt/ros/jazzy/share/turtlebot3_navigation2/param/burger.yaml
```

## Notes

- The default model is `burger`.
- The launch file starts the TurtleBot3 house world from `turtlebot3_gazebo`.
- It also starts Nav2 bringup with localization enabled and `slam:=False`.
- The default Nav2 config enables `amcl.set_initial_pose=true` with the spawn pose `(-2.0, -0.5, 0.0)`.
