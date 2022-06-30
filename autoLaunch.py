# inclue code to help us talk to the robot
from curses import start_color
import libhousy
import time
start_time = time.time()
last_count = 0
def main(robot: libhousy.robot):
    global start_time
    # Here is where your recurring code will go
    if robot.controller.getAxis(robot.controller.Axis.rTrigger) >=.8:
        robot.shootWheel.Set(1)

    else:
        robot.shootWheel.Set(0)
        robot.pickupMotor.Set(0)
        robot.pickupPneumatic.Retract()
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)
    
    if time.time() - start_time > 0.5:
        start_time = time.time()

        if robot.shootCounter.Get() - last_count  > 950:

            robot.beltZ1.Set(-0.8)
            robot.beltZ2.Set(-0.8)
            robot.beltZ3.Set(1)
            robot.upperTension.Extend()
            robot.lowerTension.Retract()
   
    
    # After everything is done, we tell the main program to stop us
   