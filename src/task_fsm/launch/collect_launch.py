import sys
import launch
import launch_ros.actions
import launch_ros.descriptions

def generate_launch_description():
    '''
    :author: Nelson Durrant
    :date: November 2024

    Launches the nodes needed for the collection task.

    :return: The launch description.
    '''

    for arg in sys.argv:
        if arg.startswith('param_file:='):
            param_file = arg.split(':=')[1]

    return launch.LaunchDescription([
        
        launch_ros.actions.Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            arguments=['serial', '--dev', '/dev/ttyACM0', '-b', '6000000'],
        ),
        launch_ros.actions.Node(
            package='task_fsm',
            executable='collect_fsm.py',
            parameters=[param_file],
        ),
        launch_ros.actions.Node(
            package='navigation',
            executable='drive_controller.py',
            parameters=[param_file],
        ),
        launch_ros.actions.Node(
            package='navigation',
            executable='drive_interface.py',
            parameters=[param_file],
        ),
        launch_ros.actions.Node(
            package='sorting',
            executable='egg_id.py',
            parameters=[param_file],
        ),
        launch_ros.actions.Node(
            package='sorting',
            executable='camera_interface.py',
            parameters=[param_file],
        ),
    ])