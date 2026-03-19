# 🧭 BCR Bot Simulation & SLAM Command Guide

This guide walks through launching the simulation, controlling the robot, running SLAM, visualizing results, and evaluating performance.

---

## 🚀 1. Start the Simulation (Gazebo)

```bash
ros2 launch bcr_bot gazebo.launch.py \
    camera_enabled:=True \
    two_d_lidar_enabled:=True \
    stereo_camera_enabled:=True \
    position_x:=0.0 \
    position_y:=0.0 \
    orientation_yaw:=0.0 \
    odometry_source:=world \
    world_file:=small_warehouse.sdf \
    robot_namespace:="bcr_bot"
```
## 🎮 2. Teleoperate the Robot

Open a new terminal to manually drive the robot and map the environment:
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/bcr_bot/cmd_vel
```
## 🧠 3. Launch SLAM and Sensor Fusion
```
ros2 launch bcr_bot rtabmap_sensor_fusion.launch.py
```
## 🔁 Alternative: Standard RTAB-Map Launch
```
ros2 launch rtabmap_launch rtabmap.launch.py \
    odom_topic:=/bcr_bot/odom \
    subscribe_scan:=true \
    scan_topic:=/bcr_bot/scan \
    rgb_topic:=/bcr_bot/kinect_camera/image_raw \
    depth_topic:=/bcr_bot/kinect_camera/depth/image_raw \
    camera_info_topic:=/bcr_bot/kinect_camera/camera_info \
    frame_id:=base_link \
    approx_sync:=true \
    use_sim_time:=true \
    rviz:=true
```

## 🖥️ 4. Visualization (RViz)

Visualize the TF tree, laser scans, and point clouds:
```
ros2 launch bcr_bot rviz.launch.py
```
## 📊 5. Quantitative Evaluation (evo Toolkit)

Evaluate the accuracy of recorded rosbag mapping runs.

### 📏 Absolute Trajectory Error (ATE)
```
evo_ape bag your_run.bag /ground_truth /rtabmap/localization_pose --plot
```
### 📐 Relative Pose Error (RPE)
```
evo_rpe bag your_run.bag /ground_truth /rtabmap/localization_pose --delta 1 --plot
```

## ✅ Notes

* Ensure all ROS 2 environments are properly sourced before running commands.

* Replace your_run.bag with your actual rosbag file.

* Use multiple terminals for parallel processes (simulation, teleop, SLAM, visualization).

## 📌 Requirements

* ROS 2 (Humble or later recommended)

* Gazebo

* RTAB-Map

* evo toolkit (pip install evo)