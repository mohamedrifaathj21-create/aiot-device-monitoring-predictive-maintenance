from datetime import datetime


def build_telemetry(device_config, readings):
    telemetry = {
        "device_id": device_config["device_id"],
        "device_type": device_config["device_type"],
        "location": device_config["location"],
        "timestamp": datetime.now().isoformat(),
        "status": device_config["status"],
        "readings": readings
    }

    return telemetry