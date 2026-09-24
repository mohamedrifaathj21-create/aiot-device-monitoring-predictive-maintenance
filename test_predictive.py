from predictive_maintenance import predict_maintenance


# -----------------------------------------
# SIMULATED MACHINE TREND
# -----------------------------------------

telemetry = [
    {
        "readings": {
            "temperature": 72,
            "vibration": 2.0,
            "pressure": 5.5
        }
    },

    {
        "readings": {
            "temperature": 74,
            "vibration": 2.2,
            "pressure": 5.4
        }
    },

    {
        "readings": {
            "temperature": 76,
            "vibration": 2.5,
            "pressure": 5.3
        }
    },

    {
        "readings": {
            "temperature": 79,
            "vibration": 2.9,
            "pressure": 5.2
        }
    },

    {
        "readings": {
            "temperature": 82,
            "vibration": 3.4,
            "pressure": 5.1
        }
    }
]


# -----------------------------------------
# PREDICT MAINTENANCE
# -----------------------------------------

result = predict_maintenance(
    telemetry
)


print("\nPredictive Maintenance")
print("----------------------")

print(
    "Health Score:",
    result["health_score"]
)

print(
    "Health Status:",
    result["health_status"]
)

print(
    "Maintenance Risk:",
    result["maintenance_risk"]
)

print("\nSensor Trends")

print(
    "Temperature:",
    result["sensor_trends"]["temperature"]
)

print(
    "Vibration:",
    result["sensor_trends"]["vibration"]
)

print(
    "Pressure:",
    result["sensor_trends"]["pressure"]
)

print("\nRecommendation")

print(
    result["recommendation"]
)