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
            
    @staticmethod
    def display_landing_process():
        print("Flight has landed")
        print("Proceed for Immigration Check")
        passenger_count = 1
        while passenger_count <= 5:
            print(f"Immigration check done for passenger, {passenger_count}")
            passenger_count += 1
        print("No_Of_Passengers=", passenger_count - 1)
        print("Collect the baggage from the conveyor belt")
        print("Baggage count", 150)
        print("All bags have been collected")
