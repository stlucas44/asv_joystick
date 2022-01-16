# Repeating joystick for roboat controls
## Setup:
```
git clone https://github.com/stlucas44/asv_joystick.git
git submodule init
git submodule update
catkin build joy asv_joystick
source ~/catkin_ws/setup.bash
```

## Example:
Example launch with joystick for agent on the left.
```
roslaunch mppi_evaluation tight_crossing_multi_agent_joystick.launch
```

## Launch params:
Currently the launcher checks for max 2 joysticks. When parameter
`ctrl_type = joystick`, the launcher checks if joystick params (`js_0` etc.)
exists and launches the receivers and mppis accordingly.
