class SmartFan:
    def __init__(self,brand,speed=0,is_on=False):
        self.brand=brand         
        self.speed=speed          
        self.is_on=is_on
        print(f"[INIT] {self.brand} fan connected to the network.")

    def turn_on(self,speed):
        self.is_on =True
        self.speed = speed
        print(f"[ON] {self.brand} fan is now ON at {self.speed} RPM.")

    def turn_off(self):
        self.is_on = False
        self.speed = 0
        print(f"[OFF] {self.brand} fan is now OFF.")


obj=SmartFan("Crompton",100,True)
print(obj.is_on,obj.speed)
