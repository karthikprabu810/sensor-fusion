from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    use_sim_time = True

    return LaunchDescription([

        # -------------------------------
        # RTABMAP SYNC (RGB + Depth + IMU)
        # -------------------------------
        Node(
            package='rtabmap_sync',
            executable='rgbd_sync',
            name='rgbd_sync',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'approx_sync': True,
                'approx_sync_max_interval': 0.01  
            }],
            remappings=[
                ('rgb/image',       '/bcr_bot/kinect_camera/image_raw'),
                ('depth/image',     '/bcr_bot/kinect_camera/depth/image_raw'),
                ('rgb/camera_info', '/bcr_bot/kinect_camera/camera_info'),
                ('imu',             '/bcr_bot/imu')
            ]
        ),

        # -------------------------------
        # RTABMAP CORE (SLAM)
        # -------------------------------
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,

                # Frames
                'frame_id': 'base_link',
                'odom_frame_id': 'odom',
		'map_frame_id': 'map',

                # Sensor usage
                'subscribe_rgbd': True,
                'subscribe_scan': True,
                'subscribe_imu': True,

                # RTAB-Map settings
                # 'sync_queue_size': 30,
                # 'publish_tf': True,
                # 'map_always_update': True,

                # Sensor fusion
                # 'Reg/Strategy': 1,        # ICP + visual
                # 'Reg/Force3DoF': True,    # Ground robot
                #'RGBD/ProximityBySpace': True,

                # ICP (LiDAR)
                # 'Icp/PointToPlane': True,
                # 'Icp/VoxelSize': 0.05,
                # 'Icp/MaxCorrespondenceDistance': 1.0,
            }],
            remappings=[
                ('rgbd_image', '/rgbd_image'),
                ('scan', '/bcr_bot/scan'),
                ('odom', '/bcr_bot/odom')
            ]
        ),

        # -------------------------------
        # RTABMAP VISUALIZATION
        # -------------------------------
        Node(
            package='rtabmap_viz',
            executable='rtabmap_viz',
            name='rtabmap_viz',
            output='screen',
            parameters=[{
                'use_sim_time': use_sim_time,
                'frame_id': 'base_link'
            }],
            remappings=[
                ('rgbd_image', '/rgbd_image'),
                ('scan', '/bcr_bot/scan'),
                ('odom', '/bcr_bot/odom')
            ]
        )
    ])
