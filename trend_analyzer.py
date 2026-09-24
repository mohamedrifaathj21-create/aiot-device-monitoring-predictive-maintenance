def calculate_trend(values):
    """
    Calculate whether a sensor is increasing,
    decreasing, or stable.
    """

    if len(values) < 3:
        return "INSUFFICIENT_DATA"

    first = values[0]
    last = values[-1]

    difference = last - first

    if difference > 0.5:
        return "INCREASING"

    elif difference < -0.5:
        return "DECREASING"

    else:
        return "STABLE"


def analyze_sensor_trends(telemetry_history):
    """
    Analyze temperature, vibration and pressure trends.
    """

    if len(telemetry_history) < 3:
        return {
            "temperature": "INSUFFICIENT_DATA",
            "vibration": "INSUFFICIENT_DATA",
            "pressure": "INSUFFICIENT_DATA"
        }

    temperatures = [
        item["readings"]["temperature"]
        for item in telemetry_history
        if "readings" in item
        and "temperature" in item["readings"]
    ]

    vibrations = [
        item["readings"]["vibration"]
        for item in telemetry_history
        if "readings" in item
        and "vibration" in item["readings"]
    ]

    pressures = [
        item["readings"]["pressure"]
        for item in telemetry_history
        if "readings" in item
        and "pressure" in item["readings"]
    ]

    return {
        "temperature": calculate_trend(
            temperatures
        ),

        "vibration": calculate_trend(
            vibrations
        ),

        "pressure": calculate_trend(
            pressures
        )
    }