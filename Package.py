import datetime


class Package:
    # Initializes a package object with all necessary details.
    # Big O Time Complexity: O(1), due to direct attribute assignments that are independent of input size.
    # Big O Space Complexity: O(1) The space required does not depend on the size of the input but is fixed per instance
    def __init__(self, package_id, delivery_address, delivery_city, delivery_state, delivery_zip_code,
                 delivery_deadline, package_weight, delivery_status):
        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip_code = delivery_zip_code
        self.delivery_deadline = delivery_deadline
        self.package_weight = package_weight
        self.delivery_status = delivery_status
        self.departure_time = None  # Initialized as None; to be updated when the package leaves the hub.
        self.delivery_time = None  # Initialized as None; to be set upon delivery.
        self.truck_number = None

    # Provides a string representation of the package, detailing its attributes.
    # Big O Time Complexity: O(1), directly returns a formatted string.
    # Big O Space Complexity: O(1), generates a string of constant size relative to the package's attributes.
    def __str__(self):
        return f"Package ID: {self.package_id}, Truck Number: {self.truck_number}, Address: {self.delivery_address}, " \
               f"City: {self.delivery_city}, State: {self.delivery_state}, Zip: {self.delivery_zip_code}, " \
               f"Deadline: {self.delivery_deadline}, Weight: {self.package_weight}KILO, " \
               f"Status: {self.delivery_status}, Delivery Time: {self.delivery_time}"

    # Update the status of the package based on the current time
    # Big O Time Complexity: O(1), as it performs a fixed number of conditional checks and potential updates
    # Big O Space Complexity: O(1), since the method's space requirement does not scale with any input size.
    def update_status(self, current_time):
        if self.delivery_time < current_time:
            self.delivery_status = "Delivered"
        elif self.departure_time > current_time:
            self.delivery_status = "At Hub"
        elif self.departure_time < current_time < self.delivery_time:
            self.delivery_status = "In Route"

    # Special handling for package 9 to update its address after a specific time
        if self.package_id == 9:
            update_time = datetime.timedelta(hours=10, minutes=20)
            if current_time > update_time:
                self.delivery_address = "410 S State St, Salt Lake City, UT 84111"
            else:
                self.delivery_address = "300 State St, Salt Lake City, UT 84103"
