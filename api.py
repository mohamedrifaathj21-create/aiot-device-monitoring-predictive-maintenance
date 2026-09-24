from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from anomaly_detector import detect_anomalies
from predictive_maintenance import predict_maintenance
import os


# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    raise Exception("MONGODB_URI not found in .env")


# --------------------------------------------------
# MONGODB CONNECTION
# --------------------------------------------------

mongo_client = MongoClient(MONGO_URI)

db = mongo_client["aiot_database"]
collection = db["telemetry"]


# --------------------------------------------------
# FASTAPI APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="AIoT Device Monitoring API",
    description="API for monitoring IoT device telemetry",
    version="1.2.0"
)


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "AIoT Device Monitoring API is running",
        "device": "MCH-007",
        "status": "online"
    }


# --------------------------------------------------
# GET TELEMETRY
# --------------------------------------------------

@app.get("/telemetry")
def get_telemetry():

    documents = list(
        collection.find(
            {},
            {"_id": 0}
        )
        .sort("timestamp", -1)
        .limit(20)
    )

    return documents


# --------------------------------------------------
# GET LATEST TELEMETRY
# --------------------------------------------------

@app.get("/telemetry/latest")
def get_latest_telemetry():

    document = collection.find_one(
        {},
        {"_id": 0},
        sort=[("timestamp", -1)]
    )

    if document is None:
        return {
            "message": "No telemetry data found"
        }

    return document


# --------------------------------------------------
# GET DEVICES
# --------------------------------------------------

@app.get("/devices")
def get_devices():

    devices = collection.distinct(
        "device_id"
    )

    return {
        "devices": devices
    }


# --------------------------------------------------
# GET SPECIFIC DEVICE
# --------------------------------------------------

@app.get("/devices/{device_id}")
def get_device(device_id: str):

    documents = list(
        collection.find(
            {
                "device_id": device_id
            },
            {
                "_id": 0
            }
        )
        .sort("timestamp", -1)
        .limit(20)
    )

    return documents


# --------------------------------------------------
# ANOMALY DETECTION
# --------------------------------------------------

@app.get("/telemetry/anomalies")
def get_anomalies():

    documents = list(
        collection.find(
            {},
            {"_id": 0}
        )
        .sort("timestamp", 1)
        .limit(50)
    )

    if len(documents) < 5:

        return {
            "message": "Not enough telemetry data for anomaly detection.",
            "data_points": len(documents),
            "anomaly_count": 0,
            "anomalies": []
        }

    anomalies = detect_anomalies(
        documents
    )

    return {
        "message": "Anomaly detection completed.",
        "data_points": len(documents),
        "anomaly_count": len(anomalies),
        "anomalies": anomalies
    }


# --------------------------------------------------
# PREDICTIVE MAINTENANCE
# --------------------------------------------------

@app.get("/telemetry/maintenance")
def get_maintenance_prediction():

    documents = list(
        collection.find(
            {},
            {"_id": 0}
        )
        .sort("timestamp", 1)
        .limit(50)
    )

    if not documents:

        return {
            "message": "No telemetry data found.",
            "health_score": 0,
            "health_status": "UNKNOWN",
            "maintenance_risk": "UNKNOWN",
            "recommendation": "Waiting for telemetry data."
        }

    result = predict_maintenance(
        documents
    )

    return {
        "message": "Predictive maintenance analysis completed.",
        "data_points": len(documents),
        **result
    }