from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, current_date, last_service_date, tire_wear=[]):
        self.current_date = current_date
        self.last_service_date = last_service_date
        super().__init__(tire_wear)

    def needs_service(self, tire_wear):
        for tw in tire_wear:
            if tw >= 0.9:
                return True
            else:
                return False