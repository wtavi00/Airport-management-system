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

class Airlines:
    def __init__(self, name, luggage_weight):
        self.name = name
        self.luggage_weight = luggage_weight
        self.weight_limits = {"AirIndia": 30, "Emirates": 35, "British Airways": 35}

    def check_luggage(self):
        weight_limit = self.weight_limits.get(self.name, 0)
        if weight_limit == 0:
            print("Invalid airline")
        elif self.luggage_weight <= weight_limit:
            print("Check-in cleared")
        else:
            print("Remove some luggage and come back")

class Ticketing:
    @staticmethod
    def generate_tickets(no_of_passengers, starting_ticket_number):
        print("Ticket Numbers for all the Passengers:")
        for _ in range(no_of_passengers):
            print(f"T - {starting_ticket_number}")
            starting_ticket_number += 1
            
class Pricing:
    @staticmethod
     def calculate_total_ticket_cost(no_of_adults, no_of_children):
        adults_price = 37550.0
        children_price = adults_price / 3
        service_tax = 0.07
        discount = 0.10

         rate_of_adults = adults_price * no_of_adults
        rate_of_children = children_price * no_of_children
        total_cost = rate_of_adults + rate_of_children

        total_with_tax = total_cost + (service_tax * total_cost)
        total_with_discount = total_with_tax - (total_with_tax * discount)
         
        return total_with_discount

class Passport:
    @staticmethod
    def check_validity(passport_no):
        if len(passport_no) == 8 and passport_no[0].isalpha():
            return "valid"
        return "invalid"

