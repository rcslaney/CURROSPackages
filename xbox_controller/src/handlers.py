import rospy  # in PyCharm shows error, solution: https://gavazzi.us/2017/07/31/pycharm-ros/
from std_msgs import msg


# PUBLISHERS
def drive_velocity_publish(vel):
    try:
        print("Starting to publish drive velocity...")
        msg_arr = msg.Float32MultiArray(data=vel)

        drive_velocity_pub.publish(msg_arr)
        print("Drive velocity publshed! " + str(drive_velocity_pub.get_num_connections()) + " nodes should have heard it")
    except rospy.ROSInterruptException:
        pass


def drive_distance_publish(pos):
    try:
        msg_arr = msg.Float32MultiArray(data=pos)

        drive_distance_pub.publish(msg_arr)
    except rospy.ROSInterruptException:
        pass


def drive_commands_publish(command):
    if type(command) is str:
        command = ord(command)
    try:
        msg_ch = msg.Char(data=command)

        drive_commands_pub.publish(msg_ch)
    except rospy.ROSInterruptException:
        pass


def flippers_velocity_publish(vel):
    try:
        msg_arr = msg.Float32MultiArray(data=vel)

        flippers_velocity_pub.publish(msg_arr)
    except rospy.ROSInterruptException:
        pass


def flippers_position_publish(pos):
    try:
        msg_arr = msg.Float32MultiArray(data=pos)

        flippers_velocity_pub.publish(msg_arr)
    except rospy.ROSInterruptException:
        pass


# FUNCTIONS
def publish_msg(topic, message):
    print("Trying to publish...")
    if topic == 'drive/velocity':
        drive_velocity_publish(message)
    elif topic == 'drive/distance':
        drive_distance_publish(message)
    elif topic == 'commands':
        drive_commands_publish(message)
    elif topic == 'flippers/velocity':
        flippers_velocity_publish(message)
    elif topic == 'flippers/position':
        flippers_position_publish(message)
    print("Ok ROS published on topic " + repr(topic))


def init_handlers():
    rospy.init_node('xbox_controller', anonymous=True)

    # PUBLISHERS

    global drive_velocity_pub
    drive_velocity_pub = rospy.Publisher('drive/velocity', msg.Float32MultiArray, queue_size=1)

    global drive_distance_pub
    drive_distance_pub = rospy.Publisher('drive/distance', msg.Float32MultiArray, queue_size=1)

    global drive_commands_pub
    drive_commands_pub = rospy.Publisher('commands', msg.Char, queue_size=20)

    global flippers_velocity_pub
    flippers_velocity_pub = rospy.Publisher('flippers/velocity', msg.Float32MultiArray, queue_size=1)

    global flippers_position_pub
    flippers_position_pub = rospy.Publisher('flippers/position', msg.Float32MultiArray, queue_size=1)
