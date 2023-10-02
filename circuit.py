from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time

zumi = Zumi()
screen = Screen()

# BROTHER CODE** 
#    (stationary(in-house)-->obstacle-->line following-->crescent)


# testing all features
#for i in range(0,50):
#    ir_readings = zumi.get_all_IR_data()
#    bottom_right_ir = ir_readings[1]
#    bottom_left_ir = ir_readings[3]
#    
#    message = "    IR readings        "
#    message = message + str(bottom_right_ir) + ", " + str(bottom_left_ir)
#    screen.draw_text(message)
#    time.sleep(0.1)
#screen.draw_text_center("Done!")


#--------------------Stage 1----------------------------
#Stationary (in-House)



#--------------------Stage 2-----------------------------
#Obstacle Avoidance

ir_readings = zumi.get_all_IR_data()
print(ir_readings)

direction = 0
zumi.reset_gyro()

# how to get correct IR readings for each time step? TODO

for x in range(300): # TODO
    
    #if zumi detects from front, stop, reverse a little bit, change direction by 180 (+ or -)
    if front_right_ir > 100 and front_left_ir > 100: # 100 is arbitrary value (needs testing)
        zumi.stop()
        zumi.reverse(30)
    
    # elif zumi detects front right, change direction left
    elif front_right_ir < 100:
        direction += 30
        print(front_right_ir)
    
    # elif zumi detects front left, change direction right
    elif front_left_ir < 100:
        direction -= 30
        print(front_left_ir)

zumi.stop()
print("Done!")

#---------------------Stage 3---------------------------
#Line Following (GOLD)

#zumi.line_follower(3, left_thresh=100,right_thresh=100) # threshold depending on tape lighting/color



#---------------------Stage 4---------------------------
#Line Following (MOON: crescent shape)

#zumi.line_follower(3, left_thresh=100,right_thresh=100) # threshold depending on tape lighting/color
