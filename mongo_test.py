import os

from dotenv import load_dotenv
from pymongo import MongoClient


# Load variables from .env
load_dotenv()

# Get MongoDB connection string
MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    print("ERROR: MONGODB_URI not found in .env")
    exit()


print("Connecting to MongoDB Atlas...")

client = MongoClient(MONGO_URI)

try:
    # Test MongoDB connection
    client.admin.command("ping")
    print("MongoDB Atlas connection successful! ✅")

    # Select database and collection
    db = client["aiot_database"]
    collection = db["telemetry"]

    # Count documents
    count = collection.count_documents({})

    print(f"Total telemetry records: {count}")

    # Get the latest 5 records
    records = collection.find().sort("timestamp", -1).limit(5)

    print("\nLatest telemetry records:\n")

    for record in records:
        print(f"Device: {record.get('device_id')}")
        print(f"Status: {record.get('status')}")
        print(f"Timestamp: {record.get('timestamp')}")
        print(f"Readings: {record.get('readings')}")
        print("-" * 60)

finally:
    client.close()
    print("\nMongoDB connection closed.")