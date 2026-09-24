import os
import requests
import streamlit as st
import pandas as pd


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AIoT Device Monitoring",
    page_icon="📊",
    layout="wide"
)


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)


# --------------------------------------------------
# API FUNCTIONS
# --------------------------------------------------

def get_latest_data():
    response = requests.get(
        f"{API_URL}/telemetry/latest",
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def get_telemetry():
    response = requests.get(
        f"{API_URL}/telemetry",
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def get_anomalies():
    response = requests.get(
        f"{API_URL}/telemetry/anomalies",
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def get_maintenance_prediction():
    response = requests.get(
        f"{API_URL}/telemetry/maintenance",
        timeout=5
    )

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:

    latest = get_latest_data()
    telemetry = get_telemetry()
    anomaly_data = get_anomalies()
    maintenance_data = get_maintenance_prediction()

except Exception as e:

    st.error(
        "Unable to connect to the FastAPI backend."
    )

    st.code(str(e))

    st.stop()


# --------------------------------------------------
# EXTRACT DEVICE INFORMATION
# --------------------------------------------------

device_id = latest.get(
    "device_id",
    "Unknown"
)

device_type = latest.get(
    "device_type",
    "Unknown"
)

location = latest.get(
    "location",
    "Unknown"
)

status = latest.get(
    "status",
    "UNKNOWN"
)

timestamp = latest.get(
    "timestamp",
    "Unknown"
)


# --------------------------------------------------
# EXTRACT SENSOR READINGS
# --------------------------------------------------

readings = latest.get(
    "readings",
    {}
)

temperature = float(
    readings.get("temperature", 0)
)

vibration = float(
    readings.get("vibration", 0)
)

pressure = float(
    readings.get("pressure", 0)
)

energy = float(
    readings.get("energy", 0)
)

humidity = float(
    readings.get("humidity", 0)
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "🏭 AIoT Device Monitoring Dashboard"
)

st.write(
    "Real-time monitoring of the Bottle Filling Machine "
    "using Python, MQTT, MongoDB Atlas and FastAPI."
)

st.divider()


# --------------------------------------------------
# SYSTEM OVERVIEW
# --------------------------------------------------

st.subheader(
    "📊 System Overview"
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Device",
        device_id
    )


with col2:

    if status == "RUNNING":

        status_display = "🟢 RUNNING"

    elif status == "WARNING":

        status_display = "🟡 WARNING"

    else:

        status_display = "🔴 FAULT"

    st.metric(
        "Machine Status",
        status_display
    )


with col3:

    critical_alerts = 0

    if temperature >= 90:
        critical_alerts += 1

    if vibration >= 5:
        critical_alerts += 1

    if pressure < 4.8 or pressure > 7.2:
        critical_alerts += 1

    st.metric(
        "Critical Alerts",
        critical_alerts
    )


with col4:

    if timestamp != "Unknown":

        display_time = (
            timestamp
            .split("T")[-1]
            .split(".")[0]
        )

    else:

        display_time = "Unknown"

    st.metric(
        "Last Update",
        display_time
    )


st.divider()


# --------------------------------------------------
# DEVICE INFORMATION
# --------------------------------------------------

st.subheader(
    "🖥️ Device Information"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.write("**Device ID**")
    st.write(device_id)


with col2:

    st.write("**Device Type**")
    st.write(device_type)


with col3:

    st.write("**Location**")
    st.write(location)


st.divider()


# --------------------------------------------------
# LIVE SENSOR MONITORING
# --------------------------------------------------

st.subheader(
    "📡 Live Sensor Monitoring"
)

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "🌡️ Temperature",
        f"{temperature:.2f} °C"
    )


with col2:

    st.metric(
        "📳 Vibration",
        f"{vibration:.2f} mm/s"
    )


with col3:

    st.metric(
        "💧 Pressure",
        f"{pressure:.2f} bar"
    )


with col4:

    st.metric(
        "⚡ Energy",
        f"{energy:.2f} kWh"
    )


with col5:

    st.metric(
        "💧 Humidity",
        f"{humidity:.2f} %RH"
    )


st.divider()


# --------------------------------------------------
# MACHINE HEALTH
# --------------------------------------------------

st.subheader(
    "🩺 Machine Health"
)

if status == "RUNNING":

    st.success(
        "🟢 MACHINE HEALTH: NORMAL\n\n"
        "All monitored parameters are within "
        "the normal range."
    )

elif status == "WARNING":

    st.warning(
        "🟡 MACHINE HEALTH: WARNING\n\n"
        "One or more sensor values require attention."
    )

else:

    st.error(
        "🔴 MACHINE HEALTH: FAULT\n\n"
        "A critical sensor condition has been detected."
    )


st.divider()


# --------------------------------------------------
# ACTIVE ALERTS
# --------------------------------------------------

st.subheader(
    "🚨 Active Alerts"
)

alerts = []


# Temperature
if temperature >= 90:

    alerts.append(
        f"🔴 CRITICAL — Temperature: "
        f"{temperature:.2f} °C"
    )

elif temperature >= 85:

    alerts.append(
        f"🟡 WARNING — Temperature: "
        f"{temperature:.2f} °C"
    )


# Vibration
if vibration >= 5:

    alerts.append(
        f"🔴 CRITICAL — Vibration: "
        f"{vibration:.2f} mm/s"
    )

elif vibration >= 4:

    alerts.append(
        f"🟡 WARNING — Vibration: "
        f"{vibration:.2f} mm/s"
    )


# Pressure
if pressure < 4.8:

    alerts.append(
        f"🔴 CRITICAL — Pressure too low: "
        f"{pressure:.2f} bar"
    )

elif pressure > 7.2:

    alerts.append(
        f"🔴 CRITICAL — Pressure too high: "
        f"{pressure:.2f} bar"
    )

elif pressure < 5:

    alerts.append(
        f"🟡 WARNING — Pressure low: "
        f"{pressure:.2f} bar"
    )

elif pressure > 7:

    alerts.append(
        f"🟡 WARNING — Pressure high: "
        f"{pressure:.2f} bar"
    )


if alerts:

    for alert in alerts:

        if "CRITICAL" in alert:

            st.error(alert)

        else:

            st.warning(alert)

else:

    st.success(
        "✅ No active alerts. "
        "Machine operating normally."
    )


st.divider()


# --------------------------------------------------
# ANOMALY DETECTION
# --------------------------------------------------

st.subheader(
    "🤖 Anomaly Detection"
)

anomaly_count = anomaly_data.get(
    "anomaly_count",
    0
)

data_points = anomaly_data.get(
    "data_points",
    0
)

anomalies = anomaly_data.get(
    "anomalies",
    []
)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Telemetry Data Points",
        data_points
    )


with col2:

    st.metric(
        "Detected Anomalies",
        anomaly_count
    )


if anomaly_count == 0:

    st.success(
        "✅ No unusual sensor behavior detected."
    )

else:

    st.warning(
        f"⚠️ {anomaly_count} anomal"
        f"{'y' if anomaly_count == 1 else 'ies'} "
        "detected."
    )

    for anomaly in anomalies:

        sensor = anomaly.get(
            "sensor",
            "Unknown"
        )

        value = anomaly.get(
            "value",
            "Unknown"
        )

        mean = anomaly.get(
            "mean",
            "Unknown"
        )

        z_score = anomaly.get(
            "z_score",
            "Unknown"
        )

        message = anomaly.get(
            "message",
            "Unusual sensor behavior detected."
        )

        st.error(
            f"🔴 {sensor.upper()} ANOMALY"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"**Current Value:** {value}"
            )

        with col2:

            st.write(
                f"**Normal Mean:** {mean}"
            )

        with col3:

            st.write(
                f"**Z-Score:** {z_score}"
            )

        st.write(
            f"ℹ️ {message}"
        )


st.divider()


# --------------------------------------------------
# PREDICTIVE MAINTENANCE
# --------------------------------------------------

st.subheader(
    "🔧 Predictive Maintenance"
)

health_score = maintenance_data.get(
    "health_score",
    0
)

health_status = maintenance_data.get(
    "health_status",
    "UNKNOWN"
)

maintenance_risk = maintenance_data.get(
    "maintenance_risk",
    "UNKNOWN"
)

recommendation = maintenance_data.get(
    "recommendation",
    "No recommendation available."
)

sensor_trends = maintenance_data.get(
    "sensor_trends",
    {}
)


temperature_trend = sensor_trends.get(
    "temperature",
    "UNKNOWN"
)

vibration_trend = sensor_trends.get(
    "vibration",
    "UNKNOWN"
)

pressure_trend = sensor_trends.get(
    "pressure",
    "UNKNOWN"
)


# --------------------------------------------------
# MAINTENANCE CARDS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🩺 Health Score",
        f"{health_score}%"
    )


with col2:

    if health_status == "GOOD":

        status_display = "🟢 GOOD"

    elif health_status == "WARNING":

        status_display = "🟡 WARNING"

    elif health_status == "CRITICAL":

        status_display = "🔴 CRITICAL"

    else:

        status_display = "⚪ UNKNOWN"

    st.metric(
        "Machine Health",
        status_display
    )


with col3:

    if maintenance_risk == "LOW":

        risk_display = "🟢 LOW"

    elif maintenance_risk == "MEDIUM":

        risk_display = "🟡 MEDIUM"

    elif maintenance_risk == "HIGH":

        risk_display = "🔴 HIGH"

    else:

        risk_display = "⚪ UNKNOWN"

    st.metric(
        "Maintenance Risk",
        risk_display
    )


# --------------------------------------------------
# HEALTH MESSAGE
# --------------------------------------------------

if health_status == "GOOD":

    st.success(
        "🟢 Machine is operating normally."
    )

elif health_status == "WARNING":

    st.warning(
        "🟡 Machine requires closer monitoring."
    )

elif health_status == "CRITICAL":

    st.error(
        "🔴 Machine requires maintenance attention."
    )

else:

    st.info(
        "⚪ Machine health status is currently unknown."
    )


# --------------------------------------------------
# MAINTENANCE RECOMMENDATION
# --------------------------------------------------

st.write(
    "**🛠️ Maintenance Recommendation**"
)

st.info(
    recommendation
)


# --------------------------------------------------
# SENSOR TRENDS
# --------------------------------------------------

st.write(
    "**📈 Sensor Trends**"
)


def display_trend(trend):

    if trend == "INCREASING":

        return "📈 INCREASING"

    elif trend == "DECREASING":

        return "📉 DECREASING"

    elif trend == "STABLE":

        return "➡️ STABLE"

    else:

        return "⚪ UNKNOWN"


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "🌡️ Temperature Trend",
        display_trend(temperature_trend)
    )


