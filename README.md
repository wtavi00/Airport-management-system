The Airline Management System is a Python-based project that simulates various aspects of airline operations, including ticketing, passenger management, luggage handling, and security checks. This program is designed to provide a modular and functional approach by leveraging object-oriented programming principles.

Features

Runway Status Display: Determine actions (landing, emergency landing, or circling) based on runway and fuel conditions.

Passenger and Ticket Management: Handle ticket generation and passenger-specific data.

Luggage Check: Validate luggage weight against airline policies and calculate extra baggage charges if applicable.

Security Check: Ensure all passengers and their baggage are cleared through security.

Dynamic Baggage Limit: Update baggage limits and calculate extra baggage charges accordingly.

## Class Structure

### `AirlineSystem`
Handles the overall operations and integration of other components. Responsible for managing the execution flow of the system.

### `Passenger`
Represents an individual passenger with attributes such as name, ticket status, and passport status. Contains methods to validate passports and manage ticket confirmation.

### `Luggage`
Manages baggage-related operations, including weight validation, extra luggage charges, and dynamic baggage limit updates.

### `Ticketing`
Responsible for generating tickets, assigning ticket numbers, and calculating total ticket costs for passengers (adults and children).

### `SecurityCheck`
Handles security clearance for passengers and their baggage. Ensures compliance with security protocols.

## How to Use
1. Clone the repository:
   ```bash
   https://github.com/wtavi00/Airport
   ```
 2. Navigate to the project directory:
   ```bash
   cd airline-management-system
   ```  
3. Run the program:
   ```bash
   python airline_system.py
   ```


## Sample Workflow

1. Input runway and fuel status to determine whether a flight can land.
2. Generate tickets for passengers, including validating their luggage weight and handling extra baggage charges.
3. Conduct security checks for passengers and baggage.
4. Output ticket costs and additional charges for all passengers

   
## Future Enhancements
- Add a graphical user interface (GUI) for better user experience.
- Include database integration to manage passenger data more effectively.
- Enhance security protocols with real-time validation.

## Authier
[Avijit Tarafder](https://github.com/wtavi00)

## License
   [MIT License](https://github.com/wtavi00/Airport/blob/main/LICENSE)
