class IoTDevice:
    __slots__ = ("device_id", "status", "battery_level", "device_type")

    def __init__(self, device_id, status, battery_level, device_type="Device"):
        self.device_id = device_id
        self.status = status
        self.battery_level = battery_level
        self.device_type = device_type

    def get_status(self):
        return self.status

    def turn_on(self):
        if self.battery_level == 0:
            print(f"{self.device_type} {self.device_id} battery is empty")
        if self.status == "off":
            self.status = "on"
            print(f"{self.device_type} {self.device_id} turned on")
        else:
            print(f"{self.device_type} {self.device_id} is already on")

    def turn_off(self):
        if self.status == "on":
            self.status = "off"
            print(f"{self.device_type} {self.device_id} turned off")
        else:
            print(f"{self.device_type} {self.device_id} is already off")

    def check_battery(self):
        if self.battery_level == 0:
            return (f"{self.device_type} {self.device_id} battery is empty")
        else:
            return (
                f"{self.device_type} {self.device_id} battery level: {self.battery_level}%"
            )


class Lamp(IoTDevice):
    pass


class Thermostat(IoTDevice):
    __slots__ = ("temperature",)

    def set_temperature(self, temperature):
        if temperature >= 18 and temperature <= 30:
            self.temperature = temperature
            print(
                f"{self.device_type} {self.device_id} set temperature to {temperature}°C"
            )
        else:
            print(f"Invalid temperature. Temperature should be between 18 and 30°C.")

    def get_temperature(self):
        return self.temperature


class Camera(IoTDevice):
    def record_video(self):
        print(f"Camera {self.device_id} recording video...")


lamp = Lamp(device_id="L123", status="off", battery_level=100)
thermostat = Thermostat(device_id="T456", status="on", battery_level=75)
camera = Camera(device_id="C789", status="on", battery_level=50)

# Управление устройствами
lamp.turn_on()
thermostat.set_temperature(22)
camera.record_video()

# Мониторинг состояния
print(lamp.check_battery())  # Проверка заряда лампы
print(thermostat.get_temperature())  # Проверка температуры термостата
print(camera.get_status())  # Статус камеры

# Отключение устройств
lamp.turn_off()
camera.turn_off()
