# 🎥 Video Demonstrations: SLAM Architecture Performance

The following videos showcase the real-time mapping process of the **BCR Bot** within a Gazebo warehouse simulation. These recordings highlight system performance across different sensor configurations, emphasizing both the vulnerabilities of single-sensor approaches and the robustness of the proposed **Multi-Modal Fusion architecture**.

*Because of limitations with video uploads on GitHub, the project videos are hosted on Google Drive. You can view them here:[link]()*

## 📹 `cam_with_lights_off.wmv` — Camera-Only SLAM Failure

**Overview:**  
Demonstrates the critical weakness of purely visual SLAM systems.

**Key Moment:**  
When the simulated environment lights are switched off, the RGB-D camera immediately loses access to visual features. This results in:

- Catastrophic tracking failure  
- Severe trajectory drift  
- Incomplete and unreliable map generation  

**video link**: click [here](artifacts/cam_with_lights_off.wmv)

## 📹 `lidar_with_lights_off.wmv` — LiDAR-Only Mapping & Perceptual Aliasing

**Overview:**  
Shows mapping based solely on geometric constraints using LiDAR.

**Key Moment:**  
Since LiDAR is unaffected by lighting conditions, the robot continues mapping successfully. However:

- A dense, chaotic network of yellow loop-closure links appears  
- This illustrates **perceptual aliasing**, where repetitive warehouse structures cause false-positive matches  
- The optimizer becomes overloaded with incorrect loop closures  

**video link**: click [here](artifacts/lidar_with_lights_off.wmv)

## 📹 `lidar_cam_with_lights_on.wmv` — Multi-Modal Fusion (Optimal Conditions)

**Overview:**  
Demonstrates the **Proxy Architecture** under ideal lighting conditions.

**Key Moment:**  
The system effectively balances both sensing modalities:

- **Visual odometry** provides smooth, high-frequency local tracking  
- **LiDAR scan matching** ensures accurate, sparse global loop closures  
- The trajectory (blue line) remains stable and precise  

**video link**: click [here](artifacts/lidar_cam_with_lights_on.wmv)

## 📹 `lidar_cam_with_lights_off.wmv` — Graceful Degradation (Blackout Test)

**Overview:**  
Validates the core hypothesis of the project: robust performance under sensor degradation.

**Key Moment:**  
When the lights are suddenly turned off mid-navigation:

- The system does **not fail**  
- The RTAB-Map optimizer automatically suppresses unreliable visual odometry  
- It seamlessly shifts reliance to **2D LiDAR (ICP fallback)**  
- The trajectory remains stable with **zero map fragmentation**  

**video link**: click [here](artifacts/lidar_cam_with_lights_off.wmv)

## ✅ Summary

These experiments clearly demonstrate:

- ❌ The fragility of single-sensor SLAM systems  
- ⚠️ The limitations of LiDAR-only approaches in structured environments  
- ✅ The robustness and adaptability of **Multi-Modal Sensor Fusion**, especially under real-world failure conditions  