with col2:

    st.metric(
        "📳 Vibration Trend",
        display_trend(vibration_trend)
    )


with col3:

    st.metric(
        "💧 Pressure Trend",
        display_trend(pressure_trend)
    )


st.divider()


# --------------------------------------------------
# SENSOR HISTORY
# --------------------------------------------------

st.subheader(
    "📈 Sensor History"
)

if telemetry:

    df = pd.DataFrame(
        telemetry
    )

    # Flatten readings
    if "readings" in df.columns:

        readings_df = pd.json_normalize(
            df["readings"]
        )

        df = pd.concat(
            [
                df.drop(
                    columns=["readings"]
                ),
                readings_df
            ],
            axis=1
        )

    # Timestamp
    if "timestamp" in df.columns:

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        df = df.sort_values(
            "timestamp"
        )

        df = df.set_index(
            "timestamp"
        )


    # Temperature
    if "temperature" in df.columns:

        st.write(
            "### 🌡️ Temperature"
        )

        st.line_chart(
            df["temperature"]
        )


    # Vibration
    if "vibration" in df.columns:

        st.write(
            "### 📳 Vibration"
        )

        st.line_chart(
            df["vibration"]
        )


    # Pressure
    if "pressure" in df.columns:

        st.write(
            "### 💧 Pressure"
        )

        st.line_chart(
            df["pressure"]
        )


    # Energy
    if "energy" in df.columns:

        st.write(
            "### ⚡ Energy"
        )

        st.line_chart(
            df["energy"]
        )


    # Humidity
    if "humidity" in df.columns:

        st.write(
            "### 💧 Humidity"
        )

        st.line_chart(
            df["humidity"]
        )


else:

    st.info(
        "No telemetry history available."
    )


st.divider()


# --------------------------------------------------
# RECENT TELEMETRY
# --------------------------------------------------

st.subheader(
    "📋 Recent Telemetry"
)

if telemetry:

    display_df = pd.DataFrame(
        telemetry
    )

    st.dataframe(
        display_df,
        use_container_width=True
    )

else:

    st.info(
        "No telemetry data available."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🔄 AIoT monitoring system | "
    "Python • MQTT • MongoDB Atlas • FastAPI • Streamlit"
)