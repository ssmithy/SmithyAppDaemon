import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#


class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from HomeServer")
        self.log("You are now ready to run Apps!")
    
    def sayHello(self):
        return "Hello!"

