from picotazo_y_a_la_rama.temperature import Temperature


class TemperatureTestClass(Temperature):

    def get_threshold(self):
        return 50
