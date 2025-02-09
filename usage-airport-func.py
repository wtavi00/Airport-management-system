print("# Runway and Flight Status")
runway = Runway(input("The status of the runway: "))
fuel_status = input("If the fuel status is low, type 'low': ")
flight = Flight(fuel_status)
flight.display_status(runway.get_status())

print("\n# Airline Check-In")
airline_name = input("Input the name of the airlines (AirIndia, Emirates, British Airways): ")
  
