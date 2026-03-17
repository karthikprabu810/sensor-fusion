# Multi-Modal SLAM Proxy: Fusing 2D LiDAR and Depth Camera for Robust Mapping

![ROS 2](https://img.shields.io/badge/ROS_2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Classic_11-orange)
![License](https://img.shields.io/badge/License-Apache_2.0-green)

## 📌 Project Overview
Autonomous mobile robots operating in visually degraded environments (e.g., unlit warehouses) often face a critical single point of failure when relying solely on visual SLAM. Standard 2D LiDARs solve the lighting issue but lack the dense semantic context required for complex tasks.

This project implements a **"Proxy Architecture"** on a differential drive mobile robot. By fusing a sparse 2D LiDAR stream with a dense 3D Depth Camera stream within a Graph-SLAM framework (`rtabmap_ros`), the system mimics high-end industrial sensor fusion. This architecture successfully prevents localization drift during simulated "sensor blackouts" (camera failures), ensuring robust, GPS-independent navigation.

---

## 🏗️ System Architecture

* **Robot Platform:** `bcr_bot` (Differential Drive)
* **Environment:** `small_warehouse.world` (Gazebo Classic)
* **Odometry Fusion:** `robot_localization` (EKF fusing wheel encoders + IMU)
* **Sensor Synchronization:** `rtabmap_sync` (`rgbd_sync` for timestamp alignment)
* **Graph-SLAM Backend:** `rtabmap_ros` (ICP scan matching + Visual Odometry)

---

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