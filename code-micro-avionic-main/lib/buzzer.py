########################################
#### BerryRocket ####
# Buzzer management module
# Louis Barbier
# MIT License
########################################

import time
from machine import Pin,PWM,Timer

# Buzzer class
class Buzzer():
    '''
    Module for buzzer
    '''

    # init
    def __init__(self, pin, enable=True):
        self._pwm_buzzer = PWM(Pin(pin))
        self._enable = enable

        # Internal variables
        self._timer_on = Timer()
        self._timer_off = Timer()
        self.freq = 500

    # Initialisation musique
    def init_music(self):
        notes = (146.83,164.81,174.61,164.81,130.81,146.83,164.81,174.61,164.81,196.00,155.56,174.61,196.00,155.56,146.83,138.59,164.81)
        notes = tuple(x*2 for x in notes) # Augmente d'une octave la musique
        tempsNotes = (1.5,0.5,0.5,0.5,1,1.5,0.5,0.5,0.5,1,1.5,0.5,1,1,1,2,2)
        bpm = 75
        if self._enable is True:
            self._pwm_buzzer.duty_u16(0) # Set to 0%
            self._pwm_buzzer.duty_u16(32768) # Set to 50%
            for iNote in range(0, len(notes)):
                self._pwm_buzzer.freq(round(notes[iNote]))
                time.sleep((60.0/bpm)*tempsNotes[iNote])

        self._pwm_buzzer.duty_u16(0) # Set to 0%

    @property
    def enable(self):
        return self._enable
    
    @enable.setter
    def enable(self, value):
        self._enable = value
        if self._enable is False:
            self._timer_on.deinit()
            self.off()

    def on(self, t=None, freq=None):
        """Put on the buzzer once"""
        if freq != None:
            self.freq = freq
        if self._enable is True:
            self._pwm_buzzer.freq(self.freq)
            self._pwm_buzzer.duty_u16(32768) # Set to 50%
            self._timer_off.init(freq=1.0/0.1, mode=Timer.ONE_SHOT, callback=self.off) # Ring the buzzer for 0.1s

    def off(self, t=None):
        """Put off the buzzer"""
        self._pwm_buzzer.duty_u16(0) # Set to 0%

    def set(self, freq=500, period=5.0):
        """Set reapeting buzzer with a frequency and a period between ring"""
        self.freq = freq
        self._timer_on.deinit()
        if self._enable is True:
            self._timer_on.init(freq=1.0/period, mode=Timer.PERIODIC, callback=self.on)

    def unset(self):
        """Unset the repeat buzzer"""
        self._timer_on.deinit()