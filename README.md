# Nearest-Neighbor-Algorithm-Based-Parcel-Routing

This project implements a package routing program using the nearest neighbor algorithm to optimize delivery routes within a 140-mile limit. It includes a hash table for efficient package management and a real-time interface for status updates.

## Introduction

This project demonstrates the application of algorithms and data structures to solve a real-world programming problem. The Western Governors University Parcel Service (WGUPS) needs an efficient routing program to ensure timely deliveries of packages while adhering to specific constraints.

## Project Overview

### Scenario

WGUPS needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD). The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

### Assumptions

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Three trucks and two drivers are available.
- Drivers leave the hub no earlier than 8:00 a.m.
- Delivery and loading times are instantaneous.
- There is one special note associated with a package.
- The delivery address for package #9 will be corrected at 10:20 a.m.
- Distances provided are equal regardless of the direction traveled.
- The day ends when all 40 packages have been delivered.

## Requirements

### Customization Tasks

1. **Hash Table for Package Management**
   - Developed a hash table to manage package details efficiently.

2. **Look-up Function**
   - Implemented a look-up function to retrieve package details using the package ID.

3. **Package Routing Algorithm**
   - Implemented the nearest neighbor algorithm to optimize delivery routes within a 140-mile limit.
   - Ensured all packages are delivered on time while meeting all requirements.

4. **User Interface**
   - Provided an intuitive interface for viewing the delivery status and total mileage.
   - Included options to view the status of all packages at different times of the day.

### Code Files

#### Hash Table Implementation
- **File**: `HashMap.py`
Implemented hash table with insertion and look-up functions.

#### Package Class
- **File**: `Package.py`
Attributes and methods to manage package details.

#### Truck Class
- **File**: `Truck.py`
Attributes and methods to manage truck details and delivery process.

#### Main Program
- **File**: `main.py`
Implemented package loading, delivery simulation (using nearest neighbor algorithm), and user interface for tracking.

### How to Use the Interface

#### Launch the Program:
- Clone the repository and navigate to the project directory.
- Run the main.py file to start the program. This will initialize the package delivery system.

#### Starting the Process:
- You will see a prompt: To begin the process, please enter 'start'. Any other entry will terminate the program.
- Type start and press Enter to proceed.

#### Entering Time for Package Status:
- You will be prompted to enter the time in the format HH:MM to view the package status at a specific time of the day.
- Input the desired time and press Enter.

#### Choosing Package Status View:
- You will be asked to choose between viewing the status of a single package or all packages.
- Enter single to check the status of a single package or all to review the status of all packages.

#### Single Package Status:
- If you chose single, you will be prompted to enter the numeric ID of the package.
- Enter the package ID and press Enter to view its status.

#### All Packages Status:
- If you chose all, the program will display the status of all packages at the given time.

#### Exit the Program:
- The program will exit automatically if an unrecognized input is entered at any prompt.

### Screenshots

1. **Status of all packages loaded onto each truck between 8:35 a.m. and 9:25 a.m.**
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/7b63cb06-bbf9-40c4-9d6a-6558629c21f2)
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/92ea7f15-dafb-43a4-b667-1efae5582097)

2. **Status of all packages loaded onto each truck between 9:35 a.m. and 10:25 a.m.**
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/691f761e-e5b6-4941-823b-0c38dcf38365)
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/ca7ac6df-0022-4331-9e6d-5bb746dd2e5f)

3. **Status of all packages loaded onto each truck between 12:03 p.m. and 1:12 p.m.**
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/1658932e-e9e4-44fc-8b87-82693f126c03)
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/f71a82a6-959c-433f-b92b-0f9155da4e7e)

4. **Total mileage traveled by all trucks**
![image](https://github.com/Jonathankhen/Nearest-Neighbor-Algorithm-Based-Parcel-Routing/assets/121633526/cabd86f9-7977-443f-abdd-e88d7d3f3d8a)

