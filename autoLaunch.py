import libhousy
import time
#You can define helper functions here, make sure to but them *above* the main function
def launch(robot):
    robot.beltZ1.Set(-0.8)
    robot.beltZ2.Set(-0.8)
    robot.beltZ3.Set(1)
    robot.upperTension.Extend()
    robot.lowerTension.Retract()
    
firstRun = True
lastCount = 0
ticks = 0
launchTimer = 0
def main(robot: libhousy.robot):
    global firstRun, lastCount, ticks, launchTimer
    if firstRun:
        firstRun = False
        launchTimer = time.time()
    if robot.controller.getAxis(robot.controller.Axis.rTrigger) > 0.8:
       robot.shootWheel.Set(1)

    else:
        robot.shootWheel.Set(0)

    if time.time() - launchTimer >= 1:
        launchTimer = time.time()
        ticks = robot.shootCounter.Get() - lastCount
        lastCount = robot.shootCounter.Get()

    if ticks > 1800:
        launch(robot)

    else:
        robot.beltZ1.Set(0)
        robot.beltZ2.Set(0)
        robot.beltZ3.Set(0)

   

       
   
