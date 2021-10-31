from singleton_decorator import singleton


@singleton
class Cordinates():
    CORDINATES = []

    def get_cordinates(self):
        return self.CORDINATES

    def set_cordinated(self,arr):
        self.CORDINATES = arr

    def set_cordinates_null(self):
        self.CORDINATES = []