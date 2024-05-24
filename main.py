from HashMap import HashMap
from Package import Package
from Truck import Truck
import csv
import datetime


# Reads a CSV file and returns its content as a list
# Big O Time Complexity: O(n) - as it needs to iterate over each line in the CSV.
# Big O Space Complexity: O(n) - stores each line of the CSV in memory.
def read_csv_file(file_path):
    with open(file_path) as file:
        csv_data = csv.reader(file)
        return list(csv_data)


# Loading data from CSV files into lists
CSV_Distance = read_csv_file("DistanceFile.csv")
CSV_Address = read_csv_file("AddressFile.csv")
CSV_Package = read_csv_file("PackageFile.csv")


# Function to load package data from a CSV file into a hash map.
# Big O Time Complexity: O(n) - iterates through each package entry once.
# Big O Space Complexity: O(n) - stores all package data in the hash map.
def load_packages_file(file_path, package_hash_map):
    package_info = read_csv_file(file_path)
    for row in package_info:
        package_id = int(row[0])
        delivery_address, delivery_city, delivery_state, delivery_zip_code = row[1:5]
        delivery_deadline, package_weight = row[5], float(row[6])
        delivery_status = "At Hub"

        # Package object
        package = Package(package_id, delivery_address, delivery_city, delivery_state,
                          delivery_zip_code, delivery_deadline, package_weight, delivery_status)

        # Populate the hash map with data
        package_hash_map.add(package_id, package)


# Initialize hash map for storing package data
package_hash_map = HashMap(capacity=40)  # Size set to accommodate expected package volume

# Load packages into the hash mao
load_packages_file('PackageFile.csv', package_hash_map)


# Calculates the distance between two addresses using the distance table.
# Big O Time Complexity: O(1) - direct access using indices to a pre-computed value in a matrix.
# Big O Space Complexity: O(1) - as it temporarily stores and returns a single float value.
def distance_between(address_index1, address_index2):
    distance = CSV_Distance[address_index1][address_index2]
    if distance == '':
        distance = CSV_Distance[address_index2][address_index1]
    return float(distance)


# Retrieves the index of an address from the address list.
# Big O Time Complexity: O(n) in the worst case, as it may scan the entire address list over all addresses.
# Big O Space Complexity: O(1) as it returns an integer index.
def get_address(address_name):
    for row in CSV_Address:
        if address_name in row[2]:
            return int(row[0])


# Initialize trucks with their package lists and other details.
# This part doesn't involve complex operations, initialization is O(1).
Truck1 = Truck(16, 18, 0.0, "HUB", datetime.timedelta(hours=8), [8, 13, 14, 15, 16, 19, 20, 21, 27, 30, 34, 35, 37, 39])
Truck2 = Truck(16, 18, 0.0, "HUB", datetime.timedelta(hours=10, minutes=20),
               [3, 5, 9, 10, 11, 12, 17, 18, 23, 28, 36, 38])
Truck3 = Truck(16, 18, 0.0, "HUB", datetime.timedelta(hours=9, minutes=5),
               [1, 2, 4, 6, 7, 22, 24, 25, 26, 29, 31, 32, 33, 40])


# Assigns each package to its respective truck by updating the package's truck_number attribute.
# Big O Time Complexity: O(n) for each truck, where n is the number of packages on the truck.
# Big O Space Complexity: O(1), as it modifies existing objects without allocating new memory.
def assign_packages_to_truck(truck, truck_number):
    for package_id in truck.packages:
        package = package_hash_map.get(package_id)  # Accessing a package in the hash map.
        if package:
            package.truck_number = truck_number  # Assigning a truck number to the package.


# Executing the assignment function for each truck.
# Big O Time Complexity: O(n) - iterate over each package across all trucks, where n is the total number of packages.
# Big O Space Complexity: O(1) - as package assignments modify existing objects without necessitating extra space.
assign_packages_to_truck(Truck1, 1)
assign_packages_to_truck(Truck2, 2)
assign_packages_to_truck(Truck3, 3)


