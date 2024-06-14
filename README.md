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

### Screenshots

1. **Status of all packages loaded onto each truck between 8:35 a.m. and 9:25 a.m.**
   - ![Screenshot1](screenshots/screenshot1.png)

2. **Status of all packages loaded onto each truck between 9:35 a.m. and 10:25 a.m.**
   - ![Screenshot2](screenshots/screenshot2.png)

3. **Status of all packages loaded onto each truck between 12:03 p.m. and 1:12 p.m.**
   - ![Screenshot3](screenshots/screenshot3.png)

4. **Total mileage traveled by all trucks**
   - ![Screenshot4](screenshots/screenshot4.png)
