import json
import time

from config import DEVICE_CONFIG
from sensors import read_all_sensors
from telemetry import build_telemetry


def determine_status(readings):
    temperature = readings["temperature"]
    vibration = readings["vibration"]
    pressure = readings["pressure"]

    # Critical conditions
    if temperature >= 90:
        return "FAULT"

    if vibration >= 5:
        return "FAULT"

    if pressure < 4.8 or pressure > 7.2:
        return "FAULT"

    # Warning conditions
    if temperature >= 85:
        return "WARNING"

    if vibration >= 4:
        return "WARNING"

    if pressure < 5.0 or pressure > 7.0:
        return "WARNING"

    return "RUNNING"


def generate_telemetry():
    """
    Generate one complete telemetry message.
    """

    readings = read_all_sensors()

    status = determine_status(readings)

    device_config = DEVICE_CONFIG.copy()
    device_config["status"] = status

    telemetry = build_telemetry(device_config, readings)

    return telemetry


def run_simulation(cycles=5, interval=1):
    for _ in range(cycles):

        telemetry = generate_telemetry()

        print(json.dumps(telemetry, indent=2))
        print("-" * 60)

        time.sleep(interval)


def test_status():
    test_cases = [
        {
            "name": "Normal",
            "temperature": 72.0,
            "vibration": 2.5,
            "pressure": 6.0
        },
        {
            "name": "Temperature Warning",
            "temperature": 87.0,
            "vibration": 2.5,
            "pressure": 6.0
        },
        {
            "name": "Temperature Fault",
            "temperature": 92.0,
            "vibration": 2.5,
            "pressure": 6.0
        },
        {
            "name": "Vibration Warning",
            "temperature": 72.0,
            "vibration": 4.5,
            "pressure": 6.0
        },
        {
            "name": "Vibration Fault",
            "temperature": 72.0,
            "vibration": 5.5,
            "pressure": 6.0
        }
    ]

    for test in test_cases:

        readings = {
            "temperature": test["temperature"],
            "vibration": test["vibration"],
            "pressure": test["pressure"]
        }

        status = determine_status(readings)

        print(
            f'{test["name"]}: '
            f'Temperature={test["temperature"]}, '
            f'Vibration={test["vibration"]}, '
            f'Pressure={test["pressure"]} '
            f'→ {status}'
        )


if __name__ == "__main__":
    run_simulation(cycles=5, interval=1)