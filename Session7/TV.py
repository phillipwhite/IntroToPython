class TV:
    def __init__(self):
        self._volume = 1
        self._channel = 1
        self._on = True

    def __int__(self, channel=1, volumeLevel=1, on=False):
        self._channel = channel
        self._volume = volumeLevel
        self._on = on

    def turnOn(self):
        pass

    def turnOff(self):
        self._on = False

    def getChannel(self):
        return self._channel

    def setChannel(self, channel):
        self._channel = channel

    def getVolume(self):
        return self._volume

    def setVolume(self, volumeLevel):
        self._volume = volumeLevel

    def channelUp(self):
        if self._channel < 120:
            self._channel += 1

    def channelDown(self):
        if self._channel > 1:
            self._channel -= 1

    def volumeUp(self):
        if self._volume < 7:
            self._volume += 1

    def volumeDown(self):
        if self._volume > 1:
            self._volume -= 1


tv1 = TV()
print(tv1.getChannel())

# tv2 = TV(15)
# print(tv2.getChannel())
# tv2.setChannel(150)
# print(tv2.getChannel())
