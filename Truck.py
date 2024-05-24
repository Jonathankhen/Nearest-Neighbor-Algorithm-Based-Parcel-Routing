class Truck:
    # Initializes truck with specified attributes.
    # Big O Time Complexity: O(1), as the __init__ method performs a fixed number of assignments.
    # Big O Space Complexity: O(n), due to the variable number of packages stored in the list,
    # influencing the truck's memory usage.
    def __init__(self, capacity, speed, miles, current_location, depart_time, packages):
        self.capacity = capacity
        self.speed = speed
        self.miles = miles  # Distance the truck has traveled
        self.current_location = current_location
        self.depart_time = depart_time  # The time the truck departs from the hub.
        self.time = depart_time  # The current time for the truck, initially set to its departure time.
        self.packages = packages  # Packages assigned to the truck

    # Returns a string representation of the truck object and Compiles information about its current status.
    # Big O Time Complexity: iterates through packages to build a string.
    # linearly proportional to the number of packages
    # Big O Space Complexity: as the method constructs a string that grows in size with the number of packages.
    # Space used increases linearly with the number of packages included in the output string.
    def __str__(self):
        package_list = ', '.join(str(pkg) for pkg in self.packages)
        return (f"Speed: {self.speed} mph, Miles Traveled: {self.miles}, "
                f"Current Location: {self.current_location}, Departure Time: {self.depart_time},"
                f"Packages: [{package_list}]")
