class WeatherStation:
    def __init__(self, name):
        self.__name = name  # Private attribute for station name
        self.__observations = []  # Private list to store observations

    def add_observation(self, observation: str):
        """Adds an observation as the last entry in the list"""
        self.__observations.append(observation)

    def latest_observation(self):
        """Returns the latest observation added to the list, or an empty string if none exist"""
        return self.__observations[-1] if self.__observations else ""

    def number_of_observations(self):
        """Returns the total number of observations added"""
        return len(self.__observations)

    def __str__(self):
        """Returns the name of the station and the total number of observations"""
        return f"{self.__name}, {len(self.__observations)} observations"

# Example usage:
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation()) 

station.add_observation("Thunderstorm")
print(station.latest_observation())  

print(station.number_of_observations())  
print(station) 
