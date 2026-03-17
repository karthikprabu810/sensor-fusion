from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time = True

    rtabmap_node = Node(
        package='rtabmap_slam',
        executable='rtabmap',
        name='rtabmap',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'frame_id': 'base_link',
            'odom_frame_id': 'odom',
            'subscribe_scan': True,
            'subscribe_rgb': False,
            'subscribe_depth': False,
            'subscribe_stereo': False,
            'subscribe_rgbd': False,
            'approx_sync': False,
            'queue_size': 10,

            # Useful LiDAR/SLAM parameters
            'Reg/Strategy': '1',          # ICP registration
            'Grid/FromDepth': 'False',
            'Grid/RangeMax': '8.0',
            'Grid/3D': 'False',
            'Icp/MaxCorrespondenceDistance': '1.0',
            'Icp/VoxelSize': '0.05',
            'Icp/PointToPlane': 'False',
            'RGBD/ProximityBySpace': 'True',
            'RGBD/AngularUpdate': '0.05',
            'RGBD/LinearUpdate': '0.05',
            'Mem/IncrementalMemory': 'True',
            'Mem/InitWMWithAllNodes': 'False',
        }],
        remappings=[
            ('scan', '/bcr_bot/scan'),
            ('odom', '/bcr_bot/odom')
        ],
        arguments=['-d']
    )

    rtabmap_viz_node = Node(
        package='rtabmap_viz',
        executable='rtabmap_viz',
        name='rtabmap_viz',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'frame_id': 'base_link',
            'subscribe_scan': True,
            'subscribe_rgb': False,
            'subscribe_depth': False,
            'subscribe_stereo': False,
            'subscribe_rgbd': False,
            'approx_sync': False,
        }],
        remappings=[
            ('scan', '/bcr_bot/scan'),
            ('odom', '/bcr_bot/odom')
        ]
    )

    return LaunchDescription([
        rtabmap_node,
        rtabmap_viz_node
    ])