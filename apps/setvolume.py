import appdaemon.plugins.hass.hassapi as hass

class SetVolume(hass.Hass):
    """ 
    Set the volume of a speaker for day and night time.
    Optionally, periodically check and reset volume to preferred level

    Attributes:
        speaker: Id of the HASS Speaker
        dayStart: Integer hour the day starts, default 7 (7am)
        nightStart: Integer hour night time starts, default 20 (8pm)
        normalVolume: Integer normal volume %
        nightVolume: Integer night time volume %
        enforce: Boolean indicating whether to perform checks periodically 
                 to enforce the set volume at night time, default false
    """

    speaker = None
    dayStart = None
    nightStart = None
    normalVolume = None
    nightVolume = None
    enforce = None
    
    def initialize(self):
        log = "SetVolume for {entity}."
        self.log(log.format(entity = self.args["speaker"]))
        self.initParams()

    def initParams(self):
        # Set defaults
        self.speaker = self.args["speaker"]
        self.dayStart = self.args.get("dayStart", 7)
        self.nightStart = self.args.get("nightStart", 20)
        self.normalVolume = self.args["normalVolume"]
        self.nightVolume = self.args["nightVolume"]
        self.enforce = self.args["enforce"]
