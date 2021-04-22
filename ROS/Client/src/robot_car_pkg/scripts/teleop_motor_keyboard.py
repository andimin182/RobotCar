#!/usr/bin/env python
import rospy
import threading
from std_msgs.msg import String
import sys, select, termios, tty

print('Modules loaded succesfully...')

screen_msg = """
Reading from the keybard and Publishing to /command topic as String
----------------------
Moving around:
    w
  a   d
    z

Changing speed:
TBD

Anything else: STOP

CTRL-C to quit
 """

moveBindings= {
    'w': 'forward',
    'W': 'forward',
    'z': 'backward',
    'Z': 'backward',
    'a': 'left',
    'A': 'left',
    'd': 'right',
    'D': 'right'
}

class PublishThread(threading.Thread):
    def __init__(self, rate):
        super(PublishThread, self).__init__()
        self.publisher = rospy.Publisher('/command', String, queue_size = 1)
        self.commande = None
        self.condition = threading.Condition()
        self.done = False

        # Set timeout to None if rate is 0 (causes new_message to wait forever
        # for new data to publish)
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None

        self.start()

    def wait_for_subscribers(self):
        i = 0
        while not rospy.is_shutdown() and self.publisher.get_num_connections() == 0:
            if i == 4:
                print("Waiting for subscriber to connect to {}".format(self.publisher.name))
            rospy.sleep(0.5)
            i += 1
            i = i % 5
        if rospy.is_shutdown():
            raise Exception("Got shutdown request before subscribers connected")

    def update(self, commande):
        self.condition.acquire()
        self.commande = commande
        
        # Notify publish thread that we have a new message.
        self.condition.notify()
        self.condition.release()

    def stop(self):
        self.done = True
        self.update('stop')
        self.join()

    def run(self):
        commande_msg = String()
        while not self.done:
            self.condition.acquire()
            # Wait for a new message or timeout.
            self.condition.wait(self.timeout)

            # Copy state into twist message.
            commande_msg.data = self.commande

            self.condition.release()

            # Publish.
            self.publisher.publish(commande_msg)

        # Publish stop message when thread exits.
        commande_msg.data = 'stop'
        self.publisher.publish(commande_msg)


def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


#def vels(speed, turn):
#    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('teleop_motor_keyboard')
    rospy.loginfo('Teleop motor keyboard publisher initialized...')
    repeat = rospy.get_param("~repeat_rate", 0.0)
    key_timeout = rospy.get_param("~key_timeout", 0.0)
    if key_timeout == 0.0:
         key_timeout = None

    pub_thread = PublishThread(repeat)

    # Initialize the commande to the stop string commande 
    commande = 'stop'

    try:
        pub_thread.wait_for_subscribers()
        pub_thread.update(commande)

        print(screen_msg)
        
        while(1):
            key = getKey(key_timeout)
            if key in moveBindings.keys():
                commande = moveBindings[key]

            else:
                # Skip updating command if key timeout and robot already
                # stopped.
                if key == '' and commande =='stop':
                    continue
                commande = 'stop'
                if (key == '\x03'):
                    break
 
            pub_thread.update(commande)

    except Exception as e:
        print(e)

    finally:
        pub_thread.stop()

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)