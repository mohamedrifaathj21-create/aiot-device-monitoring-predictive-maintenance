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

# Test the connection
client.admin.command("ping")

print("MongoDB Atlas connection successful! ✅")

client.close()

print("Connection closed.")