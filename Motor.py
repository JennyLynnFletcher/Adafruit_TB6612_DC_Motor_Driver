import RPi.GPIO as GPIO

class Motor(object):
    def __init__(self, pwm_pin, in1_pin, in2_pin):

        self._pwm_pin = pwm_pin
        self._in1_pin = in1_pin
        self._in2_pin = in2_pin

        self._direction = "forward"
        self._speed = 0
        self._stopped = True
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pwm_pin, GPIO.OUT)
        GPIO.setup(self._in1_pin, GPIO.OUT)
        GPIO.setup(self._in2_pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pwm_pin, 60)
        self._pwm.start(0)
        print("init")
        
    def _set_direction(self, direction):
        if direction == "forward":
                self._pwm.ChangeDutyCycle(0)
                GPIO.output(self._in1_pin, GPIO.LOW)
                GPIO.output(self._in2_pin, GPIO.HIGH)
                self._pwm.ChangeDutyCycle(self._speed)
                print("forward")
        if direction == "backward":
                self._pwm.ChangeDutyCycle(0)
                GPIO.output(self._in1_pin, GPIO.HIGH)
                GPIO.output(self._in2_pin, GPIO.LOW)
                self._pwm.ChangeDutyCycle(self._speed)
                print("backward")
                
    def _set_speed(self, speed):
        self._pwm.ChangeDutyCycle(self._speed)
        print("speed: " + str(self._speed))
        
    @property    
    def speed(self):
        return self._speed
        
    @speed.setter
    def speed(self, value):
        if value <= 100 and value >= 0:
            self._speed = value
        else:
            print("Speed value needs to be between 0 and 100")            
        if not self._stopped:
            self._set_speed(self._speed)       
        
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, direction):
        if direction == self._direction:
            changed = False
        else:
            changed = True
        self._direction = direction
        if changed:
            self._set_direction(self._direction)
        
    @property
    def stop(self):
        return self._stopped
    
    @stop.setter
    def stop(self, stopped):
        if stopped == self._stopped:
            changed = False
        else:
            changed = True
        self._stopped = stopped
        if self._stopped and changed:
            GPIO.output(self._in1_pin, GPIO.LOW)
            GPIO.output(self._in2_pin, GPIO.LOW)
            self._pwm.stop()
            print("stop")
        if not self._stopped and changed:
            self._pwm.start(0)
            self._set_direction(self._direction)
            self._set_speed(self._speed)
            print("start")

            
        
        
        
    
        
