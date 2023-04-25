from abc import ABC


class Tire(ABC):
    def __inti__(self, tire_wear = []):
        self.tire_wear = tire_wear

    def needs_service(self):
        pass

