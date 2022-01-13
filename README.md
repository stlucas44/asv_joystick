# Repeating joystick for roboat controls
## Setup:
```
git clone https://github.com/ros-drivers/joystick_drivers.git
catkin build joy asv_joystick
source ~/catkin_ws/setup.bash
```

## Multiple joysticks:
This has to be specified in the launch of joy. In `/dev/input/` there will be `js0`, `js1` and so on. See asv_joystick launch file.
