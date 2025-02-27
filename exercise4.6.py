class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} g)"

class Box:
    def __init__(self):
        self.presents = []  # List to store presents

    def add_present(self, present):
        self.presents.append(present)  # Add present to the list

    def total_weight(self):
        return sum(present.weight for present in self.presents)  # Sum up the weights of all presents

# Example usage:
book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)

box = Box()
box.add_present(book)
print(box.total_weight())  

cd = Present("Pink Floyd: Dark Side of the Moon", 50)
box.add_present(cd)
print(box.total_weight())  
