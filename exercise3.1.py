# File name: exercise3.1.py
# Author: Hugo Hemling
# Description: Defines a Train class that manages a list of TrainCarriage objects.

class TrainCarriage:
    def __init__(self, identifier, total_seats):
        self.identifier = identifier
        self.total_seats = total_seats
        self.reserved_seats = set()

    def add_reservation(self, seat_number):
        if seat_number < 1 or seat_number > self.total_seats:
            raise ValueError("Invalid seat number")
        if seat_number in self.reserved_seats:
            raise ValueError("Seat already reserved")
        self.reserved_seats.add(seat_number)

    def remove_reservation(self, seat_number):
        if seat_number not in self.reserved_seats:
            raise ValueError("Seat not reserved")
        self.reserved_seats.remove(seat_number)

    def reset_reservations(self):
        self.reserved_seats.clear()

    def is_full(self):
        return len(self.reserved_seats) == self.total_seats

    def get_reservation_report(self):
        reserved = sorted(self.reserved_seats)
        unreserved = sorted(set(range(1, self.total_seats + 1)) - self.reserved_seats)
        return f"Reserved seats: {reserved}\nUnreserved seats: {unreserved}"

class Train:
    """
    Represents a train composed of multiple carriages. Allows adding,
    removing carriages, reserving seats, and generating reservation reports.
    """
    
    def __init__(self, train_id, departure, destination, initial_carriage):
        """
        Initializes the Train with a unique ID, departure and destination,
        and at least one carriage.
        """
        if not isinstance(initial_carriage, TrainCarriage):
            raise TypeError("Initial carriage must be a TrainCarriage object")
        
        self.train_id = train_id
        self.departure = departure
        self.destination = destination
        self.carriages = [initial_carriage]
    
    def add_carriage(self, carriage):
        """Adds a new carriage to the train."""
        if not isinstance(carriage, TrainCarriage):
            raise TypeError("Carriage must be a TrainCarriage object")
        self.carriages.append(carriage)
    
    def remove_carriage(self, carriage_id):
        """Removes a carriage from the train by its identifier."""
        if len(self.carriages) == 1:
            raise ValueError("A train must have at least one carriage")
        
        for carriage in self.carriages:
            if carriage.identifier == carriage_id:
                self.carriages.remove(carriage)
                return
        
        raise ValueError("Carriage not found")
    
    def reserve_seat(self, seat_number):
        """Reserves a seat in the first available carriage with free seats."""
        for carriage in self.carriages:
            if not carriage.is_full():
                carriage.add_reservation(seat_number)
                return
        
        raise ValueError("No available seats in any carriage")
    
    def get_train_reservation_report(self):
        """Generates a report of all reserved and free seats in the train."""
        report = [f"Train ID: {self.train_id}\nDeparture: {self.departure}"
                  f"\nDestination: {self.destination}\n"]
        
        for carriage in self.carriages:
            report.append(f"Carriage {carriage.identifier}:\n" +
                          carriage.get_reservation_report())
        
        return "\n".join(report)
    
    def get_train_info(self):
        """Returns general information about the train."""
        return {
            "train_id": self.train_id,
            "departure": self.departure,
            "destination": self.destination,
            "carriage_count": len(self.carriages)
        }

# Example usage
if __name__ == "__main__":
    carriage1 = TrainCarriage("C1", 20)
    train = Train("T123", "New York", "Boston", carriage1)
    
    carriage2 = TrainCarriage("C2", 15)
    train.add_carriage(carriage2)
    
    train.reserve_seat(3)
    train.reserve_seat(5)
    
    print(train.get_train_reservation_report())
