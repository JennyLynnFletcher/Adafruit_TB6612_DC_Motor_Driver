import Motor
import time

def test():
    motorA = Motor.Motor(22,24,23)
    motorB = Motor.Motor(27,20,21) 
    motorA.stop = False
    motorB.stop = False
    motorA.speed = 40
    motorB.speed = 40
    time.sleep(2)
    motorA.direction = "backward"
    motorB.direction = "backward"
    time.sleep(2)
    motorA.stop = True
    motorB.stop = True
    
if __name__ == '__main__':
    test()
