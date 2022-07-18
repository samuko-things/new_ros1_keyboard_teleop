#!/usr/bin/env python

from __future__ import print_function

import threading

import roslib; #droslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped

import sys
from select import select

if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


TwistMsg = Twist
key_timeout = 0.5


moveBindings = {
        'i':(1,0,0,0),
        'o':(1,0,0,-1),
        'j':(0,0,0,1),
        'l':(0,0,0,-1),
        'u':(1,0,0,1),
        ',':(-1,0,0,0),
        '.':(-1,0,0,1),
        'm':(-1,0,0,-1),
        'O':(1,-1,0,0),
        'I':(1,0,0,0),
        'J':(0,1,0,0),
        'L':(0,-1,0,0),
        'U':(1,1,0,0),
        '<':(-1,0,0,0),
        '>':(-1,-1,0,0),
        'M':(-1,1,0,0),
        't':(0,0,1,0),
        'b':(0,0,-1,0),
    }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
    }




def getKey(settings, timeout):
    if sys.platform == 'win32':
        # getwch() returns a string on Windows
        key = msvcrt.getwch()
    else:
        tty.setraw(sys.stdin.fileno())
        # sys.stdin.read() returns a string on Linux
        rlist, _, _ = select([sys.stdin], [], [], timeout)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def saveTerminalSettings():
    if sys.platform == 'win32':
        return None
    return termios.tcgetattr(sys.stdin)

def restoreTerminalSettings(old_settings):
    if sys.platform == 'win32':
        return
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)





if __name__=="__main__":
    settings = saveTerminalSettings()

    try:
        while(1):
            key = getKey(settings, key_timeout)
            if key != '':
                print(ord(key))
            # if key in moveBindings.keys():
            #     x = moveBindings[key][0]
            #     y = moveBindings[key][1]
            #     z = moveBindings[key][2]
            #     th = moveBindings[key][3]
            # elif key in speedBindings.keys():
            #     speed = speed * speedBindings[key][0]
            #     turn = turn * speedBindings[key][1]

            # else:
            #     # Skip updating cmd_vel if key timeout and robot already
            #     # stopped.
            #     if key == '' and x == 0 and y == 0 and z == 0 and th == 0:
            #         continue
            #     x = 0
            #     y = 0
            #     z = 0
            #     th = 0
            if (key == '\x03'):
                print(key)
                print("keypress exited")
                break


    except Exception as e:
        print(e)

    finally:
        restoreTerminalSettings(settings)
