# this is the min heap class which contains the functions to insert the ride info into the heap, get the next ride, update the trip duration, cancel the ride and remove the ride from the heap
class MinHeap:
    def __init__(self):
        self.heap = []
# this is the insert function which inserts the ride info into the heap

    def insert(self, ride_info, rb_tree):
        ride_number, ride_cost, trip_duration = ride_info
        if not rb_tree.insert(ride_info):
            print("Duplicate RideNumber")
            return

        self.heap.append(ride_info)
        self._bubble_up(len(self.heap) - 1)
# this is the get next ride function which returns the next ride in the heap

    def get_next_ride(self):
        if not self.heap:
            print("No active ride requests")
            return

        min_ride = self.extract_min(rb_tree)
        # print(min_ride)
        print(
            f"Ride Number: {min_ride[0]}, Ride Cost: {min_ride[1]}, Trip Duration: {min_ride[2]}")

    def cancel_ride(self, ride_number):
        index = self._get_index_by_ride_number(ride_number)
        if index is not None:
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._bubble_down(index)


# this is the update trip function which checks the new trip duration and updates the heap accordingly


    def update_trip(self, ride_number, new_trip_duration, rb_tree):
        index = self._get_index_by_ride_number(ride_number)
        if index is None:
            return
        _, ride_cost, trip_duration = self.heap[index]
        if new_trip_duration <= trip_duration:
            self.heap[index] = (ride_number, ride_cost, new_trip_duration)
            rb_tree.update_ride_info(
                ride_number, (ride_number, ride_cost, new_trip_duration))
        elif trip_duration < new_trip_duration <= 2 * trip_duration:
            self.heap[index] = (ride_number, ride_cost + 10, new_trip_duration)
            self._bubble_down(index)
            self._bubble_up(index)
            rb_tree.update_ride_info(
                ride_number, (ride_number, ride_cost + 10, new_trip_duration))
        elif new_trip_duration > 2*trip_duration:
            rb_tree.delete(ride_number)
            self.remove_ride(ride_number)

# this is the get index by ride number function which returns the index of the ride number in the heap
    def _get_index_by_ride_number(self, ride_number):
        for i, ride_info in enumerate(self.heap):
            if ride_info[0] == ride_number:
                return i
        return None
# this is the compare rides function which compares the rides based on the trip duration and the ride cost

    def _compare_rides(self, ride1, ride2):
        if ride1[1] < ride2[1] or (ride1[1] == ride2[1] and ride1[2] < ride2[2]):
            return -1
        elif ride1[1] == ride2[1] and ride1[2] == ride2[2]:
            return 0
        else:
            return 1
# this is the bubble up function which bubbles up the ride in the heap based on the trip duration and the ride cost

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self._compare_rides(self.heap[index], self.heap[parent]) < 0:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
# this is the bubble down function which bubbles down the ride in the heap based on the trip duration and the ride cost

    def _bubble_down(self, index):
        min_child = self._min_child_index(index)
        while min_child is not None and self._compare_rides(self.heap[index], self.heap[min_child]) > 0:
            self.heap[index], self.heap[min_child] = self.heap[min_child], self.heap[index]
            index = min_child
            min_child = self._min_child_index(index)
# this is the min child index function which returns the index of the child with the minimum trip duration and the ride cost

    def _min_child_index(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child >= len(self.heap):
            return None
        if right_child >= len(self.heap) or self.heap[left_child][1] < self.heap[right_child][1]:
            return left_child
        return right_child

# this is the remove ride function which removes the ride from the heap
    def extract_min(self, rb_tree):
        if not self.heap:
            return None

        min_ride = self.heap[0]
        last_ride = self.heap.pop()

        if self.heap:
            self.heap[0] = last_ride
            self._min_heapify(0)

        rb_tree.delete(min_ride[0])

        return min_ride
# this is the min heapify function which heapifies the heap based on the trip duration and the ride cost

    def _min_heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self._compare_rides(self.heap[left_child], self.heap[smallest]) < 0:
            smallest = left_child

        if right_child < len(self.heap) and self._compare_rides(self.heap[right_child], self.heap[smallest]) < 0:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._min_heapify(smallest)
# this is the remove ride function which removes the ride from the heap

    def remove_ride(self, ride_number):
        for i, ride in enumerate(self.heap):
            if ride[0] == ride_number:
                removed_ride = self.heap.pop(i)
                self._min_heapify(i)
                return removed_ride
        return None
