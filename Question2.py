
#Parent class is defined
class TV:
    def __init__(self,brand,price,inches):
        self.brand= brand
        self.channel = 1   # Default channel
        self.volume = 50   # Default volume
        self.price= price
        self.inches = inches
        self.on_off_status = False # TV is off by default

    def turn_on(self):
        self.on_off_status = True 

    def turn_off(self):
        self.on_off_status = False
    
    def increase_volume(self):
        if self.volume <100:
            self.volume += 1
    
    def decrease_volume(self):
        if self.volume >0:
            self.volume -=1
    
    def set_channel(self,new_channel):
        if 1<= new_channel <=50:
            self.channel = new_channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

#child1 class is created where parent is inherited- that means all propertied and methods of parent is inherited to this particular child
class LED(TV):
    def __init__(self,brand,price,inches,screen_thickness,energy_usage,lifespan,refresh_rate):
        super().__init__(brand,price,inches)
        self.screen_thickness=screen_thickness
        self.energy_usage = energy_usage
        self.lifespan =lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle=0
        self.backlight=False
        self.price=0
    
    def set_viewing_angle(self,angle):
        if 0<= angle <= 180:
            self.viewing_angle=angle
    
    def toggle_backlight(self):
        self.backlight = not self.backlight
    
    def display_details(self):
        return (f"Brand:{self.brand}\n"
                f"Channel:{self.channel}\n"
                f"Volume:{self.volume}\n"
                f"Screen Thickness:{self.screen_thickness}mm\n"
                f"Energy Usage:{self.energy_usage}W\n"
                f"Lifespan:{self.lifespan}hours\n"
                f"Refresh Rate:{self.refresh_rate} hz\n"
                f"Viewing Angle:{self.viewing_angle} degrees\n"
                f"Backlight:{'on' if self.backlight else 'off'}")


 #child2 class is created where parent is inherited- that means all propertied and methods of parent is inherited to this particular child   
class Plasma(TV):
    def __init__(self,brand,price,inches,screen_thickness,energy_usage,lifespan,refresh_rate):
        super().__init__(brand,price,inches)
        self.screen_thickness=screen_thickness
        self.energy_usage = energy_usage
        self.lifespan =lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle=0
        self.backlight=True
        self.price=0
    
    def set_viewing_angle(self,angle):
        if 0<= angle <= 180:
            self.viewing_angle=angle
    
    def toggle_backlight(self):
        self.backlight = not self.backlight
    
    def display_details(self):
        return (f"Brand:{self.brand}\n"
                f"Channel:{self.channel}\n"
                f"Volume:{self.volume}\n"
                f"Screen Thickness:{self.screen_thickness}mm\n"
                f"Energy Usage:{self.energy_usage}W\n"
                f"Lifespan:{self.lifespan}hours\n"
                f"Refresh Rate:{self.refresh_rate} hz\n"
                f"Viewing Angle:{self.viewing_angle} degrees\n"
                f"Backlight:{'on' if self.backlight else 'off'}")

#calling child1 and displaying the output
ledtv_object = LED("samsung",75000.00,65,20,110,50000,100)
ledtv_object.set_channel(32)
ledtv_object.increase_volume()
ledtv_object.decrease_volume()
print(ledtv_object.status())
print(ledtv_object.display_details())


#calling child2 and displaying the output
plasmatv_object = Plasma("LG",81000.00,55,35,150,70000,120)
plasmatv_object.set_channel(16)
plasmatv_object.increase_volume()
plasmatv_object.decrease_volume()
print(plasmatv_object.status())
print(60*"*")
print(plasmatv_object.display_details())


 





        
    
        


    

    
    
    
