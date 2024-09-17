GatorTaxi Ride-Share Service

Author: Kushagra Sikka

Introduction

GatorTaxi is a ride-sharing service designed to efficiently handle multiple ride requests every day. The company aims to develop software that manages and keeps track of pending ride requests effectively. This project involves designing and implementing this software using two data structures:

	•	Red-Black Tree (RBT): Stores ride information ordered by ride number.
	•	Min-Heap: Stores ride information ordered by estimated cost and trip duration.

Features

The software supports the following six operations:

	1.	Insert (rideNumber, rideCost, tripDuration)
	2.	Print (rideNumber)
	3.	Print (rideNumber1, rideNumber2)
	4.	UpdateTrip (rideNumber, newTripDuration)
	5.	GetNextRide ()
	6.	CancelRide (rideNumber)

Both the RBT and min-heap are maintained using pointers between corresponding nodes to ensure synchronization between the two data structures.

Design and Implementation

The software is implemented in Python and includes separate classes for the RBT and min-heap data structures. Enumerated constants are used within the RBT class for clarity and code organization.

Operations

	•	Insert Operation:
	•	Checks if the rideNumber already exists in the RBT.
	•	If it doesn’t exist, inserts the ride information into both the RBT and min-heap.
	•	Print Operation:
	•	Searches for the ride using rideNumber.
	•	Prints the triplet (rideNumber, rideCost, tripDuration) if found; otherwise, prints (0, 0, 0).
	•	Print Range Operation:
	•	Traverses subtrees of the RBT that may contain rides within the specified range.
	•	Prints all triplets (rideNumber, rideCost, tripDuration) within the range, separated by commas.
	•	If no rides are found, prints (0, 0, 0).
	•	UpdateTrip Operation:
	•	Searches for the ride using rideNumber.
	•	Updates the trip duration in both the RBT and min-heap based on newTripDuration.
	•	If newTripDuration exceeds a certain factor, the ride is canceled with a penalty.
	•	GetNextRide Operation:
	•	Selects the ride with the lowest rideCost from the min-heap.
	•	If multiple rides have the same rideCost, selects the one with the lowest tripDuration.
	•	Deletes the ride from both the RBT and min-heap.
	•	CancelRide Operation:
	•	Searches for the ride using rideNumber.
	•	Deletes it from both the RBT and min-heap if it exists.

Installation and Running the Program

To run the GatorTaxi program with a specific input file, use the following command in the terminal:
```bash
make run input_file=input.txt
```
```bash
python3 gatorTaxi.py < input.txt
```
	•	Replace input.txt with the name of your input file.
	•	The program will automatically generate the output file output_file.txt in the same directory.

Note: The Makefile is configured to use Python 3 as the interpreter. If you have multiple versions of Python installed, ensure you’re using the correct command for Python 3. You may need to modify the Makefile to reflect the location of your Python 3 installation.

Testing

Testing is crucial to ensure the software works as expected and meets project requirements. Various test cases were created to validate the functionality:

	•	Insert Operation Tests:
	•	Ensured ride numbers are unique.
	•	Verified that duplicate ride numbers are not inserted.
	•	Print Operation Tests:
	•	Checked that the correct triplet is printed for a given rideNumber.
	•	Confirmed that (0, 0, 0) is printed if the rideNumber does not exist.
	•	Print Range Operation Tests:
	•	Verified that all triplets within the specified range are printed.
	•	Ensured (0, 0, 0) is printed if no rides exist within the range.
	•	UpdateTrip Operation Tests:
	•	Confirmed that trip durations are updated correctly.
	•	Checked that rides are canceled with a penalty if newTripDuration exceeds certain limits.
	•	GetNextRide Operation Tests:
	•	Ensured that the ride with the lowest rideCost and tripDuration is returned and deleted.
	•	CancelRide Operation Tests:
	•	Verified that the specified ride is deleted.
	•	Ensured no errors occur if the rideNumber does not exist.

These tests cover various scenarios and edge cases, such as inserting duplicate rides, updating trip durations, and printing ride details. By performing these tests, we ensure that the GatorTaxi program functions correctly and meets all project requirements.

Test Cases Screenshots

Please refer to the test_cases directory for screenshots of the test cases.

Complexity Analysis

The GatorTaxi system utilizes two main data structures to store and manage ride requests: a min-heap and a Red-Black Tree.

	•	Min-Heap: Maintains a priority queue based on rideCost and tripDuration, with the lowest values at the root.
	•	Red-Black Tree: Stores ride requests sorted by rideNumber.

Time Complexity for Operations

	1.	Print(rideNumber): O(log n)
	•	Searches the RBT for the specified rideNumber.
	•	Prints the triplet if found; otherwise, prints (0, 0, 0).
	2.	Print(rideNumber1, rideNumber2): O(log n + S)
	•	S is the number of triplets printed.
	•	Traverses relevant subtrees in the RBT.
	•	Prints all rides within the specified range.
	3.	Insert(rideNumber, rideCost, tripDuration): O(log n)
	•	Inserts the new ride into both the min-heap and RBT.
	4.	GetNextRide(): O(log n)
	•	Deletes the ride with the lowest rideCost from the min-heap.
	•	Updates the corresponding node in the RBT.
	5.	CancelRide(rideNumber): O(log n)
	•	Deletes the specified ride from both the min-heap and RBT.
	•	If the ride does not exist, no action is taken.
	6.	UpdateTrip(rideNumber, newTripDuration): O(log n)
	•	Updates the trip duration in both the min-heap and RBT.
	•	In worst-case scenarios (rare), the complexity may increase due to ride cancellation and penalty insertion.

Overall: All operations have a time complexity of O(log n), dominated by the efficiencies of the min-heap and Red-Black Tree.

Conclusion

We successfully designed and implemented the GatorTaxi ride-sharing service software using a Red-Black Tree and a min-heap data structure. The software efficiently manages and keeps track of pending ride requests while maintaining synchronization between the two data structures.

Contact

For any questions or further information, please contact:

	•	Name: Kushagra Sikka
	•	Email: kushagrasikka@ufl.edu

Please feel free to contribute to this project or report any issues you encounter.
