class WaterPump:
    public_number_field = 0
    public_string_field = "Default"

    def __init__(self, power=0, brand="Unknown", flow_rate=0):
        self.__power = power
        self.__brand = brand
        self.__flow_rate = flow_rate

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_flow_rate(self):
        return self.__flow_rate

    def set_flow_rate(self, flow_rate):
        self.__flow_rate = flow_rate

    def __str__(self):
        return f"Водяний насос марки {self.__brand}: потужність {self.__power} Вт, " \
               f"об'єм води {self.__flow_rate} л/год."

    def __repr__(self):
        return f"WaterPump(power={self.__power}, brand='{self.__brand}', flow_rate={self.__flow_rate})"

    def __del__(self):
        print(f"Видаляється об'єкт насоса марки {self.__brand}")

def main():
    pump1 = WaterPump(1200, "Grundfos", 3000)
    pump2 = WaterPump(1500, "Wilo", 3500)
    pump3 = WaterPump(1000, "Pedrollo", 2500)

    print(pump1)
    print(repr(pump1))

    print(pump2)
    print(repr(pump2))

    print(pump3)
    print(repr(pump3))

if __name__ == "__main__":
    main()
