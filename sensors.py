from dataclasses import dataclass
import random


@dataclass
class SensorModel:
    name: str
    value: float
    min_value: float
    max_value: float
    drift: float
    noise: float

    def read(self):
        # Slowly change the underlying sensor value
        self.value += random.uniform(-self.drift, self.drift)

        # Keep the underlying value inside the allowed range
        self.value = max(
            self.min_value,
            min(self.max_value, self.value)
        )

        # Add small measurement noise
        observed = self.value + random.uniform(
            -self.noise,
            self.noise
        )

        return round(observed, 2)


temperature_sensor = SensorModel(
    "temperature",
    72.0,
    65.0,
    95.0,
    0.35,
    0.20
)


vibration_sensor = SensorModel(
    "vibration",
    2.5,
    1.0,
    6.0,
    0.15,
    0.10
)


pressure_sensor = SensorModel(
    "pressure",
    6.0,
    4.5,
    7.5,
    0.10,
    0.05
)


energy_sensor = SensorModel(
    "energy",
    1.5,
    0.8,
    2.5,
    0.08,
    0.05
)


humidity_sensor = SensorModel(
    "humidity",
    55.0,
    40.0,
    70.0,
    0.30,
    0.20
)


def read_temperature():
    return temperature_sensor.read()


def read_vibration():
    return vibration_sensor.read()


def read_pressure():
    return pressure_sensor.read()


def read_energy():
    return energy_sensor.read()


def read_humidity():
    return humidity_sensor.read()


def read_all_sensors():
    return {
        "temperature": read_temperature(),
        "vibration": read_vibration(),
        "pressure": read_pressure(),
        "energy": read_energy(),
        "humidity": read_humidity()
    }