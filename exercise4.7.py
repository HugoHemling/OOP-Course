class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []  # List to store persons in the room

    def add(self, person):
        """Adds a person to the room"""
        self.persons.append(person)

    def is_empty(self):
        """Returns True if the room is empty, otherwise False"""
        return len(self.persons) == 0

    def print_contents(self):
        """Prints the number of persons, total height, and details of each person"""
        if self.is_empty():
            print("The room is empty.")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm.")
            for person in self.persons:
                print(person)

    def shortest(self):
        """Returns the shortest person in the room without removing them"""
        if self.is_empty():
            return None
        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self):
        """Removes the shortest person from the room and returns them"""
        if self.is_empty():
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person

# Example usage:
room = Room()
print("Is the room empty?", room.is_empty())

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))

print("Is the room empty?", room.is_empty())

# Finding the shortest person
shortest_person = room.shortest()
print("Shortest:", shortest_person)

# Removing the shortest person
removed = room.remove_shortest()
print(f"Removed from room: {removed.name}\n")

room.print_contents()
