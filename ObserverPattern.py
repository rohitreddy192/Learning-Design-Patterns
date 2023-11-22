# Subject interface
class Subject:
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass

# Concrete Subject: Weather Station
class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)

# Observer interface
class Observer:
    def update(self, temperature):
        pass

# Concrete Observer 1: Temperature Display
class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Temperature Display: {temperature}°C")

# Concrete Observer 2: Phone App
class PhoneApp(Observer):
    def update(self, temperature):
        print(f"Phone App Notification: Weather updated to {temperature}°C")

if __name__ == "__main__":
    # Usage
    weather_station = WeatherStation()

    # Creating observers
    temp_display = TemperatureDisplay()
    phone_app = PhoneApp()

    # Attaching observers to the subject (weather station)
    weather_station.attach(temp_display)
    weather_station.attach(phone_app)

    # Setting temperature at the weather station
    weather_station.set_temperature(25)

"""
Subject Interface: Defines the operations for attaching, detaching, and notifying observers.
Concrete Subject (Weather Station): Maintains a list of observers, notifies them upon a state change (temperature update).
Observer Interface: Specifies the update operation for observers.
Concrete Observers: TemperatureDisplay and PhoneApp implement the update method to react to temperature changes.

In this scenario, when the WeatherStation updates its temperature, it notifies all attached observers. 
The TemperatureDisplay and PhoneApp receive the update and display or react to the new temperature accordingly.

"""