# Simulates the delivery process of packages by each truck using the nearest neighbor algorithm which selects the next
# closest package destination as the truck's next stop.
# Big O Time Complexity: O(n^2) - due to the nested min function within the loop for finding the next nearest package.
# Big O Space Complexity: O(n) - stores not_delivered packages and updates as packages are delivered.
def deliver_packages(truck):
    # Initializes a list with packages that have not been delivered.
    # This list is dynamically updated as packages are delivered.
    not_delivered = [package_hash_map.get(packageID) for packageID in truck.packages]
    current_location = "HUB" # Starts the delivery from the HUB.

    # Continues the delivery process until all packages on the truck have been delivered.
    while not_delivered:
        # Finds the index of the current location in the distance data structure to calculate distances.
        current_location_index = get_address(current_location)
        # Chooses the next package based on the closest delivery address to the current location.
        # This is the core of the nearest neighbor algorithm, optimizing the delivery route in a greedy manner.
        next_package = min(not_delivered, key=lambda package: distance_between(current_location_index,
                                                                               get_address(package.delivery_address)))
        next_nearest_distance = distance_between(current_location_index, get_address(next_package.delivery_address))

        # adds the next closest package to the delivery list
        truck.packages.append(next_package.package_id)
        not_delivered.remove(next_package)  # Removes the delivered package from the not_delivered list.
        truck.miles += next_nearest_distance  # Accumulates the total miles traveled by the truck.
        # Updates the truck's current location to the last delivered package location.
        truck.current_location = next_package.delivery_address
        # Calculates the time taken to deliver this package based on the distance traveled and truck's average speed
        delivery_time_increase = datetime.timedelta(hours=next_nearest_distance / 18)
        truck.time += delivery_time_increase  # Updates the truck's clock with the delivery time.
        next_package.delivery_time = truck.time  # Marks the delivery time for the package.
        next_package.departure_time = truck.depart_time  # Records the truck's departure time for the package.

        # Sets up for the next iteration by updating the current location to the latest package's delivery address.
        current_location = next_package.delivery_address


# Initiate the package loading sequence for the trucks
deliver_packages(Truck1)
deliver_packages(Truck2)
# This line prevents Truck 3 from starting its route
# until at least one of Truck 1 or Truck 2 has finished delivering their packages.
Truck3.depart_time = min(Truck1.time, Truck2.time)
deliver_packages(Truck3)


# Main user interface for interaction with the delivery system.
# It allows for tracking the delivery status of packages at different times of the day.
# Big O Time Complexity: O(1) - Executes a fixed number of statements regardless of any input size.
# Big O Space Complexity: O(1) - Allocates a fixed amount of memory for variables regardless of any input size.
def main_user_interface():
    print("Western Governors University package delivery & tracking Service (WGUPS)")
    print("The total mileage traveled by all trucks for the route is:", Truck1.miles + Truck2.miles + Truck3.miles)
    # Prompt for starting the process or exiting
    text = input("To begin the process, please enter 'start'. Any other entry will terminate the program.")
    if text == "start":
        user_time_input() # Proceed to collect time input from user


# Collects time input from the user to check package status at that specific time.
# Big O Time Complexity: O(1) - Directly processes user input without iteration.
# Big O Space Complexity: O(1) - Uses a small, fixed amount of memory for the input and time conversion.
def user_time_input():
    try:
        user_time = input("Enter the time to view package status in the format HH:MM")
        (h, m) = user_time.split(":")  # Split input into hours and minutes
        # Convert string input into a timedelta object for comparison
        current_time = datetime.timedelta(hours=int(h), minutes=int(m))
        package_status_input(current_time)
    except ValueError:
        # Handle invalid time format
        print("Unrecognized input. Exiting program now.")
        exit()


# Determines whether to display the status of a single package or all packages based on the user's selection.
# Big O Time Complexity: O(1) - Evaluates a fixed set of conditions.
# Big O Space Complexity: O(1) - Minimal, constant memory use for the input handling.
def package_status_input(current_time):
    second_input = input("For the status of a single package, enter 'single'. To review all packages, input 'all'.")
    if second_input == "single":
        single_package_input(current_time)  # Proceed to input for a single package
    elif second_input == "all":
        all_packages_status(current_time)  # Display status for all packages
    else:
        exit()  # Exit if input is neither 'single' nor 'all'


# Processes user input for checking the status of a single package at the given time.
# Big O Time Complexity: O(1) - Operates on a single package lookup and update.
# Big O Space Complexity: O(1) - Memory usage does not scale with input size.
def single_package_input(current_time):
    try:
        # User enters the package ID to check its status
        solo_input = int(input("Enter the numeric package ID"))
        # Retrieve the package from the hash map using its ID
        package = package_hash_map.get(solo_input)
        # Update and print the package status based on the current time
        Package.update_status(package, current_time)
        print(package)
    except ValueError:
        # Handle non-integer inputs
        print("Unrecognized input. Exiting program now.")
        exit()


# Displays the status of all packages at the given time.
# Big O Time Complexity: O(n) - Requires iterating over each package for status updates, n is the number of packages,
# hence scales linearly with the number of packages.
# Big O Space Complexity: O(1) - Memory usage does not increase with the number of packages.
def all_packages_status(current_time):
    # Iterate over each package by ID, update its status, and print
    for package_id in range(1, 41):
        package = package_hash_map.get(package_id)
        Package.update_status(package, current_time)
        print(package)


if __name__ == "__main__":
    main_user_interface()  # Start the user interface for the package tracking system
