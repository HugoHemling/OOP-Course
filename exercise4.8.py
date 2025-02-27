class Recording:
    def __init__(self, length):
        self.__length = length  # Private attribute

    @property
    def length(self):
        """Getter method for length"""
        return self.__length

    @length.setter
    def length(self, new_length):
        """Setter method for length"""
        self.__length = new_length

# Example usage:
the_wall = Recording(43)
print(the_wall.length)  # Output: 43

the_wall.length = 44
print(the_wall.length)  # Output: 44

