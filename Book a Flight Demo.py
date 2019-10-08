# .Description: Python script to book flights for learning/exercising purposes
# .Author: Martin
# .Version: 1.0

print("The tool is starting up...")

#Destinations
Destinations = {"1": "London",
                "2": "Paris",
                "3": "Amsterdam",
                "4": "New York",
                "5": "Los Angeles",
                "6": "Manila",
                "7": "Singapore"}

#Departure Times
DepartureTimes = {"1": "8:00",
                "2": "12:00",
                "3": "16:00",
                "4": "20:00",}

FlightPrices = {"1": "250$",
                "2": "200$",
                "3": "180$",
                "4": "165$",}

def PrintDestinations():
    for keys, values in Destinations.items():
        print(keys, values)


def PrintTimes():
    for keys, values in DepartureTimes.items():
        print(keys, values)

def DestinationSelector():
    InputDestination = input("Please choose a destination from the list above. (Enter a number between 1-7)")
    if int(InputDestination) >= 1 and int(InputDestination) <= 7:
        return InputDestination
    else:
        print("Please enter a number between 1-7.")

UserName = input("Please enter your full name. (E.g. Mozzie Mozz)")
PassPort = input("Please enter your passport number. (E.g. X123456)")

PrintDestinations()

ReturnedDestination = DestinationSelector()

PrintTimes()

def TimeSelector():
    InputTime = input("Please choose a time for your flight. (Enter a number between 1-4)")
    if int(InputTime) >= 1 and int(InputTime) <= 4:
        return InputTime
    else:
        print("Please enter a number between 1-4.")

ReturnedTime = TimeSelector()

print("Summary:")
print("Passenger Name: " + UserName)
print("Passport Number: " + PassPort)
print("Selected Destination " + Destinations[ReturnedDestination])
print("Selected Time " + DepartureTimes[ReturnedTime])
print("Flight Price: " + FlightPrices[ReturnedTime])

Receipt = input("Would you like a receipt? Type y or n")

def ExportReceipt():
    r = open("Receipt.txt","w+")
    r.write("Summary:")
    r.write("\nPassenger Name: " + UserName)
    r.write("\nPassport Number: " + PassPort)
    r.write("\nSelected Destination: " + Destinations[ReturnedDestination])
    r.write("\nSelected Time: " + DepartureTimes[ReturnedTime])
    r.write("\nFlight Price: " + FlightPrices[ReturnedTime])

if Receipt is "y":
    ExportReceipt()
else:
    print("Thank you for saving the planet. Just kidding, it's a digital receipt anyway.")