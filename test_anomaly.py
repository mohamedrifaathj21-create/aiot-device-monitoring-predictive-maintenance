from anomaly_detector import detect_anomalies


# Normal telemetry
telemetry = []

for i in range(10):

    telemetry.append({
        "readings": {
            "temperature": 72 + (i * 0.1),
            "vibration": 2.0 + (i * 0.02),
            "pressure": 5.2 + (i * 0.02)
        }
    })


# Add an unusual reading
telemetry.append({
    "readings": {
        "temperature": 95.0,
        "vibration": 8.0,
        "pressure": 8.0
    }
})


anomalies = detect_anomalies(
    telemetry
)


print("\nAnomaly Detection Result")
print("------------------------")

if anomalies:

    for anomaly in anomalies:

        print(
            f"⚠️ {anomaly['sensor'].upper()} "
            f"ANOMALY"
        )

        print(
            f"Value: {anomaly['value']}"
        )

        print(
            f"Normal Mean: {anomaly['mean']}"
        )

        print(
            f"Z-Score: {anomaly['z_score']}"
        )

        print(
            anomaly["message"]
        )

        print()

else:

    print(
        "✅ No anomalies detected."
    )