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
