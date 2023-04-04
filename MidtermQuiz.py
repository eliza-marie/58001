class DistanceConversion:

    def __init__(self, distance):
        self.__dstnc = distance

    def __meter_to_centimeter(self):
        return self.__dstnc * 100

    def meter_to_kilometer(self):
        return self.__dstnc / 1000

    def meter_to_inch(self):
        return self.__dstnc * 39.37

    def convert_distance(self):
        return (self.__meter_to_centimeter(), self.meter_to_kilometer(), self.meter_to_inch())

meter_distance = float(input("Enter distance in meters: "))

md = DistanceConversion(meter_distance)

cm_distance, km_distance, inch_distance = md.convert_distance()
print(f"{meter_distance} meters to {cm_distance} centimeters")
print(f"{meter_distance} meters to {km_distance} kilometers")
print(f"{meter_distance} meters to {inch_distance} inches.")
