#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.duration import Duration


class LoopClosurePathNode(Node):
    """
    Simple open-loop motion node that drives the robot
    in a rectangular path to help trigger loop closures.

    Path (approximate):
      1) Forward L1
      2) Right 90°
      3) Forward L2
      4) Right 90°
      5) Forward L1
      6) Right 90°
      7) Forward L2
      8) Right 90° (back to original heading)
      9) Stop
    """

    def __init__(self):
        super().__init__("loop_closure_path")

        # >>> CHANGE THIS if your cmd_vel topic is different <<<
        cmd_vel_topic = "/bcr_bot/cmd_vel"   # or "/cmd_vel"
        self.pub = self.create_publisher(Twist, cmd_vel_topic, 10)

        # Parameters: tune these for your robot
        linear_speed = 0.3      # m/s
        angular_speed = -0.5    # rad/s (negative = right turn)
        L1 = 3.0                # first edge length (m)
        L2 = 2.0                # second edge length (m)

        # Durations (distance = v * t  =>  t = d / v)
        t_fwd_L1 = L1 / linear_speed
        t_fwd_L2 = L2 / linear_speed
        t_turn_90 = 1.57 / abs(angular_speed)   # ~pi/2 radians

        # Define sequence of (vx, wz, duration_sec)
        self.sequence = [
            (linear_speed, 0.0,        t_fwd_L1),  # 1) forward L1
            (0.0,          angular_speed, t_turn_90),  # 2) right 90°
            (linear_speed, 0.0,        t_fwd_L2),  # 3) forward L2
            (0.0,          angular_speed, t_turn_90),  # 4) right 90°
            (linear_speed, 0.0,        t_fwd_L1),  # 5) forward L1
            (0.0,          angular_speed, t_turn_90),  # 6) right 90°
            (linear_speed, 0.0,        t_fwd_L2),  # 7) forward L2
            (0.0,          angular_speed, t_turn_90),  # 8) right 90°
            (0.0,          0.0,        0.0),       # 9) stop
        ]

        self.current_step = 0
        self.step_start_time = self.get_clock().now()

        # Timer to update cmd_vel at 20 Hz
        self.timer = self.create_timer(0.05, self.timer_callback)
        self.get_logger().info("Loop closure motion node started.")

    def timer_callback(self):
        # If we finished all steps: keep publishing zero, then shutdown
        if self.current_step >= len(self.sequence):
            twist = Twist()
            self.pub.publish(twist)
            # Optionally shut down node after some time
            return

        vx, wz, duration = self.sequence[self.current_step]
        now = self.get_clock().now()
        elapsed = (now - self.step_start_time).nanoseconds * 1e-9

        # If still in this step, publish its velocity
        if elapsed < duration or duration == 0.0:
            twist = Twist()
            twist.linear.x = vx
            twist.angular.z = wz
            self.pub.publish(twist)
        else:
            # Move to next step
            self.current_step += 1
            self.step_start_time = now
            self.get_logger().info(f"Switching to step {self.current_step}/{len(self.sequence)}")


def main(args=None):
    rclpy.init(args=args)
    node = LoopClosurePathNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop robot on exit
        twist = Twist()
        node.pub.publish(twist)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
