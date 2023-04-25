from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, current_date, last_service_date, tire_wear=[]):
        self.current_date = current_date
        self.last_service_date = last_service_date
        super().__init__(tire_wear)

    def needs_service(self, tire_wear):
        tw = sum(tire_wear)
        if tw >= 3:
            return True
        return False
