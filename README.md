<div align="center">

# 🏎️ F1/12th Simulator

### A ROS 2 simulation environment for differential drive robots

[![ROS 2 Humble](https://img.shields.io/badge/ROS_2-Humble-blue?logo=ros&logoColor=white)](https://docs.ros.org/en/humble/)
[![Gazebo Classic](https://img.shields.io/badge/Gazebo-Classic-orange?logo=gazebo&logoColor=white)](https://classic.gazebosim.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![ament_cmake](https://img.shields.io/badge/build-ament__cmake-blueviolet)](https://docs.ros.org/en/humble/How-To-Guides/Ament-CMake-Documentation.html)

</div>

---

## 📌 Overview

`f112th_sim_2502_yankee` is a ROS 2 package that provides everything needed to simulate a **differential drive robot** (F1/12-scale style) in **Gazebo Classic**. It includes robot description files, launch configurations, world scenarios, and parameter files — giving you a reproducible sandbox for developing and testing:

- 🎮 Joystick teleoperation
- 🧭 Navigation and path following algorithms
- 🗺️ SLAM and localization pipelines
- 🔁 Custom controllers

---

## 📁 Package Structure

```
f112th_sim_2502_yankee/
├── config/          # YAML parameter files (joy, twist_mux, mapper, etc.)
├── description/     # Xacro/URDF robot and model definitions
├── docs/            # Project documentation and historical notes
├── launch/          # ROS 2 launch files
├── map/             # Maps and posegraph files for SLAM/localization tests
└── worlds/          # Gazebo world files (multiple test scenarios)
```

---

## ⚙️ Requirements

| Dependency | Version / Notes |
|---|---|
| **ROS 2** | Humble (recommended) — later distros should work, verify compatibility |
| **Gazebo** | Classic (`gazebo_ros`) — match version to your ROS 2 distro |
| `ros-<distro>-gazebo-ros` | Gazebo–ROS bridge |
| `ros-<distro>-joy` | Joystick input node |
| `ros-<distro>-teleop-twist-joy` | Joystick teleoperation |
| `ros-<distro>-twist-mux` | Velocity multiplexer |

> ⚠️ If you see API incompatibility warnings at runtime, double-check that your `gazebo_ros` version matches your ROS 2 distribution.

---

## 🚀 Quick Start

### 1. Clone into your workspace

```bash
cd ~/ros2_ws/src
git clone https://github.com/Clip2004/f112th_sim_2502_yankee.git
```

### 2. Build

```bash
cd ~/ros2_ws
colcon build --packages-select f112th_sim_2502_yankee
source install/setup.bash
```

### 3. Launch the simulation

```bash
ros2 launch f112th_sim_2502_yankee launch_sim.launch.py
```

> 💡 **Renaming the package?** The launch files use the internal variable `package_name = "f112th_sim_2502_yankee"`. If you rename the package or repository, update that string across the launch files **and** in `package.xml`.

---

## 🛠️ Launch Files

### `launch_sim.launch.py` — Full simulation stack

Brings up the complete simulation environment:

1. **`rsp.launch.py`** — Starts `robot_state_publisher` with the robot URDF/Xacro description.
2. **`gazebo.launch.py`** (from `gazebo_ros`) — Launches the Gazebo simulator.
3. **`spawn_entity.py`** — Spawns the robot into the Gazebo world using `robot_description`.
4. **`joystick.launch.py`** — Starts joystick teleoperation (see below).
5. **`twist_mux`** — Velocity multiplexer to arbitrate command sources.

### `joystick.launch.py` — Teleoperation

Starts `joy_node` and `teleop_node` for joystick-based robot control.

---

## 🔧 Configuration & Customization

### Change the robot's spawn position

In `launch_sim.launch.py`, find the `spawn_entity` call and edit the position arguments:

```python
'-x', '0.0', '-y', '0.0', '-z', '0.05', '-Y', '0.0'
```

### Simulated clock

All launch files pass `use_sim_time=true` to nodes that support it — no extra configuration needed.

### Custom parameters

Edit or add YAML files in `config/` to tune node behavior (joystick axes, velocity limits, mapper settings, etc.):

```
config/
├── joy_params.yaml
├── twist_mux.yaml
└── ...
```

---

## 🗺️ Available Worlds

The `worlds/` directory contains multiple Gazebo scenarios of varying complexity. Open any `.world` file in Gazebo or specify it as an argument in your launch file:

```bash
ros2 launch f112th_sim_2502_yankee launch_sim.launch.py world:=worlds/my_world.world
```

---

## ✅ Best Practices

- **Back up before restructuring** — create an `archive/` folder before deleting or moving files.
- **Performance** — Gazebo with complex worlds is resource-intensive. Close other heavy applications, or simplify the world model if performance is poor.
- **Distro compatibility** — Always verify `gazebo_ros` compatibility when upgrading your ROS 2 distribution.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ for the ROS 2 community
</div>
