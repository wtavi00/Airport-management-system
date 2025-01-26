class Runway:
    def __init__(self, status):
        self.status = status

    def get_status(self):
        return self.status

class Flight:
    def __init__(self, fuel_status):
        self.fuel_status = fuel_status

    def display_status(self, runway_status):
        if runway_status == "free":
            print("Land")
            self.display_landing_process()
        elif self.fuel_status == "low":
            print("Emergency landing")
            self.display_landing_process()
        else:
            print("Circle in the air")
