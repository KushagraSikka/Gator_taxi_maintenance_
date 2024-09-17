# code by Kushagra Sikka
# UFID: 3979-0988
# ADS Project final submission

import sys
from min_heap import MinHeap
from rb_tree import RBTree
# this is the gator taxi class which is calling the functions from the min heap and the rb tree


class GatorTaxi:
    def __init__(self):
        self.min_heap = MinHeap()
        self.rb_tree = RBTree()
# this is the get next ride function which returns the next ride in the heap

    def get_next_ride(self):
        next_ride = self.min_heap.extract_min(self.rb_tree)
        if next_ride is not None:
            print(str(next_ride).replace(" ", ""))
        else:
            print("No active ride requests")
# this is the print ride function which prints the ride info of the ride number

    def print_ride(self, ride_number):
        ride_info = self.rb_tree.get_ride(ride_number)
        print(ride_info.replace(" ", ""))
# this is the print rides in range function which prints the rides in the range of the ride numbers

    def print_rides_in_range(self, ride_number1, ride_number2):
        rides_in_range = self.rb_tree.get_range(ride_number1, ride_number2)
        print(rides_in_range.replace(" ", ""))
# this is the update trip function which checks the new trip duration and updates the heap accordingly

    def update_trip(self, ride_number, new_trip_duration):
        node = self.rb_tree.search(ride_number)
        if node is not None and node != self.rb_tree.nil:
            _, ride_cost, trip_duration = node.ride_info
            if new_trip_duration <= trip_duration:
                updated_ride_info = (
                    ride_number, ride_cost, new_trip_duration)
                self.rb_tree.update_ride_info(ride_number, updated_ride_info)
                self.min_heap.update_trip(
                    ride_number, new_trip_duration, self.rb_tree)
            elif trip_duration < new_trip_duration <= 2 * trip_duration:
                updated_ride_info = (
                    ride_number, ride_cost + 10, new_trip_duration)
                self.rb_tree.update_ride_info(ride_number, updated_ride_info)
                self.min_heap.update_trip(
                    ride_number, new_trip_duration, self.rb_tree)
            elif new_trip_duration > 2 * trip_duration:
                self.rb_tree.delete(ride_number)
                self.min_heap.remove_ride(ride_number)
# this is the cancel ride function which cancels the ride and updates the heap accordingly

    def cancel_ride(self, ride_number):
        self.rb_tree.delete(ride_number)
        self.min_heap.remove_ride(ride_number)
# this function processes the input file and calls the functions accordingly

    def process_input_file(self, input_file):
        with open(input_file, 'r') as file:
            for line in file:
                operation, params = line.strip().split('(')
                params = params.rstrip(')').split(',')
                if operation == "Insert":
                    # print(f"Inserting Ride: {params} \n")
                    ride_info = (int(params[0]), int(
                        params[1]), int(params[2]))
                    self.min_heap.insert(ride_info, self.rb_tree)
                elif operation == "GetNextRide":
                    # print("Getting next ride\n")
                    self.get_next_ride()
                elif operation == "Print":
                    # print("Printing ride(s)", params, "\n")
                    ride_numbers = tuple(map(int, params))
                    if isinstance(ride_numbers, tuple) and len(ride_numbers) == 1:
                        self.print_ride(ride_numbers[0])
                    elif isinstance(ride_numbers, tuple) and len(ride_numbers) == 2:
                        self.print_rides_in_range(
                            ride_numbers[0], ride_numbers[1])
                elif operation == "UpdateTrip":
                    # print("Updating trip duration", params, "\n")
                    ride_number, new_trip_duration = int(
                        params[0]), int(params[1])
                    self.update_trip(ride_number, new_trip_duration)
                elif operation == "CancelRide":
                    # print("Cancelling ride", params, "\n")
                    ride_number = int(params[0])
                    self.cancel_ride(ride_number)

# this is the main function which takes the input file as an argument and calls the process input file function


def main():
    if len(sys.argv) != 2:
        print("Usage: python gatorTaxi.py <input_file>")
        return

    input_file = sys.argv[1]
    gator_taxi = GatorTaxi()

    # Redirect standard output to a file
    original_stdout = sys.stdout
    with open("output_file.txt", "w") as output_file:
        sys.stdout = output_file
        gator_taxi.process_input_file(input_file)

    # Restore original standard output
    sys.stdout = original_stdout


if __name__ == "__main__":
    main()
