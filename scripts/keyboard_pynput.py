
from pynput.keyboard import Key, KeyCode, Listener




# key_buffer = None

# def press(key):
#     global key_buffer
    
#     if key == Key.up:
#         if key_buffer == None:
#             key_buffer = Key.up
#             # print(key_buffer)
#             print("up_key pressed")

#     elif key == Key.down:
#         if key_buffer == None:
#             key_buffer = Key.down
#             # print(key_buffer)
#             print("down_key pressed")

#     elif key == Key.left:
#         if key_buffer == None:
#             key_buffer = Key.left
#             # print(key_buffer)
#             print("left_key pressed")

#     elif key == Key.right:
#          if key_buffer == None:
#             key_buffer = Key.right
#             # print(key_buffer)
#             print("right_key pressed")
   


# def release(key):
#     global key_buffer

#     if key == Key.up:
#         if key_buffer == Key.up:
#             key_buffer = None
#             print("up_key released")

#     elif key == Key.down:
#         if key_buffer == Key.down:
#             key_buffer = None
#             print("down_key released")

#     elif key == Key.left:
#         if key_buffer == Key.left:
#             key_buffer = None
#             print("left_key released")

#     elif key == Key.right:
#         if key_buffer == Key.right:
#             key_buffer = None
#             print("right_key released")

#     elif key == Key.esc:
#         # Stop listener
#         return False




## ###     read combination of more than one key i.e three keys      #####
## ###     one can also apply it to two keys by making the key_buffer array to take two elements      #####
key_buffer = [None, None, None]

def press(key):
    global key_buffer
    
    if key == Key.up:
        if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                print("up_key pressed")

    elif key == Key.down:
        if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                print("down_key pressed")

    elif key == Key.left:
        if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                print("left_key pressed")

    elif key == Key.right:
         if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                print("right_key pressed")
    
    elif key == Key.alt:
         if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                # print("right_key pressed")
    
    elif key == Key.space:
         if key not in key_buffer:
            if None in key_buffer:
                key_buffer[key_buffer.index(None)] = key
                print(key_buffer)
                # print("right_key pressed")
   


def release(key):
    global key_buffer
    
    if key == Key.up:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            print("up_key released")

    elif key == Key.down:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            print("down_key released")

    elif key == Key.left:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            print("left_key released")

    elif key == Key.right:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            print("right_key released")

    elif key == Key.alt:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            # print("left_key released")

    elif key == Key.space:
        if key in key_buffer:
            key_buffer[key_buffer.index(key)] = None
            print(key_buffer)
            # print("right_key released")

    elif key == Key.esc:
        # Stop listener
        return False





# speed_command = 0            # 0 is None,           1 is accelerate,            -1 is deccelerate to stop
# move_command = 0             # 0 is None,           1 is forward,                -1 is reverse
# direction_command = 0      # 0 is None,          1 is left_turn,               -1 is right turn


# def publishMotion(speed_cmd,  move_cmd, direction_cmd):
#     motion_code = [move_cmd, direction_cmd]


#     if speed_cmd == 1:
#         print('accelerator pedal pressed')
#     elif speed_cmd == -1:
#         print('brake pedal pressed') 
#     else:
#         print('no pedal pressed')



#     if motion_code == [0,0]:
#         print("motion stopped")

#     elif motion_code == [1,0]:
#         print("forward motion")
    
#     elif motion_code == [-1,0]:
#         print("reverse motion")
    
#     elif motion_code == [0,1]:
#         print("left motion")
    
#     elif motion_code == [0,-1]:
#         print("right motion")
    
#     elif motion_code == [1,1]:
#         print("forward + left motion")

#     elif motion_code == [1,-1]:
#         print("forward + right motion")
    
#     elif motion_code == [-1,1]:
#         print("reverse + left motion")
    
#     elif motion_code == [-1,-1]:
#         print("reverse + right motion")


# def press(key):
#     global speed_command,  move_command, direction_command
    
#     if key == Key.up:
#         if move_command == 0:
#             move_command = 1
#             publishMotion(speed_command,  move_command, direction_command)

#     elif key == Key.down:
#         if move_command == 0:
#             move_command = -1
#             publishMotion(speed_command,  move_command, direction_command)

#     if key == Key.left:
#         if direction_command == 0:
#             direction_command = 1
#             publishMotion(speed_command,  move_command, direction_command)

#     elif key == Key.right:
#          if direction_command == 0:
#             direction_command = -1
#             publishMotion(speed_command,  move_command, direction_command)

#     if key == Key.alt:
#          if speed_command == 0:
#             speed_command = 1
#             publishMotion(speed_command,  move_command, direction_command)
    
#     elif key == Key.space:
#          if speed_command == 0:
#             speed_command = -1
#             publishMotion(speed_command,  move_command, direction_command)
   


# def release(key):
#     global speed_command,  move_command, direction_command

#     if key == Key.up:
#         if move_command == 1:
#             move_command = 0
#             publishMotion(speed_command,  move_command, direction_command)

#     elif key == Key.down:
#         if move_command == -1:
#             move_command = 0
#             publishMotion(speed_command,  move_command, direction_command)

#     if key == Key.left:
#         if direction_command == 1:
#             direction_command = 0
#             publishMotion(speed_command,  move_command, direction_command)

#     elif key == Key.right:
#         if direction_command == -1:
#             direction_command = 0
#             publishMotion(speed_command,  move_command, direction_command)
    
#     if key == Key.alt:
#          if speed_command == 1:
#             speed_command = 0
#             publishMotion(speed_command,  move_command, direction_command)
    
#     elif key == Key.space:
#          if speed_command == -1:
#             speed_command = 0
#             publishMotion(speed_command,  move_command, direction_command)

#     elif key == Key.esc:
#         # Stop listener
#         return False


def main():
    # publishMotion(speed_command,  move_command, direction_command)
    # ...or, in a non-blocking fashion:
    listener = Listener(on_press=press, on_release=release)
    listener.start()
    listener.join()


if __name__=="__main__":
    main()

    