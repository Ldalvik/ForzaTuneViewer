from tuningapi.Schema import Tuning

class TuningData:
    def __init__(self, tuningBytes):
        self.tuningBytes = tuningBytes

    # getters
    @property
    def aero_front(self): 
        return self.get_other(Tuning.AERO_FRONT)

    @property
    def aero_rear(self): 
        return self.get_other(Tuning.AERO_REAR)


    # setters
    @aero_front.setter
    def aero_front(self, value):
        self.set_value(Tuning.AERO_FRONT, value)

    @aero_rear.setter
    def aero_rear(self, value):
        self.set_value(Tuning.AERO_REAR, value)

        


    # Normalization functions
    def set_value(self, index, value, min=0, range=1):
        self.tuningBytes[index.value] = (value - min) / range

    def set_neg_value(self, index, value):
        self.tuningBytes[index.value] = (100 - value) / 100

    def get_value(self, index, min, range):
        return (self.tuningBytes[index.value] * range) + min
    
    def get_neg_value(self, index):
        value = (self.tuningBytes[index.value] * 10.0) + (-5.0)
        return round(value * 10.0) / 10.0
        
    def get_other(self, index):
        return (self.tuningBytes[index.value])
    
    # braking balance only
    def get_sub_value(self, index):
        return ((100 - self.tuningBytes[index.value]) * 100) / 100
