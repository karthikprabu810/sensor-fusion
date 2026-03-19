# ⚙️ ROS 2 Workspace Setup Guide

This guide explains how to create a ROS 2 workspace, clone the repository, install dependencies, and build the project.
## ⚙️ Dependencies & Prerequisites

This package is built for **Ubuntu 22.04** and **ROS 2 Humble**. 

Ensure you have the following installed:
* ROS 2 Humble
* Gazebo Classic 11
* `gazebo_ros_pkgs`

Install the required ROS 2 packages via `apt`:
```bash
sudo apt update
sudo apt install ros-humble-rtabmap-ros ros-humble-robot-localization ros-humble-navigation2 ros-humble-nav2-bringup
```

## 📁 1. Create a ROS 2 Workspace

```bash
mkdir -p ~/my_ws/src
cd ~/my_ws/src
```
## 📥 2. Clone the Repository
```
git clone https://github.com/karthikprabu810/sensor-fusion.git
```
## 📦 3. Install Dependencies
```
cd ~/my_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```
## 🛠️ 4. Build the Workspace
```
colcon build --symlink-install
source install/setup.bash
```
### ✅ Notes

* Make sure ROS 2 is properly installed and sourced before starting.
* Run source install/setup.bash in every new terminal before using the workspace.
* If dependencies fail, try running rosdep update again.

### 📌 Requirements

* ROS 2 Humble
* colcon build tools
* rosdep
* Git