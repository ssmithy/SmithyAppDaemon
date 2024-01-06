import appdaemon.plugins.hass.hassapi as hass
import datetime
#
# Testing the ability to test freeze time with HASS/AD events
#
# Args:
#

class TimerApp(hass.Hass):

    event_flag = None
    time_flag = None

    def initialize(self):
        self.log("Timer Test App")
        if(datetime.datetime.now().hour >= 7 and datetime.datetime.now().hour <= 20):
            self.time_flag = 99
        else:
            self.time_flag = 66

        self.event_flag = 1
        self.run_in(self.sayHello, 5)
    
    def sayHello(self):
        self.event_flag = 2
        return "Hello!"

