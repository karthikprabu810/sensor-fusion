# Multi-Modal SLAM Proxy: Fusing 2D LiDAR and 3D Depth Camera for Robust Mapping

![ROS 2](https://img.shields.io/badge/ROS_2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-Classic_11-orange)
![License](https://img.shields.io/badge/License-Apache_2.0-green)

## 📌 Project Overview
Autonomous mobile robots operating in visually degraded environments (e.g., unlit warehouses) often face a critical single point of failure when relying solely on visual SLAM. Standard 2D LiDARs solve the lighting issue but lack the dense semantic context required for complex tasks.

This project implements a **"Proxy Architecture"** on a differential drive mobile robot. By fusing a sparse 2D LiDAR stream with a dense 3D Depth Camera stream within a Graph-SLAM framework, the system mimics high-end industrial sensor fusion. This architecture successfully prevents localization drift during simulated "sensor blackouts" (camera failures), ensuring robust, GPS-independent navigation.



## 🏗️ System Architecture

* **Robot Platform:** `bcr_bot` (Differential Drive)
* **Environment:** `small_warehouse.world` (Gazebo Classic)
* **Odometry Fusion:** `robot_localization` (EKF fusing wheel encoders + IMU)
* **Sensor Synchronization:** `rtabmap_sync` (`rgbd_sync` for timestamp alignment)
* **Graph-SLAM Backend:** `rtabmap_ros` (ICP scan matching + Visual Odometry)


## 🛠️ Installation & Build Instructions

Check the installation guide for more details provided [here](docs/installation_guide.md).

🚀 Running the Simulation

Use the Command guide provided [here](docs/command_guide.md).

## 🎥 Demo Videos

👉 [View Demo Videos](docs/demo.md)

👥 Authors

Karthik Prabu Natarajan - Frankfurt University of Applied Sciences (karthik.natarajan@stud.fra-uas.de)

Snehamol Sunny - Frankfurt University of Applied Sciences (snehamol.sunny@stud.fra-uas.de)

🙏 Acknowledgments

Base simulation platform provided by Black Coffee Robotics.