import csv
import datetime
from hashtable import HashMap
from Trucks import Truck
from packages import Packages
from datetime import timedelta

#Amanuel Biru
# student ID : 011707742
# NHP3 TASK 2: WGUPS ROUTING PROGRAM

with open("distanceCSV.csv", mode="r+", encoding="utf-8-sig") as distance_csv:
    # Read the distance data from the distance.csv file
    distance_data = csv.reader(distance_csv)
    # Convert the distance data to a list
    distance_data = list(distance_data)

with open("addressCSV.csv", mode="r+", encoding="utf-8-sig") as address_csv:
    # Read the address data from the address.csv file
    address_data = csv.reader(address_csv)
    # Convert the address data to a list
    address_data = list(address_data)

with open("packageCSV.csv", mode="r", encoding="utf-8-sig") as packages_csv:
    # Read the package data from the packages.csv file
    package_data = csv.reader(packages_csv)

    next(package_data)
    # Convert the package data to a list
    package_array = list(package_data)

def loadPackageData(package_array, myHash):
    for package in package_array:
        packageID, pStreet, pCity, pState, pZip, pDeadline, pWeight, pNotes = package[:8]
        pStatus = "At Hub"

        package_data = Packages(int(packageID), pStreet, pCity, pState, pZip, pDeadline, pWeight, pStatus, pNotes)
        myHash.insert(int(packageID), package_data)

myHash = HashMap()
loadPackageData(package_array, myHash)

#updating route status for each package location

def update_status(package, current_time):
    # Convert package.depart_time to datetime.timedelta if it's a string
    if isinstance(package.departure_time, str):
        package.departure_time = datetime.timedelta(
            hours=int(package.departure_time.split(":")[0]),
            minutes=int(package.departure_time.split(":")[1]),
            seconds=int(package.departure_time.split(":")[2])
        )

    # Update the status attribute based on the value of `current_time`.
    if package.departure_time < current_time:
        package.status = "Delivered " " AT "
    elif package.departure_time > current_time:
        package.status = "en route"
    else:
        package.status = "at the hub"


#using the csv uplaod the distance into the function to calculate the 2 distance in between 
def find_distance_between(address_1, address_2):
    distance = distance_data[address_1][address_2]
    if distance == '':
        distance = distance_data[address_2][address_1]
    return float(distance)

def addressData(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])

# Entered all the trucks manually 
wgups_location = "4001 South 700 East"
truck1 = Truck(wgups_location, 16, datetime.timedelta(hours=8), None, 0.0,
               [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 18)
truck2 = Truck(wgups_location, 16, datetime.timedelta(hours=8), None, 0.0,
               [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 18)
truck3 = Truck(wgups_location, 16, datetime.timedelta(hours=8), None, 0.0,
               [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 18)

def find_nearest_neighbor(truck_address, xdelivered_packages):
    # using the nearest neighbor algorithm package to the truck's current address
    nearest_package = min(
        xdelivered_packages,
        key=lambda pvalue: find_distance_between(truck_address, addressData(pvalue.address))
    )
    return nearest_package

def deliver_with_nearest_neighbor(truck, xdelivered_packages):
    current_address = addressData(truck.address)
    upcomingPackage = find_nearest_neighbor(current_address, xdelivered_packages)

    truck.packages.append(upcomingPackage.packageID)
    xdelivered_packages.remove(upcomingPackage)

    distance = find_distance_between(current_address, addressData(upcomingPackage.address))
    time = datetime.timedelta(hours=distance / truck.speed)
    
    #calculating  the distance and time
    truck.mph += distance
    truck.address = upcomingPackage.address
    truck.time += time

    upcomingPackage.deliver_time = truck.time
    upcomingPackage.departure_time = truck.time
#go through the package list deliver all the packages after that 
def Package_delivrd(truck):
    notDelivered = [myHash.get(packageID) for packageID in truck.packages]
    truck.packages.clear()

    while notDelivered:
        deliver_with_nearest_neighbor(truck, notDelivered)

# Deliver with truck 1
Package_delivrd(truck1)

# deliver with truck2
Package_delivrd(truck2)

# delivery times of truck 1 and truck 2
truck3.departure_time = min(truck1.time, truck2.time)

# packages with truck 3 need to be delivered
Package_delivrd(truck3)


# Calculate the total route distance
total_distance_mph = truck1.mph + truck2.mph + truck3.mph

# Display the total route distance
print("The total mileage traveled by all trucks is:", total_distance_mph, "miles")

# Ask the user to type "start" to begin
text = input("Type `start` to begin.\n")

# If the user didn't type "start", print the error message and exit the program
if text != "start":
    print("Not a valid input. Exiting.")
    exit()

# Ask the user to input the time for the report in the format: HOURS:MINUTES:SECONDS
time_delta_inputs = input(
    "Please provide a time for the full detail status use format: HOURS:MINUTES:SECONDS\n"
)

# Try to split the time input into hours, minutes, and seconds and convert it to a timedelta object
try:
    (hours, minutes, seconds) = time_delta_inputs.split(":")
    rtime = datetime.timedelta(
        hours=int(hours), minutes=int(minutes), seconds=int(seconds)
    )
# If the user didn't provide the time in the correct format, print the error message and exit the program
except ValueError:
    print("Invalid input. Exiting.")
    exit()

# Ask the user if they want to generate a report for all packages or just an individual package
package_type_input = input(
    "Type `all` to generate  all the packages.\nType `one` to generate  individual package.\n"
)

# Set the initial package ID range to iterate over
package_id_range = range(1, 41)

# If the user wants to generate  individual package:
if package_type_input == "one":
    # provide the package id
    single_input = input("Please enter the package_id\n")
    package_id_range = [int(single_input)]

# Try to look up the packages and update their statuses
try:
    for packageID in package_id_range:
        package = myHash.get(packageID)
        update_status(package,rtime)
        print(str(package))
# If there is an error, print the error message and exit the program
except ValueError:
    print("Invalid input. Exiting.")
    exit()


        
        
        
        
        


    
