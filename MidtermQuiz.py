class DistanceConversion:
    def __init__(self, distance):
        self.__distance = distance  # using mangling to encapsulate distance attribute

    def meter_into_centimeter(self):
        return self.__distance * 100

    def meter_into_kilometer(self):
        return self.__distance / 1000

    def meter_into_inch(self):
        return self.__distance * 39.37


distance_in_meters = float(input("Enter distance value: "))

dc = DistanceConversion(distance_in_meters)

print("Distance value in centimeters:", dc.meter_into_centimeter())
print("Distance value in kilometers:", dc.meter_into_kilometer())
print("Distance value in inches:", dc.meter_into_inch())