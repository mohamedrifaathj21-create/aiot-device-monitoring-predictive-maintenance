from predictive_maintenance import predict_maintenance


def test_predictive_maintenance():
    # Simulated machine trend
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

    result = predict_maintenance(telemetry)

    # Verify expected result structure
    assert "health_score" in result
    assert "health_status" in result
    assert "maintenance_risk" in result
    assert "recommendation" in result
    assert "sensor_trends" in result

    # Verify sensor trend results exist
    assert "temperature" in result["sensor_trends"]
    assert "vibration" in result["sensor_trends"]
    assert "pressure" in result["sensor_trends"]

    # Health score should be numeric
    assert isinstance(result["health_score"], (int, float))

    # Health score should be within expected range
    assert 0 <= result["health_score"] <= 100