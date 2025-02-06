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


carriage = TrainCarriage("A1", 10)
carriage.add_reservation(1)
carriage.add_reservation(2)
print(carriage.get_reservation_report())
carriage.remove_reservation(1)
carriage.reset_reservations()
print(carriage.get_reservation_report())
print(carriage.is_full())