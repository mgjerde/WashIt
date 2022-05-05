# Planning
## General thoughts
* Should or should there not be added some extra time for emptying of machines etc?
* Should the end user be able to select their own time or get time based on the availability of the machines
## Thoughts on the reservations
* Having every machine stored as an object, and storing information like the different reservations in that object.
* Have the reservations check through all the machines and stored in the first available timeslot.

## Thoughts on interface
* For simplicity sake the idea is to make a menu system controlled by a single function that displays and asks for the needed input.
* It should also have a simple check that the input is valid.

# Part 2

## Identification of enduser
This I ended up somewhat implementing in part 1 as part of the cancellation functionality, the identification process could be expanded upon with a password, and all user related information stored in a class on its own.
## Check-in for end user
This could be solved with adding a "in use" flag on the Washingmachine class, and a scheduler that checks this flag in specific intervals, and if the flag is not set after the 15 minutes, delete the reservation and check for users on the waiting list
## Adding a dryer
For this i would split the Washingmachine class into three classes;
* A general "machine" class with the general information
* Two specific classes ("Washingmachine"/"Dryer") that inherited from the machine class, and with the added specifics for the different machines.