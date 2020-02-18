

class Temperature():

    def __init__(self, measure: int):
        if (measure < 0):
            raise Exception("Measure should be postive")
        self.measure = measure
